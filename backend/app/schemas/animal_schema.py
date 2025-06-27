from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.enums import Especie, Sexo
from app.schemas.objectid_schema import PyObjectId


class AnimalCreate(BaseModel):
    usuario_id: PyObjectId = Field(...)
    especie: Especie
    raca: PyObjectId = Field(...)
    nome: str
    data_nascimento: datetime
    sexo: Sexo
    foto_url: Optional[str] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }


class AnimalUpdate(BaseModel):
    usuario_id: Optional[PyObjectId] = None
    especie: Optional[Especie] = None
    raca: Optional[PyObjectId] = None
    nome: Optional[str] = None
    data_nascimento: Optional[datetime] = None
    sexo: Optional[Sexo] = None
    foto_url: Optional[str] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }


class AnimalRead(AnimalCreate):
    id: str
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None


class AnimalDB(AnimalRead):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
