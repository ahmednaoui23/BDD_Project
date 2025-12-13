from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TrajetCreate(BaseModel):
    origine: str
    destination: str
    duree: int
    economie_co2: float
    date_depart: Optional[datetime] = None
    date_arrivee: Optional[datetime] = None
    id_arrondissement_depart: Optional[int] = None
    id_arrondissement_arrivee: Optional[int] = None

class TrajetRead(TrajetCreate):
    id_trajet: int

    class Config:
        orm_mode = True
