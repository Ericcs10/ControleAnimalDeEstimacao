from pydantic import BaseModel, Field
from app.schemas.enums import Especie
from app.schemas.objectid_schema import PyObjectId
from typing import Optional
from datetime import datetime

class RacaBase(BaseModel): 
    tipo: str = Field(..., example="Labrador")
    pelagem: str = Field(..., example="Curta")
    tamanho_pelagem: str = Field(..., example="Média")
    temperamento: str = Field(..., example="Amigável")
    especie: Especie

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }

class RacaCreate(RacaBase): 
    pass

class RacaUpdate(BaseModel):
    tipo: Optional[str] = None
    pelagem: Optional[str] = None
    tamanho_pelagem: Optional[str] = None
    temperamento: Optional[str] = None
    especie: Optional[Especie] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }

class RacaRead(RacaBase):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
