from pydantic import BaseModel
from datetime import datetime
class EffectueCreate(BaseModel):
    immatriculation: str
    id_trajet: int
    date_execution: datetime

class EffectueRead(EffectueCreate):
    class Config:
        orm_mode = True
