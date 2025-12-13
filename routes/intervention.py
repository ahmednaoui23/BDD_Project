from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.intervention import Intervention
from models.database import get_db
from datetime import datetime

from schemas.intervention import InterventionCreate

router = APIRouter(tags=["Intervention"])

# Créer une intervention via Form fields
@router.post("/interventions")
def create_intervention(intervention: InterventionCreate, db: Session = Depends(get_db)):
    db_interv = Intervention(
        date_intervention=intervention.date_intervention,
        nature_intervention=intervention.nature_intervention,
        duree=intervention.duree,
        cout=intervention.cout,
        impact_environnemental=intervention.impact_environnemental,
        validation_ia=intervention.validation_ia,
        id_capteur=intervention.id_capteur,
        id_technicien_intervient=intervention.id_technicien_intervient
    )
    db.add(db_interv)
    db.commit()
    db.refresh(db_interv)
    return db_interv

# Lister toutes les interventions
@router.get("/interventions")
def list_interventions(db: Session = Depends(get_db)):
    return db.query(Intervention).all()

# Récupérer une intervention par ID
@router.get("/interventions/{id}")
def get_intervention(id: int, db: Session = Depends(get_db)):
    interv = db.query(Intervention).filter(Intervention.id_intervention == id).first()
    if not interv:
        raise HTTPException(status_code=404, detail="Intervention non trouvée")
    return interv

# Supprimer une intervention par ID
@router.delete("/interventions/{id}")
def delete_intervention(id: int, db: Session = Depends(get_db)):
    interv = db.query(Intervention).filter(Intervention.id_intervention == id).first()
    if not interv:
        raise HTTPException(status_code=404, detail="Intervention non trouvée")
    db.delete(interv)
    db.commit()
    return {"detail": "Intervention supprimée avec succès"}
