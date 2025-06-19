# backend/routers/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from backend.database import get_db
from backend.models.user import User
from backend.security import hash_password, verify_password, create_access_token

# ─── Pydantic Schemas ─────────────────────────────────────────────────────────

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

# ─── Router Setup ─────────────────────────────────────────────────────────────

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user account",
)
def register(
    req: RegisterRequest,
    db: Session = Depends(get_db),
):
    # 1) Make sure email isn't already in use
    existing = db.query(User).filter(User.email == req.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # 2) Create & persist
    user = User(
        username=req.username,
        email=req.email,
        hashed_password=hash_password(req.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": f"User {user.email} registered successfully"}


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Authenticate and return a JWT access token",
)
def login(
    req: LoginRequest,
    db: Session = Depends(get_db),
):
    # 1) Lookup user by email
    user = db.query(User).filter(User.email == req.email).first()
    # 2) Verify password
    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3) Issue JWT
    access_token = create_access_token({
        "sub": user.email,
        "user_id": user.id,
    })

    return TokenResponse(access_token=access_token)