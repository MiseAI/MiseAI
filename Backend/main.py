from fastapi import FastAPI
from routers import auth

app = FastAPI(title="MiseAI API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
