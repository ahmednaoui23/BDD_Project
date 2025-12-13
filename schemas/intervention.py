from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InterventionCreate(BaseModel):
    date_intervention: datetime
    nature_intervention: str
    duree: int
    cout: float
    impact_environnemental: Optional[float] = None
    validation_ia: bool
    id_capteur: str  # UUID
    id_technicien_intervient: Optional[int] = None
    id_technicien_valide: Optional[int] = None

class InterventionRead(InterventionCreate):
    id_intervention: int

    class Config:
        orm_mode = True
