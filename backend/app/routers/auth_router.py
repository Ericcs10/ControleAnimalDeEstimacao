from fastapi import APIRouter, HTTPException, status 
from datetime import timedelta
import bcrypt

from app.core.database import db
from app.core.security import verificar_senha, criar_token
from app.schemas.auth_schema import LoginSchema, TokenResponse, UsuarioCreateSchema

router = APIRouter(prefix="/auth", tags=["Autenticação"])

usuarios_collection = db["usuarios"]

# Endpoint de login
@router.post("/login", response_model=TokenResponse)
async def login(dados: LoginSchema):
    usuario = await usuarios_collection.find_one({"email": dados.email})
    if not usuario or not verificar_senha(dados.senha, usuario["senha"]):
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    token = criar_token(
        data={"sub": dados.email},
        expires_delta=timedelta(minutes=60),
    )

    return {"access_token": token, "token_type": "bearer"}

# Endpoint de cadastro
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def registrar(usuario: UsuarioCreateSchema):
    existente = await usuarios_collection.find_one({"email": usuario.email})
    if existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    senha_hash = bcrypt.hashpw(usuario.senha.encode("utf-8"), bcrypt.gensalt())

    novo_usuario = {
        "email": usuario.email,
        "senha": senha_hash,
        "nome": usuario.nome
    }

    result = await usuarios_collection.insert_one(novo_usuario)

    return {
        "message": "Usuário cadastrado com sucesso",
        "id": str(result.inserted_id)
    }
