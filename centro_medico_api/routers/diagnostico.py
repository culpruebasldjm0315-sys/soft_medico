from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.diagnostico import DiagnosticoCreate, DiagnosticoResponse
from crud.diagnostico import create_diagnostico, get_diagnostico_by_conversacion

router = APIRouter(prefix="/diagnostico", tags=["Diagnóstico"])

@router.post("/", response_model=DiagnosticoResponse)
def crear_diagnostico(diagnostico: DiagnosticoCreate, db: Session = Depends(get_db)):
    existente = get_diagnostico_by_conversacion(db, diagnostico.id_conversacion)
    if existente:
        raise HTTPException(status_code=400, detail="Ya existe un diagnóstico para esta conversación")
    return create_diagnostico(db, diagnostico)

@router.get("/{id_conversacion}", response_model=DiagnosticoResponse)
def obtener_diagnostico(id_conversacion: int, db: Session = Depends(get_db)):
    diagnostico = get_diagnostico_by_conversacion(db, id_conversacion)
    if not diagnostico:
        raise HTTPException(status_code=404, detail="Diagnóstico no encontrado")
    return diagnostico