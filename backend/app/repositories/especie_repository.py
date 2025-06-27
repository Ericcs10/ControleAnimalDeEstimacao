from typing import Optional, List
from bson import ObjectId
from app.core.database import db 
from app.models.especie_model import Especie

class EspecieRepository:
    collection = db["especies"]

    @staticmethod
    def criar(nome: str) -> str:
        especie = Especie(nome=nome)
        result = EspecieRepository.collection.insert_one(especie.to_dict())
        return str(result.inserted_id)

    @staticmethod
    def listar() -> List[dict]:
        especies = EspecieRepository.collection.find()
        return [{"id": str(e["_id"]), "nome": e["nome"]} for e in especies]

    @staticmethod
    def buscar_por_id(especie_id: str) -> Optional[dict]:
        doc = EspecieRepository.collection.find_one({"_id": ObjectId(especie_id)})
        if doc:
            return {"id": str(doc["_id"]), "nome": doc["nome"]}
        return None

    @staticmethod
    def atualizar(especie_id: str, nome: str) -> bool:
        result = EspecieRepository.collection.update_one(
            {"_id": ObjectId(especie_id)},
            {"$set": {"nome": nome}}
        )
        return result.modified_count > 0

    @staticmethod
    def deletar(especie_id: str) -> bool:
        result = EspecieRepository.collection.delete_one({"_id": ObjectId(especie_id)})
        return result.deleted_count > 0
