from typing import List, Optional
from app.core.database import db
from app.schemas.raca_schema import RacaSchema
from bson import ObjectId


collection = db.racas


async def listar_racas() -> List[RacaSchema]:
    return await collection.find().to_list(1000)


async def buscar_raca_por_id(raca_id: str) -> Optional[RacaSchema]:
    return await collection.find_one({"_id": ObjectId(raca_id)})


async def criar_raca(raca: RacaSchema) -> RacaSchema:
    data = raca.dict()

    result = await collection.insert_one(data)
    return await collection.find_one({"_id": result.inserted_id})


async def atualizar_raca(raca_id: str, raca: RacaSchema) -> Optional[RacaSchema]:
    data = raca.dict()

    await collection.update_one({"_id": ObjectId(raca_id)}, {"$set": data})
    return await collection.find_one({"_id": ObjectId(raca_id)})


async def deletar_raca(raca_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(raca_id)})
    return result.deleted_count == 1
