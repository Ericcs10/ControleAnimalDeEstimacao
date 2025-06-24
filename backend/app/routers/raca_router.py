from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.raca_schema import RacaSchema
from app.repositories import raca_repository


router = APIRouter(prefix="/racas", tags=["Raças"])


@router.get("/", response_model=List[RacaSchema])
async def listar_racas():
    return await raca_repository.listar_racas()


@router.get("/{raca_id}", response_model=RacaSchema)
async def buscar_raca(raca_id: str):
    raca = await raca_repository.buscar_raca_por_id(raca_id)
    if not raca:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return raca


@router.post("/", response_model=RacaSchema, status_code=201)
async def criar_raca(raca: RacaSchema):
    return await raca_repository.criar_raca(raca)


@router.put("/{raca_id}", response_model=RacaSchema)
async def atualizar_raca(raca_id: str, raca: RacaSchema):
    raca_atualizada = await raca_repository.atualizar_raca(raca_id, raca)
    if not raca_atualizada:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return raca_atualizada


@router.delete("/{raca_id}")
async def deletar_raca(raca_id: str):
    deletado = await raca_repository.deletar_raca(raca_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return {"message": "Raça deletada com sucesso"}
