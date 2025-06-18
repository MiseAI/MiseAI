from fastapi import FastAPI
from backend.database import Base, engine
from backend.routers import auth

app = FastAPI(title="MiseAI API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
