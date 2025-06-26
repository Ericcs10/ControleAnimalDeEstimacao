from typing import List, Optional
from app.services.base_service import BaseService
from app.schemas.animal_schema import AnimalSchema
from app.repositories.animal_repository import AnimalRepository 

class AnimalService(BaseService[AnimalSchema]):

    async def criar(self, animal: AnimalSchema) -> str:
        return await AnimalRepository.criar(animal)

    async def listar(self) -> List[dict]:
        animais = await AnimalRepository.listar()
        for a in animais:
            a["id"] = str(a["_id"])
            a.pop("_id", None)
        return animais

    async def buscar_por_id(self, animal_id: str) -> Optional[dict]:
        animal = await AnimalRepository.buscar_por_id(animal_id)
        if animal:
            animal["id"] = str(animal["_id"])
            animal.pop("_id", None)
        return animal

    async def atualizar(self, animal_id: str, dados: AnimalSchema) -> bool:
        return await AnimalRepository.atualizar(animal_id, dados.model_dump())

    async def deletar(self, animal_id: str) -> bool:
        return await AnimalRepository.deletar(animal_id)
