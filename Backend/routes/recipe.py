from fastapi import APIRouter

router = APIRouter()

@router.get("/recipe")
def get_recipe():
    return {"message": "recipe works!"}
