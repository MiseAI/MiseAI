from pydantic import BaseModel

class IngredientBase(BaseModel):
    name: str
    unit: str
    latest_price: float | None = None

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True
