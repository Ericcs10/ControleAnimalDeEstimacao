from typing import List, Optional
from bson import ObjectId
from app.repositories.animal_repository import AnimalRepository
from app.schemas.animal_schema import AnimalSchema
from app.schemas.objectid_schema import PyObjectId


class AnimalService:

    @staticmethod
    async def criar(animal: AnimalSchema) -> str:
        animal_id = await AnimalRepository.criar(animal)
        return str(animal_id)

    @staticmethod
    async def listar() -> List[dict]:
        animais = await AnimalRepository.listar()
        for a in animais:
            a["id"] = str(a["_id"])
            a.pop("_id", None)
        return animais

    @staticmethod
    async def buscar_por_id(animal_id: str) -> Optional[dict]:
        animal = await AnimalRepository.buscar_por_id(animal_id)
        if animal:
            animal["id"] = str(animal["_id"])
            animal.pop("_id", None)
        return animal

    @staticmethod
    async def atualizar(animal_id: str, dados: AnimalSchema) -> bool:
        return await AnimalRepository.atualizar(animal_id, dados.model_dump())

    @staticmethod
    async def deletar(animal_id: str) -> bool:
        return await AnimalRepository.deletar(animal_id)
