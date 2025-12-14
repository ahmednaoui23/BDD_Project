from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.citoyen import Citoyen
from models.database import get_db
from schemas.citoyen import CitoyenCreate

router = APIRouter(tags=["Citoyen"])

# Créer un citoyen avec Form
@router.post("/citoyens")
def create_citoyen(citoyen: CitoyenCreate, db: Session = Depends(get_db)):
    db_citoyen = Citoyen(
        nom=citoyen.nom,
        email=citoyen.email,
        adresse=citoyen.adresse,
        telephone=citoyen.telephone,
        score_engagement=citoyen.score_engagement,
        preference_mobilite=citoyen.preference_mobilite,
        id_arrondissement=citoyen.id_arrondissement,
    )
    db.add(db_citoyen)
    db.commit()
    db.refresh(db_citoyen)
    return db_citoyen

# Lister tous les citoyens
@router.get("/citoyens")
def list_citoyens(db: Session = Depends(get_db)):
    return db.query(Citoyen).all()

# Récupérer un citoyen par ID
@router.get("/citoyens/{id}")
def get_citoyen(id: int, db: Session = Depends(get_db)):
    citoyen = db.query(Citoyen).filter(Citoyen.id_citoyen == id).first()
    if not citoyen:
        raise HTTPException(status_code=404, detail="Citoyen non trouvé")
    return citoyen

# Supprimer un citoyen par ID
@router.delete("/citoyens/{id}")
def delete_citoyen(id: int, db: Session = Depends(get_db)):
    citoyen = db.query(Citoyen).filter(Citoyen.id_citoyen == id).first()
    if not citoyen:
        raise HTTPException(status_code=404, detail="Citoyen non trouvé")
    db.delete(citoyen)
    db.commit()
    return {"detail": "Citoyen supprimé avec succès"}
