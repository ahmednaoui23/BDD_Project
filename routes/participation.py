from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.participation import Participation
from models.database import get_db
from schemas.participation import ParticipationCreate

router = APIRouter(tags=["Participation"])

# Créer une participation via Form fields

@router.post("/participations")
def create_participation(participation: ParticipationCreate, db: Session = Depends(get_db)):
    db_part = Participation(
        id_citoyen=participation.id_citoyen,
        id_consultation=participation.id_consultation,
        date_participation=participation.date_participation,
        avis=participation.avis
    )
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

# Lister toutes les participations
@router.get("/participations")
def list_participations(db: Session = Depends(get_db)):
    return db.query(Participation).all()

# Récupérer une participation par citoyen et consultation
@router.get("/participations/{id_citoyen}/{id_consultation}")
def get_participation(id_citoyen: int, id_consultation: int, db: Session = Depends(get_db)):
    part = db.query(Participation).filter(
        Participation.id_citoyen == id_citoyen,
        Participation.id_consultation == id_consultation
    ).first()
    if not part:
        raise HTTPException(status_code=404, detail="Participation non trouvée")
    return part

# Supprimer une participation
@router.delete("/participations/{id_citoyen}/{id_consultation}")
def delete_participation(id_citoyen: int, id_consultation: int, db: Session = Depends(get_db)):
    part = db.query(Participation).filter(
        Participation.id_citoyen == id_citoyen,
        Participation.id_consultation == id_consultation
    ).first()
    if not part:
        raise HTTPException(status_code=404, detail="Participation non trouvée")
    db.delete(part)
    db.commit()
    return {"detail": "Participation supprimée avec succès"}
