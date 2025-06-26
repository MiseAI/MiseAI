from fastapi import FastAPI
from routes import dashboard

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello from Backend!"}
