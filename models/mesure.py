from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Mesure(Base):
    __tablename__ = "mesure"

    id_mesure = Column(Integer, primary_key=True, index=True)
    date_mesure = Column(TIMESTAMP, nullable=False)
    valeur = Column(Float, nullable=False)
    unite = Column(String(50), nullable=False)
    type_mesure = Column(String(50), nullable=False)
    id_capteur = Column(ForeignKey("capteur.id_capteur"))

    capteur = relationship("Capteur", back_populates="mesures")
