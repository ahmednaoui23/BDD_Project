from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .database import Base
import uuid

class Capteur(Base):
    __tablename__ = "capteur"

    id_capteur = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type_capteur = Column(String(50), nullable=False)
    statut = Column(String(50), nullable=False)
    date_installation = Column(Date, nullable=False)
    id_proprietaire = Column(ForeignKey("proprietaire.id_proprietaire"))
    id_arrondissement = Column(ForeignKey("arrondissement.id_arrondissement"))

    proprietaire = relationship("Proprietaire", back_populates="capteurs")
    arrondissement = relationship("Arrondissement", back_populates="capteurs")
    mesures = relationship("Mesure", back_populates="capteur")
    interventions = relationship("Intervention", back_populates="capteur")
