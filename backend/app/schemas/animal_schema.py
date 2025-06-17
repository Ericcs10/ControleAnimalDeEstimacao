from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.objectid_schema import PyObjectId
from app.schemas.enums import Especie, Sexo


class AnimalSchema(BaseModel):
    usuario_id: ObjectId
    especie: Especie
    raca: ObjectId
    nome: str
    data_nascimento: datetime
    sexo: Sexo
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str}
    }
