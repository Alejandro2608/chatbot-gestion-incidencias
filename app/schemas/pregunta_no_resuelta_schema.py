from pydantic import BaseModel
from datetime import datetime

# Para guardar una pregunta sin respuesta
class PreguntaNoResueltaCreate(BaseModel):
    pregunta: str

# Para mostrar preguntas no resueltas
class PreguntaNoResueltaOut(BaseModel):
    id: int
    pregunta: str
    timestamp: datetime

    class Config:
        from_attributes = True
