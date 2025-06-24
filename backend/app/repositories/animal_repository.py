from typing import List, Optional
from app.core.database import db
from app.schemas.animal_schema import AnimalSchema
from bson import ObjectId
from datetime import datetime


collection = db.animais


async def listar_animais() -> List[AnimalSchema]:
    return await collection.find().to_list(1000)


async def buscar_animal_por_id(animal_id: str) -> Optional[AnimalSchema]:
    return await collection.find_one({"_id": ObjectId(animal_id)})


async def criar_animal(animal: AnimalSchema) -> AnimalSchema:
    data = animal.dict()
    data["data_criacao"] = datetime.utcnow()
    data["data_atualizacao"] = datetime.utcnow()

    result = await collection.insert_one(data)
    return await collection.find_one({"_id": result.inserted_id})


async def atualizar_animal(animal_id: str, animal: AnimalSchema) -> Optional[AnimalSchema]:
    data = animal.dict()
    data["data_atualizacao"] = datetime.utcnow()

    await collection.update_one({"_id": ObjectId(animal_id)}, {"$set": data})
    return await collection.find_one({"_id": ObjectId(animal_id)})


async def deletar_animal(animal_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(animal_id)})
    return result.deleted_count == 1
