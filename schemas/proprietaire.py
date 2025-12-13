from pydantic import BaseModel
from typing import Optional

class ProprietaireCreate(BaseModel):
    nom: str
    type: Optional[str] = None
    adresse: Optional[str] = None
    telephone: Optional[str] = None
    email: Optional[str] = None

class ProprietaireRead(ProprietaireCreate):
    id_proprietaire: int

    class Config:
        orm_mode = True
