from typing import List, Optional
from fastapi import HTTPException
from app.schemas.raca_schema import RacaCreate, RacaUpdate, RacaSchema
from app.repositories import raca_repository
from app.services.base_service import BaseService


class RacaService(BaseService[RacaCreate]):
    async def criar(self, dados: RacaCreate) -> str:
        return await raca_repository.create_raca(dados)

    async def listar(self) -> List[RacaSchema]:
        return await raca_repository.get_racas()

    async def buscar_por_id(self, raca_id: str) -> Optional[RacaSchema]:
        raca = await raca_repository.get_raca_by_id(raca_id)
        if not raca:
            raise HTTPException(status_code=404, detail="Raça não encontrada")
        return raca

    async def atualizar(self, raca_id: str, dados: RacaUpdate) -> bool:
        atualizado = await raca_repository.update_raca(raca_id, dados.model_dump())
        if not atualizado:
            raise HTTPException(
                status_code=404, detail="Raça não encontrada ou nada foi alterado"
            )
        return True

    async def deletar(self, raca_id: str) -> bool:
        deletado = await raca_repository.delete_raca(raca_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Raça não encontrada")
        return True
