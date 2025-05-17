from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    password = Column(String, nullable=False)

    logs_chat = relationship("LogChat", back_populates="user")

    tickets = relationship("Ticket", back_populates="user")

