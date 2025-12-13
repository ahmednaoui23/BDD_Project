from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Trajet(Base):
    __tablename__ = "trajet"

    id_trajet = Column(Integer, primary_key=True, index=True)
    origine = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)
    duree = Column(Integer, nullable=False)
    economie_co2 = Column(Float, nullable=False)
    date_depart = Column(TIMESTAMP)
    date_arrivee = Column(TIMESTAMP)
    id_arrondissement_depart = Column(ForeignKey("arrondissement.id_arrondissement"))
    id_arrondissement_arrivee = Column(ForeignKey("arrondissement.id_arrondissement"))

    arrondissement_depart = relationship("Arrondissement", back_populates="trajets_depart", foreign_keys=[id_arrondissement_depart])
    arrondissement_arrivee = relationship("Arrondissement", back_populates="trajets_arrivee", foreign_keys=[id_arrondissement_arrivee])
    effectues = relationship("Effectue", back_populates="trajet")
