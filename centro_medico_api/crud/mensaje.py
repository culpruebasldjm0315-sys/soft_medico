from sqlalchemy.orm import Session
from models.mensaje import Mensaje
from schemas.mensaje import MensajeCreate

def create_mensaje(db: Session, mensaje: MensajeCreate):
    db_mensaje = Mensaje(**mensaje.model_dump())
    db.add(db_mensaje)
    db.commit()
    db.refresh(db_mensaje)
    return db_mensaje

def get_mensajes_by_conversacion(db: Session, id_conversacion: int):
    return db.query(Mensaje).filter(Mensaje.id_conversacion == id_conversacion).all()