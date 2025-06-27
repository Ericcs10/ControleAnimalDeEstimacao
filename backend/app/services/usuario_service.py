from typing import List, Optional
from app.services.base_service import BaseService
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario_schema import UsuarioSchema

class UsuarioService(BaseService[UsuarioSchema]):

    async def criar(self, usuario: UsuarioSchema) -> str:
        return await UsuarioRepository.criar(usuario)

    async def listar(self) -> List[dict]:
        usuarios = await UsuarioRepository.listar()
        for u in usuarios:
            u["id"] = str(u["_id"])
            u.pop("_id", None)
        return usuarios

    async def buscar_por_id(self, usuario_id: str) -> Optional[dict]:
        usuario = await UsuarioRepository.buscar_por_id(usuario_id)
        if usuario:
            usuario["id"] = str(usuario["_id"])
            usuario.pop("_id", None)
        return usuario

    async def atualizar(self, usuario_id: str, dados: UsuarioSchema) -> bool:
        return await UsuarioRepository.atualizar(usuario_id, dados.model_dump())

    async def deletar(self, usuario_id: str) -> bool:
        return await UsuarioRepository.deletar(usuario_id)
