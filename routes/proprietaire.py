from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.proprietaire import Proprietaire
from models.database import get_db
from schemas.proprietaire import ProprietaireCreate

router = APIRouter(tags=["Proprietaire"])

@router.post("/proprietaires")
def create_proprietaire(prop: ProprietaireCreate, db: Session = Depends(get_db)):
    db_prop = Proprietaire(
        nom=prop.nom,
        email=prop.email,
        type=prop.type,
        adresse=prop.adresse,
        telephone=prop.telephone,
    )
    db.add(db_prop)
    db.commit()
    db.refresh(db_prop)
    return db_prop

# Lister tous les propriétaires
@router.get("/proprietaires")
def list_proprietaires(db: Session = Depends(get_db)):
    return db.query(Proprietaire).all()

# Récupérer un propriétaire par ID
@router.get("/proprietaires/{id}")
def get_proprietaire(id: int, db: Session = Depends(get_db)):
    prop = db.query(Proprietaire).filter(Proprietaire.id_proprietaire == id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Propriétaire non trouvé")
    return prop

# Supprimer un propriétaire par ID
@router.delete("/proprietaires/{id}")
def delete_proprietaire(id: int, db: Session = Depends(get_db)):
    prop = db.query(Proprietaire).filter(Proprietaire.id_proprietaire == id).first()
    if not prop:
        raise HTTPException(status_code=404, detail="Propriétaire non trouvé")
    db.delete(prop)
    db.commit()
    return {"detail": "Propriétaire supprimé avec succès"}
