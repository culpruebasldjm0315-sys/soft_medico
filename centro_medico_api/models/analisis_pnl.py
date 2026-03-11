from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class AnalisisPNL(Base):
    __tablename__ = "analisis_pnl"

    id_analisis = Column(Integer, primary_key=True, index=True)
    id_historial = Column(Integer, ForeignKey("historial.id_historial"), nullable=False)
    resumen = Column(Text)
    traduccion = Column(Text)
    entidades = Column(Text)
    sentimientos = Column(Text)
    fecha_analisis = Column(TIMESTAMP, server_default=func.now())

    historial = relationship("Historial", back_populates="analisis")