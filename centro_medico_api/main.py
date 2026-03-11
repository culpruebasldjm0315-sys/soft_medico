from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
from routers import auth, usuarios, historial, conversaciones, mensajes, diagnostico, pnl, chat

# Crear tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Centro Médico API",
    description="API REST para el sistema de Centro Médico con IA",
    version="1.0.0"
)

# CORS para permitir conexión desde el aplicativo Java
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(usuarios.router)
app.include_router(historial.router)
app.include_router(conversaciones.router)
app.include_router(mensajes.router)
app.include_router(diagnostico.router)
app.include_router(pnl.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Centro Médico API funcionando correctamente ✅"}