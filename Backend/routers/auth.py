
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import SessionLocal
from models.user import User
from sqlalchemy.exc import IntegrityError

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(user: UserCreate):
    db = SessionLocal()
    new_user = User(username=user.username, email=user.email, password=user.password)
    try:
        db.add(new_user)
        db.commit()
        return {"message": f"User {user.email} registered successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User already exists")

@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()
    db_user = db.query(User).filter_by(email=user.email, password=user.password).first()
    if db_user:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
