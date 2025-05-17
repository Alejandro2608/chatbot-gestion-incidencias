from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database import Base

class PreguntaNoResuelta(Base):
    __tablename__ = "preguntas_no_resueltas"

    id = Column(Integer, primary_key=True, index=True)
    pregunta = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

