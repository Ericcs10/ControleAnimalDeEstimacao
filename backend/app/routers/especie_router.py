from fastapi import APIRouter, HTTPException, status, Depends
from typing import List

from app.schemas.especie_schema import EspecieSchema, EspecieDBSchema
from app.services.especie_service import EspecieService

router = APIRouter(prefix="/especies", tags=["Especies"])


def get_service() -> EspecieService:
    return EspecieService()


@router.post("/", response_model=EspecieDBSchema, status_code=status.HTTP_201_CREATED)
async def criar_especie(
    especie: EspecieSchema,
    service: EspecieService = Depends(get_service)
):
    especie_criada = await service.criar(especie)
    return especie_criada


@router.get("/", response_model=List[EspecieDBSchema])
async def listar_especies(service: EspecieService = Depends(get_service)):
    return await service.listar()


@router.get("/{especie_id}", response_model=EspecieDBSchema)
async def buscar_especie(especie_id: str, service: EspecieService = Depends(get_service)):
    especie = await service.buscar_por_id(especie_id)
    if not especie:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return especie


@router.put("/{especie_id}", response_model=EspecieDBSchema)
async def atualizar_especie(
    especie_id: str,
    especie: EspecieSchema,
    service: EspecieService = Depends(get_service)
):
    atualizada = await service.atualizar(especie_id, especie)
    if not atualizada:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return atualizada


@router.delete("/{especie_id}", response_model=dict)
async def deletar_especie(especie_id: str, service: EspecieService = Depends(get_service)):
    sucesso = await service.deletar(especie_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return {"message": "Espécie deletada com sucesso"}
