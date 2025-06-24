from typing import List, Optional
from bson import ObjectId
from app.core.database import db
from app.schemas.raca_schema import RacaSchema 


collection = db["racas"]


async def create_raca(raca: RacaSchema) -> str:
    raca_dict = raca.model_dump()
    result = await collection.insert_one(raca_dict)
    return str(result.inserted_id)


async def get_racas() -> List[RacaSchema]:
    racas = await collection.find().to_list(100)
    for r in racas:
        r["id"] = str(r["_id"])
        r.pop("_id", None)
    return racas


async def get_raca_by_id(raca_id: str) -> Optional[RacaSchema]:
    raca = await collection.find_one({"_id": ObjectId(raca_id)})
    if raca:
        r["id"] = str(raca["_id"])
        r.pop("_id", None)
    return raca

async def update_raca(raca_id: str, data: dict) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(raca_id)}, {"$set": data}
    )
    return result.modified_count > 0


async def delete_raca(raca_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(raca_id)})
    return result.deleted_count > 0
