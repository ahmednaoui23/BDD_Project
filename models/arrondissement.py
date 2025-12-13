from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Arrondissement(Base):
    __tablename__ = "arrondissement"

    id_arrondissement = Column(Integer, primary_key=True, index=True)
    nom_arrondissement = Column(String(100), nullable=False)
    type_arrondissement = Column(String(50))

    capteurs = relationship("Capteur", back_populates="arrondissement")
    consultations = relationship("ConsultationCitoyenne", back_populates="arrondissement")
    trajets_depart = relationship("Trajet", back_populates="arrondissement_depart", foreign_keys="Trajet.id_arrondissement_depart")
    trajets_arrivee = relationship("Trajet", back_populates="arrondissement_arrivee", foreign_keys="Trajet.id_arrondissement_arrivee")
