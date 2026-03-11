from pydantic import BaseModel
from datetime import datetime

class HistorialCreate(BaseModel):
    id_usuario: int
    descripcion: str

class HistorialResponse(BaseModel):
    id_historial: int
    id_usuario: int
    descripcion: str
    fecha_registro: datetime

    class Config:
        from_attributes = True