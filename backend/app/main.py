from fastapi import FastAPI
from app.routers import usuario_router, animal_router, vacina_router, raca_router


app = FastAPI(title="Controle de Pets")


app.include_router(usuario_router.router)
app.include_router(animal_router.router)
app.include_router(vacina_router.router)
app.include_router(raca_router.router)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
