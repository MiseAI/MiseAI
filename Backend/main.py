# backend/main.py

from fastapi import FastAPI
from database import Base, engine
from routers import auth, ingredients, dishes, recipes, sales, forecast

app = FastAPI(title="MiseAI API")

@app.on_event("startup")
def on_startup():
    """
    Create all database tables if they don't already exist.
    """
    Base.metadata.create_all(bind=engine)


# Authentication endpoints
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Core feature endpoints
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(dishes.router,       prefix="/dishes",      tags=["Dishes"])
app.include_router(recipes.router,      prefix="/recipes",     tags=["Recipes"])
app.include_router(sales.router,        prefix="/sales",       tags=["Sales"])
app.include_router(forecast.router,     prefix="/forecast",    tags=["Forecast"])


@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}