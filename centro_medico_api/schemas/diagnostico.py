from pydantic import BaseModel
from datetime import datetime

class DiagnosticoCreate(BaseModel):
    id_conversacion: int
    contenido_diagnostico: str

class DiagnosticoResponse(BaseModel):
    id_diagnostico: int
    id_conversacion: int
    contenido_diagnostico: str
    fecha_generado: datetime

    class Config:
        from_attributes = True