from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.consultation_citoyenne import ConsultationCitoyenne
from models.database import get_db

router = APIRouter(tags=["Consultation"])

# POST avec Form fields
@router.post("/consultations")
def create_consultation(
    titre: str = Form(...),
    description: str = Form(...),
    date_debut: str = Form(...),  # si tu utilises datetime, tu peux parser plus tard
    date_fin: str = Form(...),
    db: Session = Depends(get_db)
):
    db_cons = ConsultationCitoyenne(
        titre=titre,
        description=description,
        date_debut=date_debut,
        date_fin=date_fin
    )
    db.add(db_cons)
    db.commit()
    db.refresh(db_cons)
    return db_cons

# Lister toutes les consultations
@router.get("/consultations")
def list_consultations(db: Session = Depends(get_db)):
    return db.query(ConsultationCitoyenne).all()

# Récupérer une consultation par ID
@router.get("/consultations/{id}")
def get_consultation(id: int, db: Session = Depends(get_db)):
    cons = db.query(ConsultationCitoyenne).filter(ConsultationCitoyenne.id_consultation == id).first()
    if not cons:
        raise HTTPException(status_code=404, detail="Consultation non trouvée")
    return cons

# Supprimer une consultation par ID
@router.delete("/consultations/{id}")
def delete_consultation(id: int, db: Session = Depends(get_db)):
    cons = db.query(ConsultationCitoyenne).filter(ConsultationCitoyenne.id_consultation == id).first()
    if not cons:
        raise HTTPException(status_code=404, detail="Consultation non trouvée")
    db.delete(cons)
    db.commit()
    return {"detail": "Consultation supprimée avec succès"}
