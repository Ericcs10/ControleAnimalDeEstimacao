from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from typing import List

from app.core.database import db
from app.schemas.usuario_schema import UsuarioSchema, UsuarioDB


router = APIRouter()


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: UsuarioSchema):
    usuario_dict = usuario.model_dump()
    result = await db["usuarios"].insert_one(usuario_dict)
    return {"id": str(result.inserted_id)}


@router.get("/", response_model=List[UsuarioDB])
async def listar_usuarios():
    usuarios = await db["usuarios"].find().to_list(100)
    for usuario in usuarios:
        usuario["id"] = str(usuario["_id"])
        usuario.pop("_id", None)
    return usuarios


@router.get("/{usuario_id}", response_model=UsuarioDB)
async def buscar_usuario(usuario_id: str):
    usuario = await db["usuarios"].find_one({"_id": ObjectId(usuario_id)})
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    usuario["id"] = str(usuario["_id"])
    usuario.pop("_id", None)
    return usuario


@router.put("/{usuario_id}", response_model=dict)
async def atualizar_usuario(usuario_id: str, dados: UsuarioSchema):
    result = await db["usuarios"].update_one(
        {"_id": ObjectId(usuario_id)},
        {"$set": dados.model_dump()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário atualizado com sucesso"}


@router.delete("/{usuario_id}", response_model=dict)
async def deletar_usuario(usuario_id: str):
    result = await db["usuarios"].delete_one({"_id": ObjectId(usuario_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário removido com sucesso"}
