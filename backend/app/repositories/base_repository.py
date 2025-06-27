from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class BaseRepository(ABC, Generic[T]):

    @abstractmethod
    async def criar(self, obj: T) -> str:
        pass

    @abstractmethod
    async def listar(self) -> List[dict]:
        pass

    @abstractmethod
    async def buscar_por_id(self, obj_id: str) -> Optional[dict]:
        pass

    @abstractmethod
    async def atualizar(self, obj_id: str, dados: dict) -> bool:
        pass

    @abstractmethod
    async def deletar(self, obj_id: str) -> bool:
        pass
