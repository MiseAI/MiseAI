from fastapi import APIRouter

router = APIRouter()

@router.get("/recipes")
async def get_recipes():
    return {"message": "Recipe endpoint active"}
