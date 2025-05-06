# backend/app/main.py
from fastapi import FastAPI, HTTPException, status, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import EmailStr
from datetime import datetime
from typing import Optional, List
from .models import Pet, PetCreate, PetUpdate, PetType
import os

app = FastAPI(
    title="Controle de Animais API",
    description="API para gerenciamento de animais de estimação",
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "email": "seu.email@example.com",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(
        os.getenv("MONGODB_URL", "mongodb://root:example@mongo:27017")
    )
    app.mongodb = app.mongodb_client[os.getenv("MONGO_DB", "petdb")]
    await app.mongodb.pets.create_index("name")
    await app.mongodb.pets.create_index("type")

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.post("/pets/", response_model=Pet, status_code=status.HTTP_201_CREATED)
async def create_pet(pet: PetCreate):
    pet_dict = pet.dict()
    pet_dict["created_at"] = pet_dict["updated_at"] = datetime.utcnow()
    
    try:
        new_pet = await app.mongodb.pets.insert_one(pet_dict)
        created_pet = await app.mongodb.pets.find_one({"_id": new_pet.inserted_id})
        return created_pet
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar pet: {str(e)}"
        )

@app.get("/pets/", response_model=List[Pet])
async def list_pets(
    type: Optional[PetType] = None,
    vaccinated: Optional[bool] = None,
    limit: int = Query(10, gt=0, le=100),
    skip: int = Query(0, ge=0)
):
    query = {}
    if type:
        query["type"] = type
    if vaccinated is not None:
        query["vaccinated"] = vaccinated
    
    pets = []
    async for pet in app.mongodb.pets.find(query).skip(skip).limit(limit):
        pets.append(pet)
    return pets

@app.get("/pets/{pet_id}", response_model=Pet)
async def read_pet(pet_id: str):
    if (pet := await app.mongodb.pets.find_one({"_id": pet_id})) is not None:
        return pet
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pet com ID {pet_id} não encontrado"
    )

@app.put("/pets/{pet_id}", response_model=Pet)
async def update_pet(pet_id: str, pet_update: PetUpdate):
    update_data = pet_update.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.utcnow()
    
    if len(update_data) >= 1:
        result = await app.mongodb.pets.update_one(
            {"_id": pet_id},
            {"$set": update_data}
        )
        
        if result.modified_count == 1:
            if (updated_pet := await app.mongodb.pets.find_one({"_id": pet_id})) is not None:
                return updated_pet
    
    if (existing_pet := await app.mongodb.pets.find_one({"_id": pet_id})) is not None:
        return existing_pet
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pet com ID {pet_id} não encontrado"
    )

@app.delete("/pets/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pet(pet_id: str):
    delete_result = await app.mongodb.pets.delete_one({"_id": pet_id})
    
    if delete_result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet com ID {pet_id} não encontrado"
        )
    
    return None

@app.get("/pets/types/", response_model=List[str])
async def get_pet_types():
    return [pet_type.value for pet_type in PetType]

@app.get("/pets/stats/vaccinated", response_model=dict)
async def get_vaccination_stats():
    total = await app.mongodb.pets.count_documents({})
    vaccinated = await app.mongodb.pets.count_documents({"vaccinated": True})
    
    return {
        "total_pets": total,
        "vaccinated": vaccinated,
        "vaccination_rate": vaccinated / total if total > 0 else 0
    }