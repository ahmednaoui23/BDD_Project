from pydantic import BaseModel
from typing import Optional

class ArrondissementCreate(BaseModel):
    nom_arrondissement: str
    type_arrondissement: Optional[str] = None

class ArrondissementRead(ArrondissementCreate):
    id_arrondissement: int

    class Config:
        orm_mode = True
