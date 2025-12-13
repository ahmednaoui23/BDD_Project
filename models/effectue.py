from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Effectue(Base):
    __tablename__ = "effectue"

    immatriculation = Column(ForeignKey("vehicule.immatriculation"), primary_key=True)
    id_trajet = Column(ForeignKey("trajet.id_trajet"), primary_key=True)
    date_execution = Column(TIMESTAMP, nullable=False)

    vehicule = relationship("Vehicule", back_populates="effectues")
    trajet = relationship("Trajet", back_populates="effectues")
