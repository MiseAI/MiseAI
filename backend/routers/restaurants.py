from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.restaurant import Restaurant
from schemas import restaurant as schemas
from backend.routers.auth import get_current_user
from backend.models.user import User

router = APIRouter()

@router.post("/", response_model=schemas.Restaurant)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_restaurant = Restaurant(name=restaurant.name, owner_id=current_user.id)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

@router.get("/", response_model=list[schemas.Restaurant])
def get_my_restaurants(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Restaurant).filter(Restaurant.owner_id == current_user.id).all()
