from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.historial import HistorialCreate, HistorialResponse
from crud.historial import create_historial, get_historiales_by_usuario

router = APIRouter(prefix="/historial", tags=["Historial"])

@router.post("/", response_model=HistorialResponse)
def crear_historial(historial: HistorialCreate, db: Session = Depends(get_db)):
    return create_historial(db, historial)

@router.get("/{id_usuario}", response_model=list[HistorialResponse])
def obtener_historial(id_usuario: int, db: Session = Depends(get_db)):
    historiales = get_historiales_by_usuario(db, id_usuario)
    if not historiales:
        raise HTTPException(status_code=404, detail="No se encontraron historiales")
    return historiales