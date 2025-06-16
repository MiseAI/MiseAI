from fastapi import FastAPI
from routers import ingredients, dishes, recipes

app = FastAPI(title="MiseAI Backend")

app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(dishes.router, prefix="/dishes", tags=["Dishes"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to MiseAI API"}
