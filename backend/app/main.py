from fastapi import FastAPI
from app.routers import usuario_router  

app = FastAPI(title="Controle de Pets")

app.include_router(usuario_router.router)

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
