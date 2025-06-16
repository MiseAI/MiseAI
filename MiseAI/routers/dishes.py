from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import dish as models
from schemas import dish as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Dish)
def create_dish(dish: schemas.DishCreate, db: Session = Depends(get_db)):
    db_dish = models.Dish(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

@router.get("/", response_model=list[schemas.Dish])
def read_dishes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Dish).offset(skip).limit(limit).all()
