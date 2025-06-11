from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from .enums import Sexo, Especie

class AnimalSchema(BaseModel):
    nome: str
    especie: Especie
    raca: ObjectId
    data_nascimento: datetime
    sexo: Sexo
    usuario_id: ObjectId
    vacinas: Optional[List[ObjectId]] = []

    class Config:
        json_encoders = {ObjectId: str}
