from pydantic import BaseModel

class RecipeBase(BaseModel):
    dish_id: int
    ingredient_id: int
    quantity: float

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
