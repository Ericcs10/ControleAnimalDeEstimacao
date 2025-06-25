from app.core.database import db
from bson import ObjectId
from app.models.especie_model import Especie

collection = db["especies"]

def create_especie(especie: Especie) -> ObjectId:
    result = collection.insert_one(especie.to_dict())
    return result.inserted_id

def get_all_especies():
    return [Especie.from_dict(e) for e in collection.find()]

def get_especie_by_id(especie_id: str):
    doc = collection.find_one({"_id": ObjectId(especie_id)})
    return Especie.from_dict(doc) if doc else None

def update_especie(especie_id: str, nome: str) -> bool:
    result = collection.update_one({"_id": ObjectId(especie_id)}, {"$set": {"nome": nome}})
    return result.modified_count > 0

def delete_especie(especie_id: str) -> bool:
    result = collection.delete_one({"_id": ObjectId(especie_id)})
    return result.deleted_count > 0
