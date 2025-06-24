from fastapi import FastAPI
from app.routers import usuario_router, animal_router, vacina_router, raca_router

app = FastAPI(
    title="Controle de Animais de Estimação",
    version="1.0.0",
    description="API para gestão de usuários, animais, raças e vacinas."
)

app.include_router(usuario_router.router)
app.include_router(animal_router.router)
app.include_router(vacina_router.router)
app.include_router(raca_router.router)

@app.get("/")
async def root():
    return {"message": "API do Controle de Animais está no ar 🐶🐱🐾"}
