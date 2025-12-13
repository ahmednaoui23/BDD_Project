from sqlalchemy import Column, Integer, Float, TIMESTAMP, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Trajet(Base):
    __tablename__ = "trajet"

    id_trajet = Column(Integer, primary_key=True, index=True)

    # Id des arrondissements
    id_arrondissement_depart = Column(ForeignKey("arrondissement.id_arrondissement"), nullable=False)
    id_arrondissement_arrivee = Column(ForeignKey("arrondissement.id_arrondissement"), nullable=False)

    # Noms pour affichage / référence
    origine = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)

    economie_co2 = Column(Float, nullable=False)
    duree = Column(Integer, default=30, nullable=False)
    date_depart = Column(TIMESTAMP, nullable=False)
    date_arrivee = Column(TIMESTAMP, nullable=False)

    # Relations avec Arrondissement
    arrondissement_depart = relationship(
        "Arrondissement",
        back_populates="trajets_depart",
        foreign_keys=[id_arrondissement_depart]
    )
    arrondissement_arrivee = relationship(
        "Arrondissement",
        back_populates="trajets_arrivee",
        foreign_keys=[id_arrondissement_arrivee]
    )

    # Relation avec Effectue
    effectues = relationship("Effectue", back_populates="trajet")
