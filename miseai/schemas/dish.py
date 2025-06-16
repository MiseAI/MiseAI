from pydantic import BaseModel

class DishBase(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    category: str | None = None

class DishCreate(DishBase):
    pass

class Dish(DishBase):
    id: int

    class Config:
        orm_mode = True
