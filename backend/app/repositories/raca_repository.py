from typing import List, Optional
from bson import ObjectId 
from datetime import datetime, timezone
from app.core.database import db
from app.schemas.raca_schema import RacaCreate, RacaUpdate, RacaRead

class RacaRepository:
    collection = db["racas"]

    @staticmethod
    async def criar(raca: RacaCreate) -> str:
        try:
            dados = raca.model_dump()
            now = datetime.now(timezone.utc)
            dados["data_criacao"] = now
            dados["data_atualizacao"] = now
            result = await RacaRepository.collection.insert_one(dados)
            return str(result.inserted_id)
        except Exception as e:
            print("Erro ao criar raca:", e)
            raise

    @staticmethod
    async def listar() -> List[RacaRead]:
        racas = await RacaRepository.collection.find().to_list(100)
        for r in racas:
            r["id"] = str(r.pop("_id"))
        return racas

    @staticmethod
    async def buscar_por_id(raca_id: str) -> Optional[RacaRead]:
        raca = await RacaRepository.collection.find_one({"_id": ObjectId(raca_id)})
        if raca:
            raca["id"] = str(raca.pop("_id"))
        return raca

    @staticmethod
    async def atualizar(raca_id: str, data: dict) -> bool:
        data["data_atualizacao"] = datetime.now(timezone.utc)
        result = await RacaRepository.collection.update_one(
            {"_id": ObjectId(raca_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(raca_id: str) -> bool:
        result = await RacaRepository.collection.delete_one({"_id": ObjectId(raca_id)})
        return result.deleted_count > 0
    