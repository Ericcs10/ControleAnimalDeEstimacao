from typing import List, Optional
from bson import ObjectId
from datetime import datetime, timezone
from app.core.database import db
from app.schemas.vacina_schema import VacinaCreate, VacinaRead
from app.repositories.base_repository import BaseRepository

class VacinaRepository(BaseRepository[VacinaCreate]):
    collection = db["vacinas"]

    @staticmethod
    async def criar(vacina: VacinaCreate) -> str:
        dados = vacina.model_dump()
        now = datetime.now(timezone.utc)
        dados["data_criacao"] = now
        dados["data_atualizacao"] = now
        result = await VacinaRepository.collection.insert_one(dados)
        return str(result.inserted_id)

    @staticmethod
    async def listar() -> List[VacinaRead]:
        vacinas_raw = await VacinaRepository.collection.find().to_list(100)
        vacinas = []
        for v in vacinas_raw:
            v["id"] = str(v.pop("_id"))
            v["animal_id"] = str(v["animal_id"])
            v["data_criacao"] = v.get("data_criacao")
            v["data_atualizacao"] = v.get("data_atualizacao")
            vacinas.append(VacinaRead(**v))
        return vacinas

    @staticmethod
    async def buscar_por_id(vacina_id: str) -> Optional[VacinaRead]:
        vacina = await VacinaRepository.collection.find_one({"_id": ObjectId(vacina_id)})
        if vacina:
            vacina["id"] = str(vacina.pop("_id"))
            vacina["animal_id"] = str(vacina["animal_id"])
            return VacinaRead(**vacina)
        return None

    @staticmethod
    async def atualizar(vacina_id: str, data: dict) -> bool:
        data["data_atualizacao"] = datetime.now(timezone.utc)
        result = await VacinaRepository.collection.update_one(
            {"_id": ObjectId(vacina_id)}, {"$set": data}
        )
        return result.modified_count > 0

    @staticmethod
    async def deletar(vacina_id: str) -> bool:
        result = await VacinaRepository.collection.delete_one({"_id": ObjectId(vacina_id)})
        return result.deleted_count > 0

    @staticmethod
    async def listar_por_animal(animal_id: str) -> List[VacinaRead]:
        vacinas_raw = await VacinaRepository.collection.find({"animal_id": ObjectId(animal_id)}).to_list(100)
        vacinas = []
        for v in vacinas_raw:
            v["id"] = str(v.pop("_id"))
            v["animal_id"] = str(v["animal_id"])
            vacinas.append(VacinaRead(**v))
        return vacinas
    