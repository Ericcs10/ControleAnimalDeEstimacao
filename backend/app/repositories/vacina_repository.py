from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.vacina_schema import VacinaSchema
from app.repositories.base_repository import BaseRepository

class VacinaRepository(BaseRepository[VacinaSchema]):
    collection = db["vacinas"]

    @staticmethod
    async def criar(vacina: VacinaSchema) -> str:
        vacina_dict = vacina.model_dump()
        result = await VacinaRepository.collection.insert_one(vacina_dict)
        return str(result.inserted_id)

    @staticmethod
    async def listar() -> List[dict]:
        vacinas = await VacinaRepository.collection.find().to_list(100)
        for v in vacinas:
            v["id"] = str(v["_id"])
            v.pop("_id", None)
        return vacinas

    @staticmethod
    async def buscar_por_id(vacina_id: str) -> Optional[dict]:
        vacina = await VacinaRepository.collection.find_one({"_id": ObjectId(vacina_id)})
        if vacina:
            vacina["id"] = str(vacina["_id"])
            vacina.pop("_id", None)
        return vacina

    @staticmethod
    async def atualizar(vacina_id: str, data: dict) -> bool:
        result = await VacinaRepository.collection.update_one(
            {"_id": ObjectId(vacina_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(vacina_id: str) -> bool:
        result = await VacinaRepository.collection.delete_one({"_id": ObjectId(vacina_id)})
        return result.deleted_count > 0

    @staticmethod
    async def listar_por_animal(animal_id: str) -> List[dict]:
        vacinas = await VacinaRepository.collection.find({"animal_id": ObjectId(animal_id)}).to_list(100)
        for v in vacinas:
            v["id"] = str(v["_id"])
            v.pop("_id", None)
        return vacinas 