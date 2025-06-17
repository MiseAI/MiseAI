from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import dish as models, restaurant as restaurant_models
from schemas import dish as schemas
from routers.auth import get_current_user
from models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Dish)
def create_dish(dish: schemas.DishCreate, restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    restaurant = db.query(restaurant_models.Restaurant).filter_by(id=restaurant_id, owner_id=current_user.id).first()
    if not restaurant:
        raise HTTPException(status_code=403, detail="Unauthorized restaurant")
    db_dish = models.Dish(**dish.dict(), user_id=current_user.id, restaurant_id=restaurant_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

@router.get("/", response_model=list[schemas.Dish])
def read_dishes(restaurant_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(models.Dish).filter(models.Dish.user_id == current_user.id, models.Dish.restaurant_id == restaurant_id).all()
