from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from backend.security import get_current_user
from backend.models.user import User as UserModel

router = APIRouter(tags=["Users"])

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

@router.get("/users/me", response_model=UserResponse)
def read_current_user(current: UserModel = Depends(get_current_user)):
    return current
