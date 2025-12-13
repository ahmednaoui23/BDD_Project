from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MesureCreate(BaseModel):
    date_mesure: datetime
    valeur: float
    unite: str
    type_mesure: str
    id_capteur: str  # UUID

class MesureRead(MesureCreate):
    id_mesure: int

    class Config:
        orm_mode = True
