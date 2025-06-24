from pydantic import BaseModel, Field
from datetime import datetime
from app.schemas.enums import Intervalo
from app.schemas.objectid_schema import PyObjectId
from typing import Optional


class VacinaSchema(BaseModel):
    """
    Schema para cadastro de vacinas.
    """
    animal_id: PyObjectId = Field(...)
    nome: str
    data: datetime
    lote: str
    laboratorio: str
    necessita_revacina: bool
    periodo: int
    intervalo: Intervalo
    proxima_dose: datetime
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }
