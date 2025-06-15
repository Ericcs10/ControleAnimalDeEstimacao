from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from bson import ObjectId

class UsuarioCreateSchema(BaseModel):
    email: EmailStr
    cpf: str
    telefone: str
    senha: str  # Entrada bruta para ser hasheada internamente

class UsuarioSchema(BaseModel):
    id: Optional[str]
    email: EmailStr
    cpf: str
    telefone: str
    senha_hash: Optional[str]
    data_criacao: Optional[datetime]
    data_atualizacao: Optional[datetime]

    class Config:
        json_encoders = {ObjectId: str}
        orm_mode = True
