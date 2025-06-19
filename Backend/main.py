from fastapi import FastAPI
from backend.routers import auth, users
from backend.database import Base, engine

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiseAI API")

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
