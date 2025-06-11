from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from bson import ObjectId

class UsuarioSchema(BaseModel):
    
    email: EmailStr
    cpf: str
    telefone: str
    senha_hash: str
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    class Config:
        json_encoders = {ObjectId: str}
