from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Mensaje(Base):
    __tablename__ = "mensaje"

    id_mensaje = Column(Integer, primary_key=True, index=True)
    id_conversacion = Column(Integer, ForeignKey("conversacion.id_conversacion"), nullable=False)
    remitente = Column(String(10), nullable=False)  # 'usuario' o 'llm'
    contenido = Column(Text, nullable=False)
    fecha_hora = Column(TIMESTAMP, server_default=func.now())

    conversacion = relationship("Conversacion", back_populates="mensajes")