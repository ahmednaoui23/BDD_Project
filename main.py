from fastapi import FastAPI
from dotenv import load_dotenv
import os

from routes import (
    proprietaire,
    arrondissement,
    capteur,
    mesure,
    technicien,
    intervention,
    citoyen,
    consultation,
    participation,
    vehicule,
    trajet,
    effectue,
    analytics
)

# Charger les variables d'environnement
load_dotenv()

app = FastAPI(title="Smart City Analytics Platform")

# Inclure toutes les routes avec tags mais sans prefix
app.include_router(proprietaire.router, tags=["Proprietaire"])
app.include_router(arrondissement.router, tags=["Arrondissement"])
app.include_router(capteur.router, tags=["Capteur"])
app.include_router(mesure.router, tags=["Mesure"])
app.include_router(technicien.router, tags=["Technicien"])
app.include_router(intervention.router, tags=["Intervention"])
app.include_router(citoyen.router, tags=["Citoyen"])
app.include_router(consultation.router, tags=["Consultation"])
app.include_router(participation.router, tags=["Participation"])
app.include_router(vehicule.router, tags=["Vehicule"])
app.include_router(trajet.router, tags=["Trajet"])
app.include_router(effectue.router, tags=["Effectue"])
app.include_router(analytics.router, tags=["Analytics"])

# Route racine
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la plateforme Smart City"}
