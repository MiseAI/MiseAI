from fastapi import FastAPI
from routes import auth, menu, recipe, invoice, forecast, ai_assistant, dashboard

app = FastAPI(title="MiseAI")

app.include_router(auth.router, prefix="/api/auth")
app.include_router(menu.router, prefix="/api/menu")
app.include_router(recipe.router, prefix="/api/recipe")
app.include_router(invoice.router, prefix="/api/invoice")
app.include_router(forecast.router, prefix="/api/forecast")
app.include_router(ai_assistant.router, prefix="/api/ai")
app.include_router(dashboard.router, prefix="/api/dashboard")

@app.get("/")
def root():
    return {"message": "MiseAI backend is live!"}
