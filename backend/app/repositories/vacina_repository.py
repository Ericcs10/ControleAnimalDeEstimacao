from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.vacina_schema import VacinaSchema 


collection = db["vacinas"]


async def create_vacina(vacina: VacinaSchema) -> str:
    vacina_dict = vacina.model_dump()
    result = await collection.insert_one(vacina_dict)
    return str(result.inserted_id)


async def get_vacinas() -> List[VacinaSchema]:
    vacinas = await collection.find().to_list(100)
    for v in vacinas:
        v["id"] = str(v["_id"])
        v.pop("_id", None)
    return vacinas


async def get_vacina_by_id(vacina_id: str) -> Optional[VacinaSchema]:
    vacina = await collection.find_one({"_id": ObjectId(vacina_id)})
    if vacina:
        vacina["id"] = str(vacina["_id"])
        vacina.pop("_id", None)
    return vacina

async def update_vacina(vacina_id: str, data: dict) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(vacina_id)}, {"$set": data}
    )
    return result.modified_count > 0


async def delete_vacina(vacina_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(vacina_id)})
    return result.deleted_count > 0
