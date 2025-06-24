
from fastapi import FastAPI
from routes import forecast

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
