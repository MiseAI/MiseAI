from fastapi import FastAPI
from routers.auth import router as auth_router

app = FastAPI(title="MiseAI API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
