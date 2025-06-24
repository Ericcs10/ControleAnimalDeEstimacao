from typing import List, Optional
from app.core.database import db
from app.schemas.vacina_schema import VacinaSchema
from bson import ObjectId


collection = db.vacinas


async def listar_vacinas() -> List[VacinaSchema]:
    return await collection.find().to_list(1000)


async def buscar_vacina_por_id(vacina_id: str) -> Optional[VacinaSchema]:
    return await collection.find_one({"_id": ObjectId(vacina_id)})


async def criar_vacina(vacina: VacinaSchema) -> VacinaSchema:
    data = vacina.dict()

    result = await collection.insert_one(data)
    return await collection.find_one({"_id": result.inserted_id})


async def atualizar_vacina(vacina_id: str, vacina: VacinaSchema) -> Optional[VacinaSchema]:
    data = vacina.dict()

    await collection.update_one({"_id": ObjectId(vacina_id)}, {"$set": data})
    return await collection.find_one({"_id": ObjectId(vacina_id)})


async def deletar_vacina(vacina_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(vacina_id)})
    return result.deleted_count == 1
