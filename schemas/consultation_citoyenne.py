from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ConsultationCreate(BaseModel):
    date_consultation: datetime
    titre: str
    id_arrondissement: Optional[int] = None

class ConsultationRead(ConsultationCreate):
    id_consultation: int

    class Config:
        orm_mode = True
