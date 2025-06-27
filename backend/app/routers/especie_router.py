from fastapi import APIRouter, HTTPException, status
from typing import List

from app.schemas.especie_schema import EspecieSchema, EspecieDB
from app.services import especie_service 

router = APIRouter(prefix="/especies", tags=["Especies"])


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def criar_especie(especie: EspecieSchema):
    especie_id = await especie_service.criar_especie(especie.nome)
    return {"id": especie_id}


@router.get("/", response_model=List[EspecieDB])
async def listar_especies():
    return await especie_service.listar_especies()


@router.get("/{especie_id}", response_model=EspecieDB)
async def buscar_especie(especie_id: str):
    especie = await especie_service.buscar_especie_por_id(especie_id)
    if not especie:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return especie


@router.put("/{especie_id}", response_model=dict)
async def atualizar_especie(especie_id: str, especie: EspecieSchema):
    sucesso = await especie_service.atualizar_especie(especie_id, especie.nome)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return {"message": "Espécie atualizada com sucesso"}


@router.delete("/{especie_id}", response_model=dict)
async def deletar_especie(especie_id: str):
    sucesso = await especie_service.deletar_especie(especie_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return {"message": "Espécie deletada com sucesso"}
