from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.animal_schema import AnimalCreate, AnimalRead
from app.repositories.base_repository import BaseRepository


class AnimalRepository(BaseRepository[AnimalCreate]):
    collection = db["animais"]

    @staticmethod
    async def criar(animal: AnimalCreate) -> str:
        try:
            animal_dict = animal.model_dump()
            animal_dict["usuario_id"] = ObjectId(str(animal_dict["usuario_id"]))
            animal_dict["raca"] = ObjectId(str(animal_dict["raca"]))
            result = await AnimalRepository.collection.insert_one(animal_dict)
            return str(result.inserted_id)
        except Exception as e:
            print("Erro ao criar animal:", e)
            raise

    @staticmethod
    async def listar() -> List[AnimalRead]:
        animais = await AnimalRepository.collection.find().to_list(100)
        return [AnimalRead(**{
            **a,
            "id": str(a["_id"]),
            "usuario_id": str(a["usuario_id"]),
            "raca": str(a["raca"]),
        }) for a in animais]

    @staticmethod
    async def buscar_por_id(animal_id: str) -> Optional[AnimalRead]:
        animal = await AnimalRepository.collection.find_one({"_id": ObjectId(animal_id)})
        if animal:
            return AnimalRead(**{
                **animal,
                "id": str(animal["_id"]),
                "usuario_id": str(animal["usuario_id"]),
                "raca": str(animal["raca"]),
            })
        return None

    @staticmethod
    async def atualizar(animal_id: str, dados: dict) -> bool:
        if not dados:
            return False
        result = await AnimalRepository.collection.update_one(
            {"_id": ObjectId(animal_id)},
            {"$set": dados}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(animal_id: str) -> bool:
        result = await AnimalRepository.collection.delete_one({"_id": ObjectId(animal_id)})
        return result.deleted_count > 0
