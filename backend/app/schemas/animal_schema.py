from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.enums import Especie, Sexo
from app.schemas.objectid_schema import PyObjectId
from bson import ObjectId


class AnimalCreate(BaseModel):
    usuario_id: PyObjectId = Field(..., example="665a4b7c25ee4c001c7db4c1")
    especie: Especie = Field(..., example="Canino")
    raca: PyObjectId = Field(..., example="665a4b7c25ee4c001c7db4c2")
    nome: str = Field(..., example="Rex")
    data_nascimento: datetime = Field(..., example="2024-06-10T00:00:00Z")
    sexo: Sexo = Field(..., example="Masculino")
    foto_url: Optional[str] = Field(None, example="https://exemplo.com/foto.jpg")

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }


class AnimalUpdate(BaseModel):
    usuario_id: Optional[PyObjectId] = Field(None, example="665a4b7c25ee4c001c7db4c1")
    especie: Optional[Especie] = Field(None, example="Canino")
    raca: Optional[PyObjectId] = Field(None, example="665a4b7c25ee4c001c7db4c2")
    nome: Optional[str] = Field(None, example="Rex")
    data_nascimento: Optional[datetime] = Field(None, example="2024-06-10T00:00:00Z")
    sexo: Optional[Sexo] = Field(None, example="Masculino")
    foto_url: Optional[str] = Field(None, example="https://exemplo.com/foto.jpg")

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }


class AnimalRead(AnimalCreate): 
    id: str
    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str}
    }
