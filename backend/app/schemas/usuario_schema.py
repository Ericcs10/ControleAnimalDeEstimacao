from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId

class UsuarioSchema(BaseModel):
    email: EmailStr
    cpf: str
    telefone: str
    senha: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "exemplo@teste.com",
                "cpf": "12345678900",
                "telefone": "61999999999",
                "senha": "123456"
            }
        }
    }

class UsuarioDB(UsuarioSchema):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
