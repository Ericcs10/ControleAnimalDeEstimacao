from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.animal_schema import AnimalSchema
from app.services.animal_service import AnimalService


router = APIRouter(prefix="/animais", tags=["Animais"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_animal(animal: AnimalSchema):
    animal_id = await AnimalService.criar(animal)
    return {"id": animal_id}


@router.get("/", response_model=List[dict])
async def listar_animais():
    return await AnimalService.listar()


@router.get("/{animal_id}", response_model=dict)
async def buscar_animal(animal_id: str):
    animal = await AnimalService.buscar_por_id(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return animal


@router.put("/{animal_id}")
async def atualizar_animal(animal_id: str, dados: AnimalSchema):
    atualizado = await AnimalService.atualizar(animal_id, dados)
    if not atualizado:
        raise HTTPException(
            status_code=404, detail="Animal não encontrado ou nada foi alterado"
        )
    return {"msg": "Animal atualizado com sucesso"}


@router.delete("/{animal_id}")
async def deletar_animal(animal_id: str):
    deletado = await AnimalService.deletar(animal_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Animal não encontrado")
    return {"msg": "Animal removido com sucesso"}
