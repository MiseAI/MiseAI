from fastapi import FastAPI
from routers import auth, debug  # ⬅️ Import the debug router

app = FastAPI(title="MiseAI API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(debug.router, prefix="/auth/debug", tags=["Debug"])  # ⬅️ Add this line

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}