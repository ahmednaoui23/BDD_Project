from pydantic import BaseModel



class TrajetCreate(BaseModel):
    id_arrondissement_depart: int
    id_arrondissement_arrivee: int
    economie_co2: float
    duree: int = 30
    date_depart: str  # format "YYYY-MM-DD HH:MM:SS"

class TrajetRead(TrajetCreate):
    id_trajet: int
    origine: str
    destination: str
    date_arrivee: str  # format "YYYY-MM-DD HH:MM:SS"

    class Config:
        orm_mode = True
