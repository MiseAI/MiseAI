from fastapi import FastAPI
from database import Base, engine
from routers import auth

app = FastAPI(title="MiseAI API")

# ← ensure this runs before any request
@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
