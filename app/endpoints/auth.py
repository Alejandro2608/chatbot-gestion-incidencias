from fastapi import APIRouter, HTTPException
from pydantic import EmailStr
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserOut
from passlib.context import CryptContext
from app.schemas.user_schema import UserLogin

router = APIRouter()

# Configuración de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@router.post("/register", response_model=UserOut)
def register(user: UserCreate):
    db = SessionLocal()

    # Verificar si ya existe el usuario
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="El usuario ya existe.")

    # Crear nuevo usuario
    hashed_password = get_password_hash(user.password)
    nuevo_usuario = User(
        email=user.email,
        nombre=user.nombre,
        password=hashed_password
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    db.close()

    return nuevo_usuario

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    usuario = db.query(User).filter(User.email == user.email).first()

    if not usuario or not verify_password(user.password, usuario.password):
        db.close()
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    db.close()
    return {"message": "Inicio de sesión exitoso", "usuario": usuario.email}
