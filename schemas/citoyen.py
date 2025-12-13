from pydantic import BaseModel
from typing import Optional

class CitoyenCreate(BaseModel):
    nom: str
    adresse: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    score_engagement: float
    preference_mobilite: Optional[str] = None

class CitoyenRead(CitoyenCreate):
    id_citoyen: int

    class Config:
        orm_mode = True
