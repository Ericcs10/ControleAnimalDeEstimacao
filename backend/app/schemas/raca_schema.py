from pydantic import BaseModel
from app.schemas.enums import Especie
from bson import ObjectId

class RacaSchema(BaseModel):
    tipo: str
    pelagem: str
    tamanho_pelagem: str
    temperamento: str
    especie: Especie

    class model_config:
        json_encoders = {ObjectId: str}
