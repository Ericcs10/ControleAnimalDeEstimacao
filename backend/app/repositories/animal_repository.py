from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.animal_schema import AnimalCreate
from app.schemas.objectid_schema import PyObjectId
from app.repositories.base_repository import BaseRepository


class AnimalRepository(BaseRepository[AnimalCreate]):
    collection = db["animais"]

    @staticmethod
    async def criar(animal: AnimalCreate) -> PyObjectId:
        animal_dict = animal.model_dump()
        result = await AnimalRepository.collection.insert_one(animal_dict)
        return result.inserted_id

    @staticmethod
    async def listar() -> List[dict]:
        animais = await AnimalRepository.collection.find().to_list(100)
        for a in animais:
            a["id"] = str(a["_id"])
            a.pop("_id", None)
        return animais

    @staticmethod
    async def buscar_por_id(animal_id: str) -> Optional[dict]:
        animal = await AnimalRepository.collection.find_one({"_id": ObjectId(animal_id)})
        if animal:
            animal["id"] = str(animal["_id"])
            animal.pop("_id", None)
        return animal

    @staticmethod
    async def atualizar(animal_id: str, dados: dict) -> bool:
        if not dados:
            return False  # Evita atualização nula
        result = await AnimalRepository.collection.update_one(
            {"_id": ObjectId(animal_id)},
            {"$set": dados}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(animal_id: str) -> bool:
        result = await AnimalRepository.collection.delete_one({"_id": ObjectId(animal_id)})
        return result.deleted_count > 0
