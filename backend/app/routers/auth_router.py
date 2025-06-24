from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from datetime import timedelta
from app.core.database import db
from app.core.security import (
    verificar_senha,
    criar_token,
)


router = APIRouter(prefix="/auth", tags=["Autenticação"])


class LoginSchema(BaseModel):
    email: EmailStr
    senha: str


@router.post("/login")
async def login(dados: LoginSchema):
    user = await db["usuarios"].find_one({"email": dados.email})
    if not user:
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    if not verificar_senha(dados.senha, user["senha"]):
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    token = criar_token(
        data={"sub": dados.email},
        expires_delta=timedelta(minutes=60),
    )

    return {"access_token": token, "token_type": "bearer"}
