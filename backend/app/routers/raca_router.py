from fastapi import APIRouter, status
from typing import List
from app.schemas.raca_schema import RacaSchema
from app.services import raca_service


router = APIRouter(prefix="/racas", tags=["Racas"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_raca(raca: RacaSchema):
    return await raca_service.criar_raca(raca)


@router.get("/", response_model=List[RacaSchema])
async def listar_racas():
    return await raca_service.listar_racas()


@router.get("/{raca_id}", response_model=RacaSchema)
async def buscar_raca(raca_id: str):
    return await raca_service.buscar_raca_por_id(raca_id)


@router.put("/{raca_id}")
async def atualizar_raca(raca_id: str, raca: RacaSchema):
    return await raca_service.atualizar_raca(raca_id, raca)


@router.delete("/{raca_id}")
async def deletar_raca(raca_id: str):
    return await raca_service.deletar_raca(raca_id)
