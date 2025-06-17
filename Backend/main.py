
from fastapi import FastAPI
from routers import auth, debug

app = FastAPI(title="MiseAI API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(debug.router, prefix="/debug", tags=["Debug"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
