from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models.trajet import Trajet
from models.arrondissement import Arrondissement
from models.database import get_db
from pydantic import BaseModel

from schemas.trajet import TrajetCreate

router = APIRouter(tags=["Trajet"])
# Créer un trajet
@router.post("/trajets")
def create_trajet(trajet: TrajetCreate, db: Session = Depends(get_db)):
    # Récupérer les arrondissements via les IDs
    origine = db.query(Arrondissement).filter(Arrondissement.id_arrondissement == trajet.id_arrondissement_depart).first()
    destination = db.query(Arrondissement).filter(Arrondissement.id_arrondissement == trajet.id_arrondissement_arrivee).first()

    if not origine or not destination:
        raise HTTPException(status_code=404, detail="Arrondissement d'origine ou de destination non trouvé")

    # Convertir date_depart
    try:
        date_depart_obj = datetime.strptime(trajet.date_depart, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise HTTPException(status_code=400, detail="Format de date_depart incorrect. Utilisez YYYY-MM-DD HH:MM:SS")

    # Créer le trajet
    db_trajet = Trajet(
        id_arrondissement_depart=trajet.id_arrondissement_depart,
        id_arrondissement_arrivee=trajet.id_arrondissement_arrivee,
        origine=origine.nom_arrondissement,
        destination=destination.nom_arrondissement,
        economie_co2=trajet.economie_co2,
        duree=trajet.duree,
        date_depart=date_depart_obj,
        date_arrivee=date_depart_obj + timedelta(minutes=trajet.duree)
    )
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
