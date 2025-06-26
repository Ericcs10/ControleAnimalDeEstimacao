from typing import List
from fastapi import HTTPException
from app.schemas.vacina_schema import VacinaSchema
from app.repositories import vacina_repository
from app.services.base_service import BaseService

class VacinaService(BaseService[VacinaSchema]):

    async def criar(self, vacina: VacinaSchema) -> str:
        return await vacina_repository.create_vacina(vacina)

    async def listar(self) -> List[VacinaSchema]:
        return await vacina_repository.get_vacinas()

    async def buscar_por_id(self, vacina_id: str):
        vacina = await vacina_repository.get_vacina_by_id(vacina_id)
        if not vacina:
            raise HTTPException(status_code=404, detail="Vacina não encontrada")
        return vacina

    async def atualizar(self, vacina_id: str, dados: VacinaSchema):
        atualizado = await vacina_repository.update_vacina(vacina_id, dados.model_dump())
        if not atualizado:
            raise HTTPException(
                status_code=404, detail="Vacina não encontrada ou nada foi alterado"
            )
        return {"msg": "Vacina atualizada com sucesso"}

    async def deletar(self, vacina_id: str):
        deletado = await vacina_repository.delete_vacina(vacina_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Vacina não encontrada")
        return {"msg": "Vacina removida com sucesso"}