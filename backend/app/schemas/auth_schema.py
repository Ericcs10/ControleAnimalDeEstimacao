from pydantic import BaseModel, EmailStr, Field

class LoginSchema(BaseModel):
    email: EmailStr
    senha: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UsuarioCreateSchema(BaseModel):
    email: EmailStr
    senha: str = Field(..., min_length=4)
    nome: str