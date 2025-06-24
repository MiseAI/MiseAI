from fastapi import FastAPI
from routes import menu

app = FastAPI()

app.include_router(menu.router)