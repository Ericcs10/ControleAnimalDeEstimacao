from fastapi import APIRouter, status
from typing import List
from app.schemas.vacina_schema import VacinaSchema
from app.services import vacina_service


router = APIRouter(prefix="/vacinas", tags=["Vacinas"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def criar_vacina(vacina: VacinaSchema):
    return await vacina_service.criar_vacina(vacina)


@router.get("/", response_model=List[VacinaSchema])
async def listar_vacinas():
    return await vacina_service.listar_vacinas()


@router.get("/{vacina_id}", response_model=VacinaSchema)
async def buscar_vacina(vacina_id: str):
    return await vacina_service.buscar_vacina_por_id(vacina_id)


@router.put("/{vacina_id}")
async def atualizar_vacina(vacina_id: str, vacina: VacinaSchema):
    return await vacina_service.atualizar_vacina(vacina_id, vacina)


@router.delete("/{vacina_id}")
async def deletar_vacina(vacina_id: str):
    return await vacina_service.deletar_vacina(vacina_id)
