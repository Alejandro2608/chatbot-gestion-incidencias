from pydantic import BaseModel, EmailStr

# Para crear un nuevo usuario
class UserCreate(BaseModel):
    email: EmailStr
    nombre: str
    password: str

# Para mostrar info del usuario (sin contraseña)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    nombre: str

    class Config:
        orm_mode = True
