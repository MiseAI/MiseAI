# backend/security.py

import os
from datetime import datetime, timedelta
from typing import Generator

from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import User

# ------------------------------------------------------------------------------
# 1) Config & CryptContext
# ------------------------------------------------------------------------------

SECRET_KEY = os.getenv("JWT_SECRET", "change-this")  # override via env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ------------------------------------------------------------------------------
# 2) Password Helpers
# ------------------------------------------------------------------------------

def hash_password(plain: str) -> str:
    return pwd_ctx.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_ctx.verify(plain, hashed)


# ------------------------------------------------------------------------------
# 3) JWT Helpers
# ------------------------------------------------------------------------------

def create_access_token(data: dict) -> str:
    """
    Create a JWT that includes the provided `data` plus an 'exp' claim
    set ACCESS_TOKEN_EXPIRE_MINUTES into the future.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


# ------------------------------------------------------------------------------
# 4) OAuth2 Dependency & Current User
# ------------------------------------------------------------------------------

# This tells FastAPI where the client should send credentials (the token URL).
# It’s the path they POST to get the token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    Dependency you can add to any route to enforce
    authentication and retrieve the current User.
    """
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exc
    except JWTError:
        raise credentials_exc

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exc

    return user
