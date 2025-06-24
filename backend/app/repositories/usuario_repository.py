from typing import List, Optional
from app.core.database import db
from app.schemas.usuario_schema import UsuarioSchema, UsuarioDB
from bson import ObjectId
from datetime import datetime


collection = db.usuarios


async def listar_usuarios() -> List[UsuarioDB]:
    return await collection.find().to_list(1000)


async def buscar_usuario_por_id(usuario_id: str) -> Optional[UsuarioDB]:
    return await collection.find_one({"_id": ObjectId(usuario_id)})


async def criar_usuario(usuario: UsuarioSchema) -> UsuarioDB:
    data = usuario.dict()
    data["data_criacao"] = datetime.utcnow()
    data["data_atualizacao"] = datetime.utcnow()

    result = await collection.insert_one(data)
    return await collection.find_one({"_id": result.inserted_id})


async def atualizar_usuario(usuario_id: str, usuario: UsuarioSchema) -> Optional[UsuarioDB]:
    data = usuario.dict()
    data["data_atualizacao"] = datetime.utcnow()

    await collection.update_one({"_id": ObjectId(usuario_id)}, {"$set": data})
    return await collection.find_one({"_id": ObjectId(usuario_id)})


async def deletar_usuario(usuario_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(usuario_id)})
    return result.deleted_count == 1
