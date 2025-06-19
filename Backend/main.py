# main.py
from fastapi import FastAPI
from routers import auth, users

app = FastAPI(title="MiseAI API")

# mount the auth router at /auth
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# mount your users router at /users
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}