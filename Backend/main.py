from fastapi import FastAPI
from routers.auth import router as auth_router
from database import Base, engine
from sqlalchemy.orm import sessionmaker

# Create database tables on startup
app = FastAPI(title="MiseAI API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
