from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from app.schemas.objectid_schema import PyObjectId


class UsuarioBase(BaseModel):
    email: EmailStr = Field(..., example="exemplo@teste.com")
    cpf: str = Field(..., example="12345678900")
    telefone: str = Field(..., example="61999999999")

    model_config = { 
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }


class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., example="senha123")


class UsuarioUpdate(UsuarioBase):
    senha: Optional[str] = Field(None, example="senha123")


class UsuarioSchema(UsuarioCreate):
    pass


class UsuarioDB(UsuarioBase):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    senha: str
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
