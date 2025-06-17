from fastapi import FastAPI
from backend.routers import ingredients, dishes, recipes, sales, forecast

app = FastAPI(title="MiseAI Backend")

app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(dishes.router, prefix="/dishes", tags=["Dishes"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(forecast.router, prefix="/forecast", tags=["Forecast"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
