from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime 
 
class UsuarioSchema(BaseModel): 
    email: EmailStr
    cpf: str
    telefone: str
    senha: str  # Use "senha", não "senha_hash" na criação


class UsuarioDB(UsuarioSchema):
    id: Optional[str] = None
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
