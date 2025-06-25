from fastapi import APIRouter

router = APIRouter()

@router.get("/menu")
def get_menu():
    return {"message": "menu works!"}
