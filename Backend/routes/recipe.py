from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RecipeIn(BaseModel):
    name: str
    ingredients: dict

@router.post("/cost")
async def cost_recipe(r: RecipeIn):
    return {"name": r.name, "cost": 0.0, "suggestedPrice": 0.0}
