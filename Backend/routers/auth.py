from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from database import get_db
from models.user import User
from security import (
    hash_password,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

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



router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    # 1) check if email already exists
    if db.query(User).filter(User.email == req.email).first():
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    # 2) create & save user
    new_user = User(
        username=req.username,
        email=req.email,
        hashed_password=hash_password(req.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": f"User {new_user.email} registered successfully"}


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Authenticate and receive a JWT access token",
)
def login(req: LoginRequest, db: Session = Depends(get_db)):
    # 1) find user by email
    user = db.query(User).filter(User.email == req.email).first()
    # 2) verify password
    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # 3) create a JWT that expires in ACCESS_TOKEN_EXPIRE_MINUTES
    token = create_access_token(
        data={"sub": user.email, "user_id": user.id},
        # create_access_token already applies the expiration
    )
    # 4) return in the shape FastAPI expects (by our TokenResponse)
    return {"access_token": token, "token_type": "bearer"}