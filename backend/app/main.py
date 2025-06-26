from fastapi import FastAPI 
from app.routers import (
    usuario_router,
    animal_router,
    vacina_router,
    raca_router,
    auth_router,
    especie_router,
    debug_router  
)

app = FastAPI(title="Controle de Pets")

app.include_router(usuario_router.router, prefix="/usuarios", tags=["Usuarios"]) 
app.include_router(animal_router.router, prefix="/animais", tags=["Animais"])
app.include_router(vacina_router.router, prefix="/vacinas", tags=["Vacinas"])
app.include_router(raca_router.router, prefix="/racas", tags=["Racas"])
app.include_router(auth_router.router, prefix="/auth", tags=["Autenticação"])
app.include_router(especie_router.router, prefix="/especies", tags=["Especies"])
app.include_router(debug_router.router) 

@app.get("/")
async def root():
    return {"message": "Hello World"}
