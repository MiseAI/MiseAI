from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import recipe as models, restaurant as restaurant_models
from schemas import recipe as schemas
from backend.routers.auth import get_current_user
from backend.models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    restaurant = db.query(restaurant_models.Restaurant).filter_by(id=restaurant_id, owner_id=current_user.id).first()
    if not restaurant:
        raise HTTPException(status_code=403, detail="Unauthorized restaurant")
    db_recipe = models.Recipe(**recipe.dict(), user_id=current_user.id, restaurant_id=restaurant_id)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@router.get("/", response_model=list[schemas.Recipe])
def read_recipes(restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(models.Recipe).filter(models.Recipe.user_id == current_user.id, models.Recipe.restaurant_id == restaurant_id).all()
