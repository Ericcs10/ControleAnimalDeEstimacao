from fastapi import FastAPI
from app.core.database import client, db

app = FastAPI(title="Controle de Pets")

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
    