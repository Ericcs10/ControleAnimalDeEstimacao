from pydantic import BaseModel
from app.schemas.enums import Especie
from bson import ObjectId

class RacaSchema(BaseModel):
    tipo: str
    pelagem: str
    tamanho_pelagem: str
    temperamento: str
    especie: Especie

    class Config:
        json_encoders = {ObjectId: str}
