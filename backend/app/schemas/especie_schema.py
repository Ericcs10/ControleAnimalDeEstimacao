from pydantic import BaseModel, Field
from typing import Optional


class EspecieSchema(BaseModel):
    nome: str = Field(..., example="Canino")


class EspecieDBSchema(EspecieSchema):
    id: str = Field(..., example="665a4b7c25ee4c001c7db4c1")
