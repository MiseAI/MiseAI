from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth

app = FastAPI(title="MiseAI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(debug.router, prefix="/debug", tags=["Debug"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
