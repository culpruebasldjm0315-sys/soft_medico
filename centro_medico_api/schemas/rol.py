from pydantic import BaseModel

class RolBase(BaseModel):
    nombre_rol: str
    descripcion: str | None = None

class RolResponse(RolBase):
    id_rol: int

    class Config:
        from_attributes = True