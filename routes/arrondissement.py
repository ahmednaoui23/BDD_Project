from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models.arrondissement import Arrondissement
from models.database import get_db
from schemas.arrondissement import ArrondissementCreate

router = APIRouter(tags=["Arrondissement"])

# POST pour créer un arrondissement avec Form, compatible Postman sans Content-Type JSON
@router.post("/arrondissements")
def create_arrondissement(trajet: ArrondissementCreate, db: Session = Depends(get_db)):
    db_arr = Arrondissement(
        nom_arrondissement=trajet.nom_arrondissement,
        type_arrondissement=trajet.type_arrondissement
    )
    db.add(db_arr)
    db.commit()
    db.refresh(db_arr)
    return db_arr

# GET pour lister tous les arrondissements
@router.get("/arrondissements")
def list_arrondissements(db: Session = Depends(get_db)):
    return db.query(Arrondissement).all()

# GET pour un arrondissement par ID
@router.get("/arrondissements/{id}")
def get_arrondissement(id: int, db: Session = Depends(get_db)):
    arr = db.query(Arrondissement).filter(Arrondissement.id_arrondissement == id).first()
    if not arr:
        raise HTTPException(status_code=404, detail="Arrondissement non trouvé")
    return arr

# DELETE pour un arrondissement par ID
@router.delete("/arrondissements/{id}")
def delete_arrondissement(id: int, db: Session = Depends(get_db)):
    arr = db.query(Arrondissement).filter(Arrondissement.id_arrondissement == id).first()
    if not arr:
        raise HTTPException(status_code=404, detail="Arrondissement non trouvé")
    db.delete(arr)
    db.commit()
    return {"detail": "Arrondissement supprimé avec succès"}
