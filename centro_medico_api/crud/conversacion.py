from sqlalchemy.orm import Session
from models.conversacion import Conversacion
from schemas.conversacion import ConversacionCreate
from datetime import datetime

def create_conversacion(db: Session, conversacion: ConversacionCreate):
    db_conv = Conversacion(**conversacion.model_dump())
    db.add(db_conv)
    db.commit()
    db.refresh(db_conv)
    return db_conv

def get_conversaciones_by_usuario(db: Session, id_usuario: int):
    return db.query(Conversacion).filter(Conversacion.id_usuario == id_usuario).all()

def get_conversacion_by_id(db: Session, id_conversacion: int):
    return db.query(Conversacion).filter(Conversacion.id_conversacion == id_conversacion).first()

def cerrar_conversacion(db: Session, id_conversacion: int):
    conv = get_conversacion_by_id(db, id_conversacion)
    if not conv:
        return None
    conv.fecha_fin = datetime.now()
    db.commit()
    db.refresh(conv)
    return conv