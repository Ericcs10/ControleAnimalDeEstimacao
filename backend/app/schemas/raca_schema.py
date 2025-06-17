from pydantic import BaseModel
from app.schemas.enums import Especie
from app.schemas.objectid_schema import PyObjectId


class RacaSchema(BaseModel):
    tipo: str
    pelagem: str
    tamanho_pelagem: str
    temperamento: str
    especie: Especie

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str}
    }
