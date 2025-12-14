from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Citoyen(Base):
    __tablename__ = "citoyen"

    id_citoyen = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    adresse = Column(Text)
    telephone = Column(String(15))
    email = Column(String(100))
    score_engagement = Column(Float, nullable=False)
    preference_mobilite = Column(Text)

    # ← Nouvelle colonne FK vers arrondissement
    id_arrondissement = Column(Integer, ForeignKey("arrondissement.id_arrondissement"))

    # Relations
    arrondissement = relationship("Arrondissement", back_populates="citoyens")
    participations = relationship("Participation", back_populates="citoyen")
