from fastapi import FastAPI
from app.db.database import engine
from app.models import menu, recipe, invoice  # example import

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MiseAI backend is live!"}
