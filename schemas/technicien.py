from pydantic import BaseModel

# Pour la création d'un technicien (POST)
class TechnicienCreate(BaseModel):
    nom: str
    prenom: str

# Pour la lecture d'un technicien (GET)
class TechnicienRead(BaseModel):
    id_technicien: int
    nom: str
    prenom: str

    class Config:
        orm_mode = True  # obligatoire pour convertir SQLAlchemy -> Pydantic
