from fastapi import FastAPI
from backend.routers.auth import router as auth_router
from backend.routers.users import router as users_router

app = FastAPI(title="MiseAI API")

app.include_router(auth_router)
app.include_router(users_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
