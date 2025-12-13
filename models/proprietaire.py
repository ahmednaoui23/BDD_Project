from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .database import Base

class Proprietaire(Base):
    __tablename__ = "proprietaire"

    id_proprietaire = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    type = Column(String(50))
    adresse = Column(Text)
    telephone = Column(String(15))
    email = Column(String(100))

    capteurs = relationship("Capteur", back_populates="proprietaire")
