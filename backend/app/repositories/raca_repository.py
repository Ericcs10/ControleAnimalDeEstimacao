from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.raca_schema import RacaSchema
from app.repositories.base_repository import BaseRepository

class RacaRepository(BaseRepository[RacaSchema]):
    collection = db["racas"]

    @staticmethod
    async def criar(raca: RacaSchema) -> str:
        raca_dict = raca.model_dump()
        result = await RacaRepository.collection.insert_one(raca_dict)
        return str(result.inserted_id)

    @staticmethod
    async def listar() -> List[RacaSchema]:
        racas = await RacaRepository.collection.find().to_list(100)
        for r in racas:
            r["id"] = str(r["_id"])
            r.pop("_id", None)
        return racas

    @staticmethod
    async def buscar_por_id(raca_id: str) -> Optional[RacaSchema]:
        raca = await RacaRepository.collection.find_one({"_id": ObjectId(raca_id)})
        if raca:
            raca["id"] = str(raca["_id"])
            raca.pop("_id", None)
        return raca

    @staticmethod
    async def atualizar(raca_id: str, data: dict) -> bool:
        result = await RacaRepository.collection.update_one(
            {"_id": ObjectId(raca_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(raca_id: str) -> bool:
        result = await RacaRepository.collection.delete_one({"_id": ObjectId(raca_id)})
        return result.deleted_count > 0