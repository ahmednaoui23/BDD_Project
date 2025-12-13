from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.technicien import Technicien
from models.database import get_db
from schemas.technicien import TechnicienCreate

router = APIRouter(tags=["Technicien"])

# Créer un technicien via Form
@router.post("/techniciens")
def create_technicien(tech: TechnicienCreate, db: Session = Depends(get_db)):
    db_tech = Technicien(
        nom=tech.nom,
        prenom=tech.prenom,
        certification=tech.certification,
    )
    db.add(db_tech)
    db.commit()
    db.refresh(db_tech)
    return db_tech

# Lister tous les techniciens
@router.get("/techniciens")
def list_techniciens(db: Session = Depends(get_db)):
    return db.query(Technicien).all()

# Récupérer un technicien par ID
@router.get("/techniciens/{id}")
def get_technicien(id: int, db: Session = Depends(get_db)):
    tech = db.query(Technicien).filter(Technicien.id_technicien == id).first()
    if not tech:
        raise HTTPException(status_code=404, detail="Technicien non trouvé")
    return tech

# Supprimer un technicien par ID
@router.delete("/techniciens/{id}")
def delete_technicien(id: int, db: Session = Depends(get_db)):
    tech = db.query(Technicien).filter(Technicien.id_technicien == id).first()
    if not tech:
        raise HTTPException(status_code=404, detail="Technicien non trouvé")
    db.delete(tech)
    db.commit()
    return {"detail": "Technicien supprimé avec succès"}
