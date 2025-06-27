from typing import List, Optional
from fastapi import HTTPException
from app.models.especie_model import Especie
from app.repositories import especie_repository
from app.services.base_service import BaseService
from app.schemas.especie_schema import EspecieSchema


class EspecieService(BaseService[EspecieSchema]):

    async def criar(self, dados: EspecieSchema) -> str:
        especie = Especie(nome=dados.nome)
        especie_id = especie_repository.create_especie(especie)
        return str(especie_id)

    async def listar(self) -> List[dict]:
        especies = especie_repository.get_all_especies()
        return [{"id": str(e._id), "nome": e.nome} for e in especies]

    async def buscar_por_id(self, especie_id: str) -> Optional[dict]:
        especie = especie_repository.get_especie_by_id(especie_id)
        if not especie:
            return None
        return {"id": str(especie._id), "nome": especie.nome}

    async def atualizar(self, especie_id: str, dados: EspecieSchema) -> bool:
        atualizado = especie_repository.update_especie(especie_id, dados.nome)
        return atualizado

    async def deletar(self, especie_id: str) -> bool:
        deletado = especie_repository.delete_especie(especie_id)
        return deletado