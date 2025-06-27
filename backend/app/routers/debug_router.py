from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.utils.fake_data import popular_dados
from app.core.config import settings

router = APIRouter(prefix="/debug", tags=["Debug"])

class DebugResponse(BaseModel):
    msg: str

def verificar_token(token: str):
    if token != settings.DEBUG_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

@router.post("/popular-banco", response_model=DebugResponse)
async def popular_banco(_: str = Depends(verificar_token)):
    await popular_dados()
    return {"msg": "Banco de dados populado com sucesso"}
