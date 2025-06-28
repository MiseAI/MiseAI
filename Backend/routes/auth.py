from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import SessionLocal
from models.user import User
from schemas.auth import UserCreate, UserLogin, Token
from core.security import hash_password, verify_password, create_access_token

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/register")
async def register(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if user exists
    result = await db.execute(
        User.__table__.select().where(User.email == user_data.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")

    new_user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )
    db.add(new_user)
    await db.commit()

    return {"message": "User registered successfully."}
