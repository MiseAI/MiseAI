import os
from datetime import datetime, timedelta

import jwt  # PyJWT
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database import SessionLocal, engine, Base
from models.user import User

# Create tables at startup
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/auth", tags=["Auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter((User.email == req.email) | (User.username == req.username)).first():
        raise HTTPException(400, "Email or username already registered")
    user = User(
        username=req.username,
        email=req.email,
        hashed_password=hash_password(req.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": f"User {user.email} registered successfully"}

@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == req.email).first()
    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token({"sub": user.email, "user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}