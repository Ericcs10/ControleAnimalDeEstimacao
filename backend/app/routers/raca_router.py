from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.raca_schema import RacaSchema, RacaDB
from app.services import raca_service 


router = APIRouter(prefix="/racas", tags=["Racas"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
async def criar_raca(raca: RacaSchema):
    raca_id = await raca_service.criar_raca(raca)
    return {"id": raca_id}


@router.get("/", response_model=List[RacaDB])
async def listar_racas():
    return await raca_service.listar_racas()


@router.get("/{raca_id}", response_model=RacaDB)
async def buscar_raca(raca_id: str):
    raca = await raca_service.buscar_raca_por_id(raca_id)
    if not raca:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return raca


@router.put("/{raca_id}", response_model=dict)
async def atualizar_raca(raca_id: str, raca: RacaSchema):
    sucesso = await raca_service.atualizar_raca(raca_id, raca)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return {"message": "Raça atualizada com sucesso"}


@router.delete("/{raca_id}", response_model=dict)
async def deletar_raca(raca_id: str):
    sucesso = await raca_service.deletar_raca(raca_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return {"message": "Raça deletada com sucesso"}
