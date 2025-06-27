from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class BaseService(ABC, Generic[T]):

    @abstractmethod
    async def criar(self, obj: T) -> str:
        pass

    @abstractmethod
    async def listar(self) -> List[dict]:
        pass

    @abstractmethod
    async def buscar_por_id(self, id_: str) -> Optional[dict]:
        pass

    @abstractmethod
    async def atualizar(self, id_: str, obj: T) -> bool:
        pass

    @abstractmethod
    async def deletar(self, id_: str) -> bool:
        pass
