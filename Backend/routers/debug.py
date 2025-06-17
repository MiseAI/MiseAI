
from fastapi import APIRouter
from database import SessionLocal
from models.user import User

router = APIRouter()

@router.get("/users")
def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    return [{"id": u.id, "email": u.email, "username": u.username} for u in users]
