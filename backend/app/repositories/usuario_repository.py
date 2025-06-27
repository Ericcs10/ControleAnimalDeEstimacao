from typing import List, Optional
from bson import ObjectId
from datetime import datetime, timezone
from app.core.database import db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioDB
from app.repositories.base_repository import BaseRepository

class UsuarioRepository(BaseRepository[UsuarioCreate]):
    collection = db["usuarios"]

    async def criar(self, usuario: UsuarioCreate) -> str:
        data = usuario.model_dump()
        now = datetime.now(timezone.utc)
        data["data_criacao"] = now
        data["data_atualizacao"] = now

        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def listar(self) -> List[UsuarioDB]:
        usuarios = await self.collection.find().to_list(100)
        usuarios_formatados = []
        for u in usuarios:
            try:
                u["id"] = str(u["_id"])
                u.pop("_id", None)
                usuarios_formatados.append(UsuarioDB(**u))
            except Exception as e:
                print("Erro ao formatar usuário:", u)
                print("Erro:", e)
        return usuarios_formatados

    async def buscar_por_id(self, usuario_id: str) -> Optional[UsuarioDB]:
        try:
            usuario = await self.collection.find_one({"_id": ObjectId(usuario_id)})
            if usuario:
                usuario["id"] = str(usuario["_id"])
                usuario.pop("_id", None)
                return UsuarioDB(**usuario)
            return None
        except Exception as e:
            print(f"Erro ao buscar usuário com ID {usuario_id}: {e}")
            return None

    async def atualizar(self, usuario_id: str, dados: dict) -> bool:
        dados["data_atualizacao"] = datetime.now(timezone.utc)
        result = await self.collection.update_one(
            {"_id": ObjectId(usuario_id)},
            {"$set": dados}
        )
        return result.modified_count > 0

    async def deletar(self, usuario_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(usuario_id)})
        return result.deleted_count > 0
