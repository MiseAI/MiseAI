from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    dish_id: int
    date: date
    quantity_sold: int

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True
