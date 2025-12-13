from sqlalchemy import Column, Integer, String, Float, Text
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

    participations = relationship("Participation", back_populates="citoyen")
