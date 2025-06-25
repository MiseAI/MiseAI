from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class MenuItem(BaseModel):
    name: str
    price: float
    category: str

menu_db = []

@router.post("/menu", response_model=MenuItem)
def add_menu_item(item: MenuItem):
    menu_db.append(item)
    return item

@router.get("/menu", response_model=List[MenuItem])
def get_menu():
    return menu_db