from pydantic import BaseModel
from datetime import date
from typing import Optional

class ParticipationCreate(BaseModel):
    id_citoyen: int
    id_consultation: int
    date_participation: date
    avis: Optional[str] = None

class ParticipationRead(ParticipationCreate):
    class Config:
        orm_mode = True
