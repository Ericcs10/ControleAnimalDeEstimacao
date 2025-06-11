from pydantic import BaseModel, EmailStr
from typing import List, Optional
from bson import ObjectId
from datetime import datetime
from .enums import Sexo

class UsuarioSchema(BaseModel):
    nome: str
    email: EmailStr
    cpf: str
    senha: str
    sexo: Sexo
    data_nascimento: datetime
    animais: Optional[List[ObjectId]] = []

    class Config:
        json_encoders = {ObjectId: str}
