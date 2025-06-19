from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.models.user import User
from backend.routers.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

@router.get("/me", response_model=UserResponse, summary="Get current logged-in user")
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user
