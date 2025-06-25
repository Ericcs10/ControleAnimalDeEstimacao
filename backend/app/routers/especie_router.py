from fastapi import APIRouter, HTTPException
from app.repositories import especie_repository
from app.services import especie_service
from app.models.especie_model import Especie
from app.schemas.especie_schema import EspecieSchema
from app.core.database import db

router = APIRouter()

@router.post("/")
def criar_especie(especie: EspecieSchema):
    especie_id = especie_service.criar_especie(especie.nome)
    return {"id": especie_id}

@router.get("/")
def listar_especies():
    especies = especie_service.listar_especies()
    return [{"id": str(e._id), "nome": e.nome} for e in especies]

@router.get("/{especie_id}")
def buscar_especie(especie_id: str):
    especie = especie_service.buscar_especie_por_id(especie_id)
    if not especie:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return {"id": str(especie._id), "nome": especie.nome}

@router.put("/{especie_id}")
def atualizar_especie(especie_id: str, especie: EspecieSchema):
    sucesso = especie_service.atualizar_especie(especie_id, especie.nome)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return {"message": "Espécie atualizada com sucesso"}

@router.delete("/{especie_id}")
def deletar_especie(especie_id: str):
    sucesso = especie_service.deletar_especie(especie_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Espécie não encontrada")
    return {"message": "Espécie deletada com sucesso"}
