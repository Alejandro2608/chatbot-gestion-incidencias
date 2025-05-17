from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(String, default="pendiente")
    fecha = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="tickets")
