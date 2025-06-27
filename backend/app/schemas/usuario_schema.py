from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime 

class UsuarioBase(BaseModel): 
    email: EmailStr = Field(..., example="exemplo@teste.com")
    cpf: str = Field(..., example="12345678900")
    telefone: str = Field(..., example="61999999999")

class UsuarioCreate(UsuarioBase): 
    senha: str = Field(..., example="senha123")

class UsuarioUpdate(UsuarioBase): 
    senha: Optional[str] = Field(None, example="senha123")

class UsuarioDB(UsuarioBase): 
    id: Optional[str] = Field(default=None)  # Alterado de PyObjectId para str
    senha: str
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
