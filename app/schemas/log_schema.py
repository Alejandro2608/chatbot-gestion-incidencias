from pydantic import BaseModel
from datetime import datetime

# Para crear un registro de chat
class LogChatCreate(BaseModel):
    user_id: int
    pregunta: str
    respuesta: str | None = None

# Para mostrar un log de chat
class LogChatOut(BaseModel):
    id: int
    user_id: int
    pregunta: str
    respuesta: str | None = None
    timestamp: datetime

    class Config:
        orm_mode = True
