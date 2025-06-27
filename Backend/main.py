from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth
from database import engine, Base
from routes import history
from routes import chat

app = FastAPI()

origins = [
    "https://frontend-production-f46d.up.railway.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(history.router, prefix="/api")
app.include_router(chat.router, prefix="/api")