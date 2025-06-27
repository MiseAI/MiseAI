
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer

from database import get_db
from models.user import User
from security import SECRET_KEY, ALGORITHM
from routers.auth import TokenResponse

router = APIRouter(prefix="/users", tags=["Users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if not email:
            raise credentials_exception
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception
