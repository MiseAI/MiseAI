# main.py
from fastapi import FastAPI
from routers import auth, users

app = FastAPI(title="MiseAI API")

# ⚠️ Be explicit about the path prefix here
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}