from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Intervention(Base):
    __tablename__ = "intervention"

    id_intervention = Column(Integer, primary_key=True, index=True)
    date_intervention = Column(TIMESTAMP, nullable=False)
    nature_intervention = Column(String(50), nullable=False)
    duree = Column(Integer, nullable=False)
    cout = Column(Float, nullable=False)
    impact_environnemental = Column(Float)
    validation_ia = Column(Boolean, nullable=False)
    id_capteur = Column(ForeignKey("capteur.id_capteur"))
    id_technicien_intervient = Column(ForeignKey("technicien.id_technicien"))
    id_technicien_valide = Column(ForeignKey("technicien.id_technicien"))

    capteur = relationship("Capteur", back_populates="interventions")
    technicien_intervient = relationship("Technicien", back_populates="interventions_intervient", foreign_keys=[id_technicien_intervient])
    technicien_valide = relationship("Technicien", back_populates="interventions_valide", foreign_keys=[id_technicien_valide])
