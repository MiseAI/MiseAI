from fastapi import FastAPI
from routers import auth, users

app = FastAPI(title="MiseAI API")

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
