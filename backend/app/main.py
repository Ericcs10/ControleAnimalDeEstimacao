from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.routers import (
    usuario_router,
    animal_router,
    vacina_router,
    raca_router,
    auth_router,
    especie_router,
)

from app.utils import fake_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    await fake_data.popular_dados(limpar_db=True)
    yield


app = FastAPI(
    title="Controle de Pets",
    lifespan=lifespan
)
app.include_router(usuario_router.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(animal_router.router, prefix="/animais", tags=["Animais"])
app.include_router(vacina_router.router, prefix="/vacinas", tags=["Vacinas"])
app.include_router(raca_router.router, prefix="/racas", tags=["Racas"])
app.include_router(auth_router.router, prefix="/auth", tags=["Autenticação"])
app.include_router(especie_router.router, prefix="/especies", tags=["Especies"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
