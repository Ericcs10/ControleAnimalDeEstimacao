from pydantic import BaseModel
from datetime import datetime
from bson import ObjectId
from app.schemas.enums import Intervalo

class VacinaSchema(BaseModel):
    animal_id: ObjectId
    nome: str
    data: datetime
    lote: str
    laboratorio: str
    necessita_revacina: bool
    periodo: int
    intervalo: Intervalo
    proxima_dose: datetime


    class model_config:
        json_encoders = {ObjectId: str}
