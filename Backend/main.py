from fastapi import FastAPI
from routes import forecast

app = FastAPI()
app.include_router(forecast.router)

@app.get("/")
def read_root():
    return {"message": "Forecast Tool is live!"}
