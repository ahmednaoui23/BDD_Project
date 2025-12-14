from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Technicien(Base):
    __tablename__ = "technicien"

    id_technicien = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)

    interventions_intervient = relationship("Intervention", back_populates="technicien_intervient", foreign_keys="Intervention.id_technicien_intervient")
    interventions_valide = relationship("Intervention", back_populates="technicien_valide", foreign_keys="Intervention.id_technicien_valide")
