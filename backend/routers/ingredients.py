from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import ingredient as models, restaurant as restaurant_models
from schemas import ingredient as schemas
from backend.routers.auth import get_current_user
from backend.models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Ingredient)
def create_ingredient(ingredient: schemas.IngredientCreate, restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    restaurant = db.query(restaurant_models.Restaurant).filter_by(id=restaurant_id, owner_id=current_user.id).first()
    if not restaurant:
        raise HTTPException(status_code=403, detail="Unauthorized restaurant")

    db_ingredient = models.Ingredient(**ingredient.dict(), user_id=current_user.id, restaurant_id=restaurant_id)
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

@router.get("/", response_model=list[schemas.Ingredient])
def read_ingredients(restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(models.Ingredient).filter(models.Ingredient.user_id == current_user.id, models.Ingredient.restaurant_id == restaurant_id).all()
