from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# 🔹 Charger les variables d'environnement
load_dotenv()

# 🔹 Créer l'application FastAPI
app = FastAPI(title="Smart City Analytics Platform")

# 🔹 CORS (permet à tous les frontends de consommer l'API en DEV)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔹 autorise toutes les origines en DEV
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Inclure toutes les routes avec tags
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

# 🔹 Route racine
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur la plateforme Smart City"}
