from fastapi import FastAPI, Depends, HTTPException, status
from routers import auth, users
from database import Base, engine

app = FastAPI(title="MiseAI API")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
