from typing import List
from fastapi import HTTPException
from app.schemas.raca_schema import RacaSchema
from app.repositories import raca_repository


async def criar_raca(raca: RacaSchema) -> str:
    return await raca_repository.create_raca(raca)


async def listar_racas() -> List[RacaSchema]:
    return await raca_repository.get_racas()


async def buscar_raca_por_id(raca_id: str):
    raca = await raca_repository.get_raca_by_id(raca_id)
    if not raca:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return raca


async def atualizar_raca(raca_id: str, dados: RacaSchema):
    atualizado = await raca_repository.update_raca(raca_id, dados.model_dump())
    if not atualizado:
        raise HTTPException(
            status_code=404, detail="Raça não encontrada ou nada foi alterado"
        )
    return {"msg": "Raça atualizada com sucesso"}


async def deletar_raca(raca_id: str):
    deletado = await raca_repository.delete_raca(raca_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Raça não encontrada")
    return {"msg": "Raça removida com sucesso"}
