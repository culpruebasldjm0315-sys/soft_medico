from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.mensaje import MensajeCreate, MensajeResponse
from crud.mensaje import create_mensaje, get_mensajes_by_conversacion

router = APIRouter(prefix="/mensajes", tags=["Mensajes"])

@router.post("/", response_model=MensajeResponse)
def crear_mensaje(mensaje: MensajeCreate, db: Session = Depends(get_db)):
    return create_mensaje(db, mensaje)

@router.get("/{id_conversacion}", response_model=list[MensajeResponse])
def obtener_mensajes(id_conversacion: int, db: Session = Depends(get_db)):
    mensajes = get_mensajes_by_conversacion(db, id_conversacion)
    if not mensajes:
        raise HTTPException(status_code=404, detail="No se encontraron mensajes")
    return mensajes