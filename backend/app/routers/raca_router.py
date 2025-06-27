from fastapi import APIRouter, status, HTTPException, Depends
from typing import List 

from app.schemas.raca_schema import RacaCreate, RacaUpdate, RacaRead
from app.services.raca_service import RacaService

router = APIRouter(prefix="/racas", tags=["Racas"])

def get_service() -> RacaService: 
    return RacaService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=RacaRead)
async def criar_raca(raca: RacaCreate, service: RacaService = Depends(get_service)):
    raca_id = await service.criar(raca)
    raca_data = await service.buscar_por_id(raca_id)
    return raca_data

@router.get("/", response_model=List[RacaRead])
async def listar_racas(service: RacaService = Depends(get_service)):
    return await service.listar()

@router.get("/{raca_id}", response_model=RacaRead)
async def buscar_raca(raca_id: str, service: RacaService = Depends(get_service)):
    return await service.buscar_por_id(raca_id)

@router.put("/{raca_id}", response_model=RacaRead)
async def atualizar_raca(raca_id: str, raca: RacaUpdate, service: RacaService = Depends(get_service)):
    return await service.atualizar(raca_id, raca)

@router.delete("/{raca_id}", response_model=dict)
async def deletar_raca(raca_id: str, service: RacaService = Depends(get_service)):
    await service.deletar(raca_id)
    return {"message": "Raça removida com sucesso"}
