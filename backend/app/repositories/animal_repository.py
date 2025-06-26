from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.animal_schema import AnimalSchema
from app.schemas.objectid_schema import PyObjectId
from app.repositories.base_repository import BaseRepository

class AnimalRepository(BaseRepository[AnimalSchema]):

    @staticmethod
    async def criar(animal: AnimalSchema) -> PyObjectId:
        animal_dict = animal.model_dump()
        result = await db["animais"].insert_one(animal_dict)
        return result.inserted_id

    @staticmethod
    async def listar() -> List[dict]:
        return await db["animais"].find().to_list(100)

    @staticmethod
    async def buscar_por_id(animal_id: str) -> Optional[dict]:
        return await db["animais"].find_one({"_id": ObjectId(animal_id)})

    @staticmethod
    async def atualizar(animal_id: str, dados: dict) -> bool:
        result = await db["animais"].update_one(
            {"_id": ObjectId(animal_id)}, {"$set": dados}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(animal_id: str) -> bool:
        result = await db["animais"].delete_one({"_id": ObjectId(animal_id)})
        return result.deleted_count > 0
