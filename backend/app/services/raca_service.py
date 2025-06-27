from typing import List, Optional
from fastapi import HTTPException
from app.schemas.raca_schema import RacaCreate, RacaUpdate
from app.repositories.raca_repository import RacaRepository

class RacaService:
    def __init__(self):
        self.repository = RacaRepository()
        

    async def criar(self, dados: RacaCreate) -> str:
        return await self.repository.criar(dados)

    async def listar(self) -> List[dict]:
        return await self.repository.listar()

    async def buscar_por_id(self, raca_id: str) -> Optional[dict]:
        raca = await self.repository.buscar_por_id(raca_id)
        if not raca:
            raise HTTPException(status_code=404, detail="Raça não encontrada")
        return raca

    async def atualizar(self, raca_id: str, dados: RacaUpdate) -> bool:
        atualizado = await self.repository.atualizar(raca_id, dados.model_dump(exclude_unset=True))
        if not atualizado:
            raise HTTPException(
                status_code=404, detail="Raça não encontrada ou nada foi alterado"
            )
        return True

    async def deletar(self, raca_id: str) -> bool:
        deletado = await self.repository.deletar(raca_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Raça não encontrada")
        return True
