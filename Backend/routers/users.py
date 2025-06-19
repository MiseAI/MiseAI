from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.user import User

router = APIRouter()

@router.get("/users/me", response_model=dict)
def read_users_me(db: Session = Depends(get_db)):
    # placeholder, needs auth dependency
    return {"user": "me"}
