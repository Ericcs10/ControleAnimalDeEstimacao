from typing import List, Optional
from app.services.base_service import BaseService
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario_schema import UsuarioSchema, UsuarioDB


class UsuarioService(BaseService[UsuarioSchema]):
    def __init__(self):
        self.repository = UsuarioRepository()

    async def criar(self, usuario: UsuarioSchema) -> str:
        return await self.repository.criar(usuario)

    async def listar(self) -> List[UsuarioDB]:
        return await self.repository.listar()

    async def buscar_por_id(self, usuario_id: str) -> Optional[UsuarioDB]:
        return await self.repository.buscar_por_id(usuario_id)

    async def atualizar(self, usuario_id: str, dados: UsuarioSchema) -> bool:
        return await self.repository.atualizar(usuario_id, dados.model_dump())

    async def deletar(self, usuario_id: str) -> bool:
        return await self.repository.deletar(usuario_id)
