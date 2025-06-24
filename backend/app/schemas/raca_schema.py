from pydantic import BaseModel, Field
from app.schemas.enums import Especie
from app.schemas.objectid_schema import PyObjectId
from typing import Optional
from datetime import datetime


class RacaSchema(BaseModel):
    """
    Schema para cadastro de raças.
    """
    tipo: str
    pelagem: str
    tamanho_pelagem: str
    temperamento: str
    especie: Especie
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }
