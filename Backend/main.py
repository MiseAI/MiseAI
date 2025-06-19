from fastapi import FastAPI
from routers import auth, users

app = FastAPI(title="MiseAI API")

# mount the routers with their prefixes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}