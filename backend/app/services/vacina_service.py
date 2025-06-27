from typing import List, Optional
from fastapi import HTTPException
from app.schemas.vacina_schema import VacinaCreate, VacinaUpdate, VacinaRead
from app.repositories.vacina_repository import VacinaRepository
from app.services.base_service import BaseService

class VacinaService(BaseService[VacinaCreate]):
    def __init__(self):
        self.repository = VacinaRepository()

    async def criar(self, dados: VacinaCreate) -> str:
        return await self.repository.criar(dados)

    async def listar(self) -> List[VacinaRead]:
        return await self.repository.listar()

    async def buscar_por_id(self, vacina_id: str) -> Optional[VacinaRead]:
        vacina = await self.repository.buscar_por_id(vacina_id)
        if not vacina:
            raise HTTPException(status_code=404, detail="Vacina não encontrada")
        return vacina

    async def atualizar(self, vacina_id: str, dados: VacinaUpdate) -> VacinaRead:
        atualizado = await self.repository.atualizar(vacina_id, dados.model_dump())
        if not atualizado:
            raise HTTPException(status_code=404, detail="Vacina não encontrada ou nada foi alterado")
        return await self.buscar_por_id(vacina_id)

    async def deletar(self, vacina_id: str) -> bool:
        deletado = await self.repository.deletar(vacina_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Vacina não encontrada")
        return True
