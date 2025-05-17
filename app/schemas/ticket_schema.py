from pydantic import BaseModel
from datetime import datetime

# Esquema para crear un ticket (entrada desde el frontend)
class TicketCreate(BaseModel):
    user_id: int
    titulo: str
    descripcion: str

# Esquema para mostrar el ticket (salida al frontend)
class TicketOut(BaseModel):
    id: int
    user_id: int
    titulo: str
    descripcion: str
    estado: str
    fecha: datetime

    class Config:
        orm_mode = True
