from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Historial(Base):
    __tablename__ = "historial"

    id_historial = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())

    usuario = relationship("Usuario", back_populates="historiales")
    analisis = relationship("AnalisisPNL", back_populates="historial")