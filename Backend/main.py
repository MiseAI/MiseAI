from fastapi import FastAPI
from backend.routers import auth, user

app = FastAPI(title="MiseAI API")

app.include_router(auth.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
