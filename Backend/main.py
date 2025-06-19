# main.py

from fastapi import FastAPI
from sqlalchemy.orm import Session
from backend.database import Base, engine, get_db
from backend.routers import auth, users

# — Create all tables at startup (so you don’t get “no such table” errors) —
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiseAI API")

# — Auth routes (/auth/register, /auth/login) —
app.include_router(auth.router)

# — User routes (/users/me, etc.) —
app.include_router(users.router)

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}