from fastapi import APIRouter, status, HTTPException, Depends
from typing import List 

from app.schemas.vacina_schema import VacinaCreate, VacinaUpdate, VacinaRead
from app.services.vacina_service import VacinaService

router = APIRouter(prefix="/vacinas", tags=["Vacinas"])


def get_service() -> VacinaService:
    return VacinaService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
async def criar_vacina(vacina: VacinaCreate, service: VacinaService = Depends(get_service)):
    vacina_id = await service.criar(vacina)
    return {"id": vacina_id}

@router.get("/", response_model=List[VacinaRead])
async def listar_vacinas(service: VacinaService = Depends(get_service)):
    return await service.listar()

@router.get("/{vacina_id}", response_model=VacinaRead)
async def buscar_vacina(vacina_id: str, service: VacinaService = Depends(get_service)):
    return await service.buscar_por_id(vacina_id)

@router.put("/{vacina_id}", response_model=VacinaRead)
async def atualizar_vacina(vacina_id: str, vacina: VacinaUpdate, service: VacinaService = Depends(get_service)):
    return await service.atualizar(vacina_id, vacina)

@router.delete("/{vacina_id}", response_model=dict)
async def deletar_vacina(vacina_id: str, service: VacinaService = Depends(get_service)):
    sucesso = await service.deletar(vacina_id)
    return {"message": "Vacina removida com sucesso"}
