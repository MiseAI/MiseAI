from fastapi import FastAPI
from routes import auth, menu, recipe, invoice, forecast, ai_assistant, dashboard

app = FastAPI()

app.include_router(auth.router)
app.include_router(menu.router)
app.include_router(recipe.router)
app.include_router(invoice.router)
app.include_router(forecast.router)
app.include_router(ai_assistant.router)
app.include_router(dashboard.router)
