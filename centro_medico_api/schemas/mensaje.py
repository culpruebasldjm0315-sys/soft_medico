from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class MensajeCreate(BaseModel):
    id_conversacion: int
    remitente: Literal["usuario", "llm"]
    contenido: str

class MensajeResponse(BaseModel):
    id_mensaje: int
    id_conversacion: int
    remitente: str
    contenido: str
    fecha_hora: datetime

    class Config:
        from_attributes = True