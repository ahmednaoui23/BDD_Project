from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.intervention import Intervention
from models.database import get_db
from datetime import datetime

router = APIRouter(tags=["Intervention"])

# Créer une intervention via Form fields
@router.post("/interventions")
def create_intervention(
    date_intervention: str = Form(...),   # à parser en datetime si besoin
    nature_intervention: str = Form(...),
    duree: int = Form(...),
    cout: float = Form(...),
    impact_environnemental: float = Form(0),
    validation_IA: bool = Form(...),
    id_capteur: str = Form(...),
    id_technicien_intervient: int = Form(...),
    db: Session = Depends(get_db)
):
    db_interv = Intervention(
        date_intervention=datetime.strptime(date_intervention, "%Y-%m-%d %H:%M:%S"),
        nature_intervention=nature_intervention,
        duree=duree,
        cout=cout,
        impact_environnemental=impact_environnemental,
        validation_ia=validation_ia,
        id_capteur=id_capteur,
        id_technicien_intervient=id_technicien_intervient
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
