from typing import List, Optional
from fastapi import HTTPException
from app.schemas.vacina_schema import VacinaCreate, VacinaUpdate, VacinaSchema
from app.repositories import vacina_repository
from app.services.base_service import BaseService

class VacinaService(BaseService[VacinaCreate]):
    async def criar(self, dados: VacinaCreate) -> str:
        return await vacina_repository.create_vacina(dados)

    async def listar(self) -> List[VacinaSchema]:
        return await vacina_repository.get_vacinas()

    async def buscar_por_id(self, vacina_id: str) -> Optional[VacinaSchema]:
        vacina = await vacina_repository.get_vacina_by_id(vacina_id)
        if not vacina:
            raise HTTPException(status_code=404, detail="Vacina não encontrada")
        return vacina

    async def atualizar(self, vacina_id: str, dados: VacinaUpdate) -> bool:
        atualizado = await vacina_repository.update_vacina(vacina_id, dados.model_dump())
        if not atualizado:
            raise HTTPException(
                status_code=404, detail="Vacina não encontrada ou nada foi alterado"
            )
        return True

    async def deletar(self, vacina_id: str) -> bool:
        deletado = await vacina_repository.delete_vacina(vacina_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Vacina não encontrada")
        return True
