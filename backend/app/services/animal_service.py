from typing import List, Optional
from app.services.base_service import BaseService
from app.schemas.animal_schema import AnimalCreate
from app.repositories.animal_repository import AnimalRepository
from fastapi import HTTPException

class AnimalService(BaseService[AnimalCreate]):
    def __init__(self):
        self.repository = AnimalRepository()

    async def criar(self, animal: AnimalCreate) -> str:
        return await self.repository.criar(animal)

    async def listar(self) -> List[dict]:
        return await self.repository.listar()

    async def buscar_por_id(self, animal_id: str) -> Optional[dict]:
        animal = await self.repository.buscar_por_id(animal_id)
        if not animal:
            raise HTTPException(status_code=404, detail="Animal não encontrado")
        return animal

    async def atualizar(self, animal_id: str, dados: AnimalCreate) -> bool:
        atualizado = await self.repository.atualizar(animal_id, dados.model_dump())
        if not atualizado:
            raise HTTPException(status_code=404, detail="Animal não encontrado ou nada foi alterado")
        return True

    async def deletar(self, animal_id: str) -> bool:
        deletado = await self.repository.deletar(animal_id)
        if not deletado:
            raise HTTPException(status_code=404, detail="Animal não encontrado")
        return True
