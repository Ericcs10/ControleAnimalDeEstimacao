from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.animal_schema import AnimalSchema
from app.repositories import animal_repository


router = APIRouter(prefix="/animais", tags=["Animais"])


@router.get("/", response_model=List[AnimalSchema])
async def listar_animais():
    return await animal_repository.listar_animais()


@router.get("/{animal_id}", response_model=AnimalSchema)
async def buscar_animal(animal_id: str):
    animal = await animal_repository.buscar_animal_por_id(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal


@router.post("/", response_model=AnimalSchema, status_code=201)
async def criar_animal(animal: AnimalSchema):
    return await animal_repository.criar_animal(animal)


@router.put("/{animal_id}", response_model=AnimalSchema)
async def atualizar_animal(animal_id: str, animal: AnimalSchema):
    animal_atualizado = await animal_repository.atualizar_animal(animal_id, animal)
    if not animal_atualizado:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal_atualizado


@router.delete("/{animal_id}")
async def deletar_animal(animal_id: str):
    deletado = await animal_repository.deletar_animal(animal_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return {"message": "Animal deletado com sucesso"}
