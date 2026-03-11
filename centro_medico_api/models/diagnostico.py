from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Diagnostico(Base):
    __tablename__ = "diagnostico"

    id_diagnostico = Column(Integer, primary_key=True, index=True)
    id_conversacion = Column(Integer, ForeignKey("conversacion.id_conversacion"), nullable=False, unique=True)
    contenido_diagnostico = Column(Text, nullable=False)
    fecha_generado = Column(TIMESTAMP, server_default=func.now())

    conversacion = relationship("Conversacion", back_populates="diagnostico")