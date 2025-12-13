from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.effectue import Effectue
from models.database import get_db

router = APIRouter(tags=["Effectue"])

# POST avec Form fields
@router.post("/effectues")
def create_effectue(
    immatriculation: str = Form(...),
    id_trajet: int = Form(...),
    date_eff: str = Form(...),  # si c'est datetime, parser plus tard
    db: Session = Depends(get_db)
):
    db_effect = Effectue(
        immatriculation=immatriculation,
        id_trajet=id_trajet,
        date_eff=date_eff
    )
    db.add(db_effect)
    db.commit()
    db.refresh(db_effect)
    return db_effect

# Lister tous les effectues
@router.get("/effectues")
def list_effectues(db: Session = Depends(get_db)):
    return db.query(Effectue).all()

# Récupérer un effectue par immatriculation et id_trajet
@router.get("/effectues/{immatriculation}/{id_trajet}")
def get_effectue(immatriculation: str, id_trajet: int, db: Session = Depends(get_db)):
    effect = db.query(Effectue).filter(
        Effectue.immatriculation == immatriculation,
        Effectue.id_trajet == id_trajet
    ).first()
    if not effect:
        raise HTTPException(status_code=404, detail="Effectué non trouvé")
    return effect

# Supprimer un effectue par immatriculation et id_trajet
@router.delete("/effectues/{immatriculation}/{id_trajet}")
def delete_effectue(immatriculation: str, id_trajet: int, db: Session = Depends(get_db)):
    effect = db.query(Effectue).filter(
        Effectue.immatriculation == immatriculation,
        Effectue.id_trajet == id_trajet
    ).first()
    if not effect:
        raise HTTPException(status_code=404, detail="Effectué non trouvé")
    db.delete(effect)
    db.commit()
    return {"detail": "Effectué supprimé avec succès"}
