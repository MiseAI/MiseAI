from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import recipe as recipe_models, dish as dish_models, ingredient as ingredient_models

router = APIRouter()

@router.get("/recipes/{dish_id}/cost")
def get_recipe_cost(dish_id: int, db: Session = Depends(get_db)):
    recipe_items = db.query(recipe_models.Recipe).filter(recipe_models.Recipe.dish_id == dish_id).all()
    dish = db.query(dish_models.Dish).filter(dish_models.Dish.id == dish_id).first()
    if not dish:
        return {"error": "Dish not found"}

    total_cost = 0
    cost_breakdown = []
    for item in recipe_items:
        ingredient = db.query(ingredient_models.Ingredient).filter(ingredient_models.Ingredient.id == item.ingredient_id).first()
        if ingredient and ingredient.latest_price is not None:
            item_cost = item.quantity * ingredient.latest_price
            total_cost += item_cost
            cost_breakdown.append({
                "ingredient": ingredient.name,
                "quantity": item.quantity,
                "unit_cost": ingredient.latest_price,
                "cost": round(item_cost, 2)
            })

    margin = None
    if dish.price is not None:
        margin = round(dish.price - total_cost, 2)

    return {
        "dish": dish.name,
        "total_cost": round(total_cost, 2),
        "menu_price": dish.price,
        "margin": margin,
        "breakdown": cost_breakdown
    }

@router.get("/recipes/profitability")
def get_all_dish_margins(db: Session = Depends(get_db)):
    results = []
    dishes = db.query(dish_models.Dish).all()
    for dish in dishes:
        recipe_items = db.query(recipe_models.Recipe).filter(recipe_models.Recipe.dish_id == dish.id).all()
        total_cost = 0
        for item in recipe_items:
            ingredient = db.query(ingredient_models.Ingredient).filter(ingredient_models.Ingredient.id == item.ingredient_id).first()
            if ingredient and ingredient.latest_price is not None:
                total_cost += item.quantity * ingredient.latest_price
        if dish.price is not None:
            margin = round(dish.price - total_cost, 2)
            results.append({
                "dish": dish.name,
                "price": dish.price,
                "cost": round(total_cost, 2),
                "margin": margin
            })

    sorted_results = sorted(results, key=lambda x: x["margin"])
    return sorted_results
