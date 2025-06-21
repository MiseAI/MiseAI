from fastapi import FastAPI, Depends, HTTPException, status
from database import Base, engine, get_db
from routers import auth, users

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiseAI API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
