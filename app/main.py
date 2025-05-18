from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.models import user, log_chat, pregunta_no_resuelta, ticket
from app.endpoints import chatbot
from app.endpoints import auth



app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar "*" por el dominio del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(chatbot.router)
app.include_router(auth.router)
