from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from datetime import timedelta
from app.core.database import db
from app.core.security import verificar_senha, criar_token

router = APIRouter(prefix="/auth", tags=["Autenticação"]) 
class LoginSchema(BaseModel):
    email: EmailStr
    senha: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

@router.post("/login", response_model=TokenResponse)
async def login(dados: LoginSchema):
    usuario = await db["usuarios"].find_one({"email": dados.email})
    if not usuario or not verificar_senha(dados.senha, usuario.get("senha", "")):
        raise HTTPException(status_code=400, detail="Email ou senha inválidos")

    token = criar_token(
        data={"sub": dados.email},
        expires_delta=timedelta(minutes=60),
    )

    return {"access_token": token, "token_type": "bearer"}
