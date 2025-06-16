from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from database import get_db
from models import sales as models
from models import dish as dish_models
from datetime import date, timedelta

router = APIRouter()

@router.get("/", summary="Forecast next week's daily sales by dish")
def forecast_sales(db: Session = Depends(get_db)):
    # Step 1: Group by dish_id and weekday (0=Mon, 6=Sun)
    sales_by_dish_day = (
        db.query(
            models.Sale.dish_id,
            extract("dow", models.Sale.date).label("weekday"),
            func.avg(models.Sale.quantity_sold).label("avg_quantity")
        )
        .group_by(models.Sale.dish_id, "weekday")
        .all()
    )

    # Step 2: Build forecast per weekday
    forecast = {d.name: {} for d in db.query(dish_models.Dish).all()}
    for record in sales_by_dish_day:
        dish = db.query(dish_models.Dish).filter(dish_models.Dish.id == record.dish_id).first()
        if dish:
            weekday_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][int(record.weekday)]
            forecast[dish.name][weekday_name] = round(record.avg_quantity)

    return forecast
