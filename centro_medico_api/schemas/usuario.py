from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioCreate(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    contrasena: str
    id_rol: int

class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str
    apellido: str
    email: str
    id_rol: int
    activo: bool
    fecha_registro: datetime

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    contrasena: str