from fastapi import FastAPI
from routes.assistant import router as assistant_router

app = FastAPI()
app.include_router(assistant_router, prefix="/api/ai-assistant")