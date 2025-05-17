from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.response_logic import obtener_respuesta
from app.utils.email import enviar_ticket_por_correo
from app.database import SessionLocal
from app.models.pregunta_no_resuelta import PreguntaNoResuelta


router = APIRouter()

class PreguntaEntrada(BaseModel):
    pregunta: str
    correo_usuario: str = "anonimo@chatbot.com"

@router.post("/chat")
def responder_pregunta(pregunta_entrada: PreguntaEntrada):
    pregunta = pregunta_entrada.pregunta
    correo_usuario = pregunta_entrada.correo_usuario
    respuesta = obtener_respuesta(pregunta)

    if respuesta:
        return {"respuesta": respuesta}

    # Enviar correo al soporte simulando el ticket
    enviado = enviar_ticket_por_correo(pregunta, correo_usuario)

    # Guardar la pregunta en la base de datos
    try:
        db = SessionLocal()
        pregunta_db = PreguntaNoResuelta(pregunta=pregunta)
        db.add(pregunta_db)
        db.commit()
        db.close()
    except Exception as e:
        print(f"⚠️ Error guardando pregunta no resuelta: {e}")

    if enviado:
        raise HTTPException(status_code=404, detail="No se encontró una respuesta. La pregunta ha sido enviada a soporte.")
    else:
        raise HTTPException(status_code=500, detail="No se encontró respuesta y falló el intento de escalar a soporte.")
