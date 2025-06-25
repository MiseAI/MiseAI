from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Recipe(BaseModel):
    name: str
    ingredients: List[str]
    cost: float

recipes_db = []

@router.post("/recipe", response_model=Recipe)
def add_recipe(recipe: Recipe):
    recipes_db.append(recipe)
    return recipe