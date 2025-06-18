from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .auth import get_current_user  # your JWT-based dependency
from backend.database import SessionLocal
from backend.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", dependencies=[Depends(get_current_user)])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "email": u.email} for u in users]