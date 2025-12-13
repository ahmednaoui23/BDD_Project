from pydantic import BaseModel
from typing import Optional
from datetime import date

class CapteurCreate(BaseModel):
    type_capteur: str
    statut: str
    date_installation: date
    id_proprietaire: Optional[int] = None
    id_arrondissement: Optional[int] = None

class CapteurRead(CapteurCreate):
    id_capteur: str  # UUID

    class Config:
        orm_mode = True
