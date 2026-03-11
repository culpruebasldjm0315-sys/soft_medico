from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.usuario import LoginRequest, UsuarioResponse
from crud.usuario import get_usuario_by_email, verify_password

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/login", response_model=UsuarioResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    usuario = get_usuario_by_email(db, request.email)
    if not usuario or not verify_password(request.contrasena, usuario.contrasena):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    if not usuario.activo:
        raise HTTPException(status_code=403, detail="Usuario inactivo")
    return usuario