from fastapi import FastAPI
from routes import recipes
app = FastAPI()
app.include_router(recipes.router)