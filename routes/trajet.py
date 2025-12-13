from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.trajet import Trajet
from models.database import get_db

router = APIRouter(tags=["Trajet"])

# Créer un trajet via Form
@router.post("/trajets")
def create_trajet(
    origine: str = Form(...),
    destination: str = Form(...),
    economie_co2: float = Form(...),
    db: Session = Depends(get_db)
):
    db_trajet = Trajet(origine=origine, destination=destination, economie_CO2=economie_CO2)
    db.add(db_trajet)
    db.commit()
    db.refresh(db_trajet)
    return db_trajet

# Lister tous les trajets
@router.get("/trajets")
def list_trajets(db: Session = Depends(get_db)):
    return db.query(Trajet).all()

# Récupérer un trajet par ID
@router.get("/trajets/{id}")
def get_trajet(id: int, db: Session = Depends(get_db)):
    trajet = db.query(Trajet).filter(Trajet.id_trajet == id).first()
    if not trajet:
        raise HTTPException(status_code=404, detail="Trajet non trouvé")
    return trajet

# Supprimer un trajet par ID
@router.delete("/trajets/{id}")
def delete_trajet(id: int, db: Session = Depends(get_db)):
    trajet = db.query(Trajet).filter(Trajet.id_trajet == id).first()
    if not trajet:
        raise HTTPException(status_code=404, detail="Trajet non trouvé")
    db.delete(trajet)
    db.commit()
    return {"detail": "Trajet supprimé avec succès"}
