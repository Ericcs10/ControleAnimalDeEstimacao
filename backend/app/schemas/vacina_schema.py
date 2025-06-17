from pydantic import BaseModel
from datetime import datetime
from app.schemas.objectid_schema import PyObjectId
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

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str}
    }
