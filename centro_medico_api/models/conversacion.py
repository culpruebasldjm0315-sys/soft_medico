from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Conversacion(Base):
    __tablename__ = "conversacion"

    id_conversacion = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    fecha_inicio = Column(TIMESTAMP, server_default=func.now())
    fecha_fin = Column(TIMESTAMP, nullable=True)

    usuario = relationship("Usuario", back_populates="conversaciones")
    mensajes = relationship("Mensaje", back_populates="conversacion")
    diagnostico = relationship("Diagnostico", back_populates="conversacion", uselist=False)