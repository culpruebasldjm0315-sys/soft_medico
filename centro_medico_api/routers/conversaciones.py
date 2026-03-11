from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.conversacion import ConversacionCreate, ConversacionResponse
from crud.conversacion import create_conversacion, get_conversaciones_by_usuario, cerrar_conversacion

router = APIRouter(prefix="/conversaciones", tags=["Conversaciones"])

@router.post("/", response_model=ConversacionResponse)
def crear_conversacion(conversacion: ConversacionCreate, db: Session = Depends(get_db)):
    return create_conversacion(db, conversacion)

@router.get("/{id_usuario}", response_model=list[ConversacionResponse])
def obtener_conversaciones(id_usuario: int, db: Session = Depends(get_db)):
    conversaciones = get_conversaciones_by_usuario(db, id_usuario)
    if not conversaciones:
        raise HTTPException(status_code=404, detail="No se encontraron conversaciones")
    return conversaciones

@router.put("/{id_conversacion}/cerrar", response_model=ConversacionResponse)
def cerrar(id_conversacion: int, db: Session = Depends(get_db)):
    conv = cerrar_conversacion(db, id_conversacion)
    if not conv:
        raise HTTPException(status_code=404, detail="Conversación no encontrada")
    return conv