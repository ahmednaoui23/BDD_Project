from pydantic import BaseModel

class VehiculeCreate(BaseModel):
    immatriculation: str
    type_vehicule: str
    energie_utilisee: str

class VehiculeRead(VehiculeCreate):
    class Config:
        orm_mode = True
