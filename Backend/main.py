from fastapi import FastAPI
from routers import auth, users

# ← add these two imports:
from database import Base, engine

app = FastAPI(title="MiseAI API")

# ← and immediately after creating the app, create all tables:
Base.metadata.create_all(bind=engine)

# now mount your routers as before:
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Default"])
def read_root():
    return {"message": "Welcome to MiseAI API"}