from sqlalchemy.orm import Session
from models.diagnostico import Diagnostico
from schemas.diagnostico import DiagnosticoCreate

def create_diagnostico(db: Session, diagnostico: DiagnosticoCreate):
    db_diag = Diagnostico(**diagnostico.model_dump())
    db.add(db_diag)
    db.commit()
    db.refresh(db_diag)
    return db_diag

def get_diagnostico_by_conversacion(db: Session, id_conversacion: int):
    return db.query(Diagnostico).filter(Diagnostico.id_conversacion == id_conversacion).first()