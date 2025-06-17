from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import SessionLocal
from models.user import User
from sqlalchemy.exc import IntegrityError

router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: RegisterRequest):
    db = SessionLocal()
    new_user = User(email=user.email, username=user.username, password=user.password)
    try:
        db.add(new_user)
        db.commit()
        return {"message": f"User {user.email} registered successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    finally:
        db.close()

@router.post("/login")
def login(credentials: LoginRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.email == credentials.email).first()
    db.close()
    if user and user.password == credentials.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
