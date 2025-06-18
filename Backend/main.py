from fastapi import FastAPI
from routers import auth, ingredients, dishes, recipes, sales, forecast
from database import Base, engine

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MiseAI API")

app.include_router(auth.router)
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(dishes.router, prefix="/dishes", tags=["Dishes"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(forecast.router, prefix="/forecast", tags=["Forecast"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to MiseAI API"}
