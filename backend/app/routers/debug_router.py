from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.fake_data import popular_dados 
from app.core.config import settings
from pydantic import BaseModel

router = APIRouter(prefix="/debug", tags=["Debug"])

def verificar_token(token: str):
    if token != settings.DEBUG_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")


class DebugResponse(BaseModel):
    msg: str



@router.post("/popular-banco", response_model=DebugResponse)
async def popular_com_dados(token: str = Depends(verificar_token)):
    await popular_dados()
    return {"msg": "Banco de dados populado com sucesso"}
