from typing import List
from fastapi import HTTPException
from app.schemas.raca_schema import RacaSchema
from app.repositories import raca_repository
from app.services.base_service import BaseService

class RacaService(BaseService[RacaSchema]):

    async def criar(self, raca: RacaSchema) -> str:
        return await raca_repository.create_raca(raca)

    async def listar(self) -> List[RacaSchema]:
        return await raca_repository.get_racas()

    async def buscar_por_id(self, raca_id: str):
        raca = await raca_repository.get_raca_by_id(raca_id)
        if not raca:
            raise HTTPException(status_code=404, detail="Raça não encontrada")
        return raca

    async def atualizar(self, raca_id: str, dados: RacaSchema):
        atualizado = await raca_repository.update_raca(raca_id, dados.model_dump())
        if not atualizado:
            raise HTTPException(
                status_code=404, detail="Raça não encontrada ou nada foi alterado"
            )
        return {"msg": "Raça atualizada com sucesso"}

    async def deletar(self, raca_id: str):
        deletado = await raca_repository.delete_raca(raca_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Raça não encontrada")
        return {"msg": "Raça removida com sucesso"}