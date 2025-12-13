from sqlalchemy import Column, Integer, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .database import Base

class Participation(Base):
    __tablename__ = "participation"

    id_citoyen = Column(ForeignKey("citoyen.id_citoyen"), primary_key=True)
    id_consultation = Column(ForeignKey("consultation_citoyenne.id_consultation"), primary_key=True)
    date_participation = Column(Date, nullable=False)
    avis = Column(Text)

    citoyen = relationship("Citoyen", back_populates="participations")
    consultation = relationship("ConsultationCitoyenne", back_populates="participations")
