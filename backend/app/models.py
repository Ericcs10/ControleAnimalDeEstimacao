# backend/app/models.py

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class PetType(str, Enum):
    DOG = "cachorro"
    CAT = "gato"
    BIRD = "pássaro"
    FISH = "peixe"
    OTHER = "outro"

class PetBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="Rex")
    type: PetType = Field(..., example=PetType.DOG)
    age: int = Field(..., gt=0, le=30, example=3)
    breed: Optional[str] = Field(None, max_length=50, example="Labrador")
    owner_name: Optional[str] = Field(None, max_length=100, example="João Silva")
    owner_email: Optional[EmailStr] = None
    vaccinated: bool = Field(default=False)
    adopted: bool = Field(default=False)

class PetCreate(PetBase):
    pass

class Pet(PetBase):
    id: str = Field(alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class PetUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    age: Optional[int] = Field(None, gt=0, le=30)
    vaccinated: Optional[bool] = None
    adopted: Optional[bool] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)