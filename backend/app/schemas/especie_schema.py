from pydantic import BaseModel

class EspecieSchema(BaseModel):
    nome: str

class EspecieDBSchema(EspecieSchema):
    id: str
