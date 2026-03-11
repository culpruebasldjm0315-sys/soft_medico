from pydantic import BaseModel
from datetime import datetime

class AnalisisPNLCreate(BaseModel):
    id_historial: int
    resumen: str | None = None
    traduccion: str | None = None
    entidades: str | None = None
    sentimientos: str | None = None

class AnalisisPNLResponse(BaseModel):
    id_analisis: int
    id_historial: int
    resumen: str | None = None
    traduccion: str | None = None
    entidades: str | None = None
    sentimientos: str | None = None
    fecha_analisis: datetime

    class Config:
        from_attributes = True