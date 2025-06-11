from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime
from .enums import Intervalo

class VacinaSchema(BaseModel):
    nome: str
    data: datetime
    lote: str
    revacinacao: bool
    intervalo: Intervalo
    proxima_dose: datetime
    animal_id: ObjectId

    class Config:
        json_encoders = {ObjectId: str}
