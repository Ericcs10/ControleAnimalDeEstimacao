from typing import List, Optional
from fastapi import HTTPException
from app.models.especie_model import Especie
from app.repositories import especie_repository
from app.services.base_service import BaseService
from app.schemas.especie_schema import EspecieSchema


class EspecieService(BaseService[EspecieSchema]):

    async def criar(self, dados: EspecieSchema) -> dict:
        especie_id = especie_repository.criar(dados.nome)

        if not especie_id:
            raise HTTPException(status_code=500, detail="Erro ao criar espécie")

        return {"id": especie_id, "nome": dados.nome}

    async def listar(self) -> List[dict]:
        return especie_repository.listar()

    async def buscar_por_id(self, especie_id: str) -> Optional[dict]:
        return especie_repository.buscar_por_id(especie_id)

    async def atualizar(self, especie_id: str, dados: EspecieSchema) -> bool:
        return especie_repository.atualizar(especie_id, dados.nome)

    async def deletar(self, especie_id: str) -> bool:
        return especie_repository.deletar(especie_id)
