from fastapi import FastAPI
from routes import auth
from database import engine, Base
from routes import history

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(history.router, prefix="/api")
