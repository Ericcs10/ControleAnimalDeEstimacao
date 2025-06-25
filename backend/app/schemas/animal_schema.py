from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.schemas.enums import Especie, Sexo
from app.schemas.objectid_schema import PyObjectId 


class AnimalSchema(BaseModel):
    """
    Schema para cadastro e leitura de animais.
    """
    usuario_id: PyObjectId = Field(...)
    especie: Especie
    raca: PyObjectId = Field(...)
    nome: str
    data_nascimento: datetime
    sexo: Sexo
    foto_url: Optional[str] = None  # <-- Adicionado o campo opcional
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }
