from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.capteur import Capteur
from models.database import get_db

router = APIRouter(tags=["Capteur"])

# Créer un capteur avec Form
@router.post("/capteurs")
def create_capteur(
    nom_capteur: str = Form(...),
    type_capteur: str = Form(...),
    id_arrondissement: int = Form(...),
    statut: str = Form(...),
    db: Session = Depends(get_db)
):
    db_cap = Capteur(
        nom_capteur=nom_capteur,
        type_capteur=type_capteur,
        id_arrondissement=id_arrondissement,
        statut=statut
    )
    db.add(db_cap)
    db.commit()
    db.refresh(db_cap)
    return db_cap

# Lister tous les capteurs
@router.get("/capteurs")
def list_capteurs(db: Session = Depends(get_db)):
    return db.query(Capteur).all()

# Récupérer un capteur par ID
@router.get("/capteurs/{id}")
def get_capteur(id: str, db: Session = Depends(get_db)):
    cap = db.query(Capteur).filter(Capteur.id_capteur == id).first()
    if not cap:
        raise HTTPException(status_code=404, detail="Capteur non trouvé")
    return cap

# Supprimer un capteur par ID
@router.delete("/capteurs/{id}")
def delete_capteur(id: str, db: Session = Depends(get_db)):
    cap = db.query(Capteur).filter(Capteur.id_capteur == id).first()
    if not cap:
        raise HTTPException(status_code=404, detail="Capteur non trouvé")
    db.delete(cap)
    db.commit()
    return {"detail": "Capteur supprimé avec succès"}
