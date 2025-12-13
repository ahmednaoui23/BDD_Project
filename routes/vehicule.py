from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.vehicule import Vehicule
from models.database import get_db
from schemas.vehicule import VehiculeCreate

router = APIRouter(tags=["Vehicule"])

# POST via Form, pas besoin de Content-Type JSON
@router.post("/vehicules")
def create_vehicule(veh: VehiculeCreate, db: Session = Depends(get_db)):
    db_veh = Vehicule(
        immatriculation=veh.immatriculation,
        type_vehicule=veh.type_vehicule,
        energie_utilisee=veh.energie_utilisee
    )
    db.add(db_veh)
    db.commit()
    db.refresh(db_veh)
    return db_veh

# Lister tous les véhicules
@router.get("/vehicules")
def list_vehicules(db: Session = Depends(get_db)):
    return db.query(Vehicule).all()

# Récupérer un véhicule par immatriculation
@router.get("/vehicules/{immatriculation}")
def get_vehicule(immatriculation: str, db: Session = Depends(get_db)):
    veh = db.query(Vehicule).filter(Vehicule.immatriculation == immatriculation).first()
    if not veh:
        raise HTTPException(status_code=404, detail="Véhicule non trouvé")
    return veh

# Supprimer un véhicule par immatriculation
@router.delete("/vehicules/{immatriculation}")
def delete_vehicule(immatriculation: str, db: Session = Depends(get_db)):
    veh = db.query(Vehicule).filter(Vehicule.immatriculation == immatriculation).first()
    if not veh:
        raise HTTPException(status_code=404, detail="Véhicule non trouvé")
    db.delete(veh)
    db.commit()
    return {"detail": "Véhicule supprimé avec succès"}
