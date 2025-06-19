from fastapi import FastAPI
from routers import auth, users  # make sure “users” is imported

app = FastAPI(title="MiseAI API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])  # this line

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
