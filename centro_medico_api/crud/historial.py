from sqlalchemy.orm import Session
from models.historial import Historial
from schemas.historial import HistorialCreate

def create_historial(db: Session, historial: HistorialCreate):
    db_historial = Historial(**historial.model_dump())
    db.add(db_historial)
    db.commit()
    db.refresh(db_historial)
    return db_historial

def get_historiales_by_usuario(db: Session, id_usuario: int):
    return db.query(Historial).filter(Historial.id_usuario == id_usuario).all()

def get_historial_by_id(db: Session, id_historial: int):
    return db.query(Historial).filter(Historial.id_historial == id_historial).first()