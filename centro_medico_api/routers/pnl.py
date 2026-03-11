from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.analisis_pnl import AnalisisPNLCreate, AnalisisPNLResponse
from crud.analisis_pnl import create_analisis, get_analisis_by_historial, get_analisis_by_usuario

router = APIRouter(prefix="/pnl", tags=["Análisis PNL"])

@router.post("/", response_model=AnalisisPNLResponse)
def crear_analisis(analisis: AnalisisPNLCreate, db: Session = Depends(get_db)):
    return create_analisis(db, analisis)

@router.get("/historial/{id_historial}", response_model=AnalisisPNLResponse)
def obtener_por_historial(id_historial: int, db: Session = Depends(get_db)):
    analisis = get_analisis_by_historial(db, id_historial)
    if not analisis:
        raise HTTPException(status_code=404, detail="Análisis no encontrado")
    return analisis

@router.get("/usuario/{id_usuario}", response_model=list[AnalisisPNLResponse])
def obtener_por_usuario(id_usuario: int, db: Session = Depends(get_db)):
    analisis = get_analisis_by_usuario(db, id_usuario)
    if not analisis:
        raise HTTPException(status_code=404, detail="No se encontraron análisis")
    return analisis