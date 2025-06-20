from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from security import get_current_user
from models.user import User as UserModel

router = APIRouter()

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
    )
