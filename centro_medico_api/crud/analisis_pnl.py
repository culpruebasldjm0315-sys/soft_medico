from sqlalchemy.orm import Session
from models.analisis_pnl import AnalisisPNL
from schemas.analisis_pnl import AnalisisPNLCreate

def create_analisis(db: Session, analisis: AnalisisPNLCreate):
    db_analisis = AnalisisPNL(**analisis.model_dump())
    db.add(db_analisis)
    db.commit()
    db.refresh(db_analisis)
    return db_analisis

def get_analisis_by_historial(db: Session, id_historial: int):
    return db.query(AnalisisPNL).filter(AnalisisPNL.id_historial == id_historial).first()

def get_analisis_by_usuario(db: Session, id_usuario: int):
    return db.query(AnalisisPNL).join(AnalisisPNL.historial).filter_by(id_usuario=id_usuario).all()