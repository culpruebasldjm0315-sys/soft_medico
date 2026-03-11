from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.usuario import UsuarioCreate, UsuarioResponse
from crud.usuario import create_usuario, get_usuarios, get_usuario_by_id, update_usuario, get_usuario_by_email

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    existente = get_usuario_by_email(db, usuario.email)
    if existente:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return create_usuario(db, usuario)

@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

@router.get("/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = get_usuario_by_id(db, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{id_usuario}", response_model=UsuarioResponse)
def actualizar_usuario(id_usuario: int, datos: dict, db: Session = Depends(get_db)):
    usuario = update_usuario(db, id_usuario, datos)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario