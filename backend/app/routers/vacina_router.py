from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.vacina_schema import VacinaSchema, VacinaDB
from app.services import vacina_service


router = APIRouter(prefix="/vacinas", tags=["Vacinas"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=dict)
async def criar_vacina(vacina: VacinaSchema):
    vacina_id = await vacina_service.criar_vacina(vacina)
    return {"id": vacina_id}


@router.get("/", response_model=List[VacinaDB])
async def listar_vacinas():
    return await vacina_service.listar_vacinas()


@router.get("/{vacina_id}", response_model=VacinaDB)
async def buscar_vacina(vacina_id: str):
    vacina = await vacina_service.buscar_vacina_por_id(vacina_id)
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return vacina


@router.put("/{vacina_id}", response_model=dict)
async def atualizar_vacina(vacina_id: str, vacina: VacinaSchema):
    sucesso = await vacina_service.atualizar_vacina(vacina_id, vacina)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return {"message": "Vacina atualizada com sucesso"}


@router.delete("/{vacina_id}", response_model=dict)
async def deletar_vacina(vacina_id: str):
    sucesso = await vacina_service.deletar_vacina(vacina_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return {"message": "Vacina deletada com sucesso"}
