from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioDB
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
service = UsuarioService()


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: UsuarioCreate):
    usuario_id = await service.criar(usuario)
    return {"id": usuario_id}


@router.get("/", response_model=List[UsuarioDB])
async def listar_usuarios():
    return await service.listar()


@router.get("/{usuario_id}", response_model=UsuarioDB)
async def buscar_usuario(usuario_id: str):
    usuario = await service.buscar_por_id(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.put("/{usuario_id}", response_model=dict)
async def atualizar_usuario(usuario_id: str, dados: UsuarioUpdate):
    sucesso = await service.atualizar(usuario_id, dados)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário atualizado com sucesso"}


@router.delete("/{usuario_id}", response_model=dict)
async def deletar_usuario(usuario_id: str):
    sucesso = await service.deletar(usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário removido com sucesso"}
