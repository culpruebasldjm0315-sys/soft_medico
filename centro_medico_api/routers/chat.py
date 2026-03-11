from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.mensaje import MensajeCreate, MensajeResponse
from schemas.conversacion import ConversacionCreate
from crud.conversacion import create_conversacion, get_conversacion_by_id
from crud.mensaje import create_mensaje
from services.llm import consultar_llm
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    id_usuario: int
    id_conversacion: int | None = None
    mensaje: str

class ChatResponse(BaseModel):
    id_conversacion: int
    mensaje_usuario: MensajeResponse
    respuesta_llm: MensajeResponse

@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    # Si no hay conversación activa, crear una nueva
    if not request.id_conversacion:
        nueva_conv = create_conversacion(db, ConversacionCreate(id_usuario=request.id_usuario))
        id_conversacion = nueva_conv.id_conversacion
    else:
        conv = get_conversacion_by_id(db, request.id_conversacion)
        if not conv:
            raise HTTPException(status_code=404, detail="Conversación no encontrada")
        id_conversacion = request.id_conversacion

    # Guardar mensaje del usuario
    msg_usuario = create_mensaje(db, MensajeCreate(
        id_conversacion=id_conversacion,
        remitente="usuario",
        contenido=request.mensaje
    ))

    # Consultar el LLM
    respuesta = consultar_llm(request.mensaje)

    # Guardar respuesta del LLM
    msg_llm = create_mensaje(db, MensajeCreate(
        id_conversacion=id_conversacion,
        remitente="llm",
        contenido=respuesta
    ))

    return ChatResponse(
        id_conversacion=id_conversacion,
        mensaje_usuario=msg_usuario,
        respuesta_llm=msg_llm
    )