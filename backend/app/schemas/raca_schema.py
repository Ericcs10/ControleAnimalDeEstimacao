from pydantic import BaseModel
from .enums import Especie

class RacaSchema(BaseModel):
    tipo: str
    especie: Especie
    temperamento: str
    porte: str
