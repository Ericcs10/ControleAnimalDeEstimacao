from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.vacina_schema import VacinaSchema
from app.repositories import vacina_repository


router = APIRouter(prefix="/vacinas", tags=["Vacinas"])


@router.get("/", response_model=List[VacinaSchema])
async def listar_vacinas():
    return await vacina_repository.listar_vacinas()


@router.get("/{vacina_id}", response_model=VacinaSchema)
async def buscar_vacina(vacina_id: str):
    vacina = await vacina_repository.buscar_vacina_por_id(vacina_id)
    if not vacina:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return vacina


@router.post("/", response_model=VacinaSchema, status_code=201)
async def criar_vacina(vacina: VacinaSchema):
    return await vacina_repository.criar_vacina(vacina)


@router.put("/{vacina_id}", response_model=VacinaSchema)
async def atualizar_vacina(vacina_id: str, vacina: VacinaSchema):
    vacina_atualizada = await vacina_repository.atualizar_vacina(vacina_id, vacina)
    if not vacina_atualizada:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return vacina_atualizada


@router.delete("/{vacina_id}")
async def deletar_vacina(vacina_id: str):
    deletado = await vacina_repository.deletar_vacina(vacina_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Vacina não encontrada")
    return {"message": "Vacina deletada com sucesso"}
