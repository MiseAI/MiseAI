from fastapi import FastAPI
from routes import auth
from database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
