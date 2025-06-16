from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from bson import ObjectId
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

    class model_config:
        json_encoders = {ObjectId: str}
