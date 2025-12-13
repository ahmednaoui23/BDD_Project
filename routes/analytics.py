from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.database import get_db
from models.capteur import Capteur
from models.arrondissement import Arrondissement
from models.mesure import Mesure
from models.citoyen import Citoyen
from models.intervention import Intervention
from models.trajet import Trajet
from datetime import datetime, timedelta

router = APIRouter(tags=["Analytics"])


def score_mesure(mesure: Mesure):
    poids = {
        "Qualité de l'air": 2,
        "Trafic": 1,
        "Énergie": 0.5,
        "Déchets": 1.5,
        "Éclairage": 0.2
    }
    return (mesure.valeur or 0) * poids.get(mesure.type_mesure, 1)

@router.get("/zones-plus-polluees")
def zones_plus_polluees(db: Session = Depends(get_db)):
    arrs = db.query(Arrondissement).all()
    result = []

    for arr in arrs:
        score_total = 0
        capteurs = db.query(Capteur).filter(Capteur.id_arrondissement == arr.id_arrondissement).all()
        for cap in capteurs:
            mesures = db.query(Mesure).filter(Mesure.id_capteur == cap.id_capteur).all()
            for mes in mesures:
                score_total += score_mesure(mes)
        result.append({"arrondissement": arr.nom_arrondissement, "score_total": score_total})

    # Trier par score décroissant
    result.sort(key=lambda x: x["score_total"], reverse=True)
    return result

# 2. Taux de disponibilité des capteurs par arrondissement
@router.get("/taux-disponibilite-capteurs")
def taux_disponibilite_capteurs(db: Session = Depends(get_db)):
    arrs = db.query(Arrondissement).all()
    result = []
    for arr in arrs:
        capteurs = db.query(Capteur).filter(Capteur.id_arrondissement == arr.id_arrondissement).all()
        total = len(capteurs)
        actifs = len([c for c in capteurs if c.statut.lower() == "actif"])
        taux = (actifs / total * 100) if total else 0
        result.append({"arrondissement": arr.nom_arrondissement, "taux_disponibilite": taux})
    return result

# 3. Citoyens les plus engagés
@router.get("/citoyens-plus-engages")
def citoyens_plus_engages(db: Session = Depends(get_db)):
    citoyens = db.query(Citoyen).order_by(Citoyen.score_engagement.desc()).limit(10).all()
    return [{"nom": c.nom, "score_engagement": c.score_engagement} for c in citoyens]

# 4. Interventions prédictives du mois et économie générée
@router.get("/interventions-predictives")
def interventions_predictives(db: Session = Depends(get_db)):
    now = datetime.now()
    debut_mois = datetime(now.year, now.month, 1)
    interventions = db.query(Intervention).filter(
        Intervention.date_intervention >= debut_mois,
        Intervention.nature_intervention.ilike("prédictive")
    ).all()
    total_economie = sum([i.impact_environnemental or 0 for i in interventions])
    return {"nombre_interventions": len(interventions), "economie_co2": total_economie}

# 5. Trajets de véhicules autonomes avec la plus grande réduction de CO2
@router.get("/trajets-plus-economiques")
def trajets_plus_economiques(db: Session = Depends(get_db)):
    trajets = db.query(Trajet).order_by(Trajet.economie_co2.desc()).limit(10).all()
    return [{"origine": t.origine, "destination": t.destination, "economie_co2": t.economie_co2} for t in trajets]
