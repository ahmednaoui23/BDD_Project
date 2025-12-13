from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .database import Base

class Vehicule(Base):
    __tablename__ = "vehicule"

    immatriculation = Column(String(20), primary_key=True, index=True)
    type_vehicule = Column(String(50), nullable=False)
    energie_utilisee = Column(String(50), nullable=False)

    effectues = relationship("Effectue", back_populates="vehicule")
