from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AIQuery(BaseModel):
    query: str

@router.post("/ai/query")
def ask_ai(query: AIQuery):
    return {"response": f"Simulated response to: {query.query}"}