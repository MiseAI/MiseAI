from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from jose import JWTError, jwt

from database import get_db
from models.user import User
from security import SECRET_KEY, ALGORITHM
from routers.auth import TokenResponse

router = APIRouter(prefix="/users", tags=["Users"])

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

def get_current_user(token: str = Depends(lambda: None), db: Session = Depends(get_db)):
    # replace lambda with actual OAuth2 dependency if needed
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
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise credentials_exception
    return user

@router.get("/me", response_model=UserResponse)
def read_users_me(current: User = Depends(get_current_user)):
    return current
