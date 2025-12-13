from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class ConsultationCitoyenne(Base):
    __tablename__ = "consultation_citoyenne"

    id_consultation = Column(Integer, primary_key=True, index=True)
    date_consultation = Column(TIMESTAMP, nullable=False)
    titre = Column(String(255), nullable=False)
    id_arrondissement = Column(ForeignKey("arrondissement.id_arrondissement"))

    arrondissement = relationship("Arrondissement", back_populates="consultations")
    participations = relationship("Participation", back_populates="consultation")
