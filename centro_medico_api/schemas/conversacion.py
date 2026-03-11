from pydantic import BaseModel
from datetime import datetime

class ConversacionCreate(BaseModel):
    id_usuario: int

class ConversacionResponse(BaseModel):
    id_conversacion: int
    id_usuario: int
    fecha_inicio: datetime
    fecha_fin: datetime | None = None

    class Config:
        from_attributes = True