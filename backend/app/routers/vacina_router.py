from fastapi import APIRouter, status, HTTPException, Depends
from typing import List 

from app.schemas.vacina_schema import VacinaSchema, VacinaDBSchema
from app.services.vacina_service import VacinaService

router = APIRouter(prefix="/vacinas", tags=["Vacinas"])


def get_service() -> VacinaService:
    return VacinaService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VacinaDBSchema)
async def criar_vacina(
    vacina: VacinaSchema,
    service: VacinaService = Depends(get_service)
):
    return await service.criar(vacina)


@router.get("/", response_model=List[VacinaDBSchema])
async def listar_vacinas(service: VacinaService = Depends(get_service)):
    return await service.listar()


@router.get("/{vacina_id}", response_model=VacinaDBSchema)
async def buscar_vacina(vacina_id: str, service: VacinaService = Depends(get_service)):
    vacina = await service.buscar_por_id(vacina_id)
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return vacina


@router.put("/{vacina_id}", response_model=VacinaDBSchema)
async def atualizar_vacina(
    vacina_id: str,
    vacina: VacinaSchema,
    service: VacinaService = Depends(get_service)
):
    atualizada = await service.atualizar(vacina_id, vacina)
    if not atualizada:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return atualizada


@router.delete("/{vacina_id}", response_model=dict)
async def deletar_vacina(vacina_id: str, service: VacinaService = Depends(get_service)):
    sucesso = await service.deletar(vacina_id)
    if not sucesso:
        raise HTTPException
