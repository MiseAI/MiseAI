from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth
from routes import history
from routes import chat
from routes import invoice
from database import engine, Base
import os

app = FastAPI()

origins = [
    "https://frontend-production-f46d.up.railway.app",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(history.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(invoice.router, prefix="/api")
app.include_router(invoice.router, prefix="/api/invoice")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
