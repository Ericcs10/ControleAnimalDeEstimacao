from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.schemas.enums import Intervalo
from app.schemas.objectid_schema import PyObjectId 

class VacinaBase(BaseModel):
    animal_id: PyObjectId = Field(..., example="60c72b2f9b1e8a3f1d4e7c0a")
    nome: str = Field(..., example="Antirrábica")
    data: datetime = Field(..., example="2025-01-15T14:30:00Z")
    lote: str = Field(..., example="A1234")
    laboratorio: str = Field(..., example="LabVet")
    necessita_revacina: bool = Field(..., example=True)
    periodo: int = Field(..., example=12)
    intervalo: Intervalo = Field(..., example="MESES")
    proxima_dose: datetime = Field(..., example="2026-01-15T14:30:00Z")

    model_config = {
        "arbitrary_types_allowed": True,
        "json_encoders": {PyObjectId: str}
    }

class VacinaCreate(VacinaBase): 
    pass

class VacinaUpdate(VacinaBase): 
    pass

class VacinaRead(VacinaBase):
    id: str = Field(..., example="665a4b7c25ee4c001c7db4c1")
    data_criacao: Optional[datetime] = None
    data_atualizacao: Optional[datetime] = None
    