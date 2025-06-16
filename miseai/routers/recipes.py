from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import recipe as models
from schemas import recipe as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@router.get("/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Recipe).offset(skip).limit(limit).all()
