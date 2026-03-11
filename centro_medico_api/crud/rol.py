from sqlalchemy.orm import Session
from models.rol import Rol

def get_roles(db: Session):
    return db.query(Rol).all()

def get_rol_by_id(db: Session, id_rol: int):
    return db.query(Rol).filter(Rol.id_rol == id_rol).first()