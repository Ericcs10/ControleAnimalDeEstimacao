from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar("T")  # Tipo do schema

class BaseService(ABC, Generic[T]):

    @abstractmethod
    async def criar(self, obj: T) -> str:
        pass

    @abstractmethod
    async def listar(self) -> List[T]:
        pass

    @abstractmethod
    async def buscar_por_id(self, id_: str) -> T:
        pass

    @abstractmethod
    async def atualizar(self, id_: str, obj: T) -> bool:
        pass

    @abstractmethod
    async def deletar(self, id_: str) -> bool:
        pass