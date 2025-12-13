from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.mesure import Mesure
from models.database import get_db
from datetime import datetime

from schemas.mesure import MesureCreate

router = APIRouter(tags=["Mesure"])

# Créer une mesure via Form fields

@router.post("/mesures")
def create_mesure(mesure: MesureCreate, db: Session = Depends(get_db)):
    db_mes = Mesure(
        valeur=mesure.valeur,
        unite=mesure.unite,
        date_mesure=mesure.date_mesure,
        id_capteur=mesure.id_capteur
    )
    db.add(db_mes)
    db.commit()
    db.refresh(db_mes)
    return db_mes

# Lister toutes les mesures
@router.get("/mesures")
def list_mesures(db: Session = Depends(get_db)):
    return db.query(Mesure).all()

# Récupérer une mesure par ID
@router.get("/mesures/{id}")
def get_mesure(id: int, db: Session = Depends(get_db)):
    mes = db.query(Mesure).filter(Mesure.id_mesure == id).first()
    if not mes:
        raise HTTPException(status_code=404, detail="Mesure non trouvée")
    return mes

# Supprimer une mesure par ID
@router.delete("/mesures/{id}")
def delete_mesure(id: int, db: Session = Depends(get_db)):
    mes = db.query(Mesure).filter(Mesure.id_mesure == id).first()
    if not mes:
        raise HTTPException(status_code=404, detail="Mesure non trouvée")
    db.delete(mes)
    db.commit()
    return {"detail": "Mesure supprimée avec succès"}
