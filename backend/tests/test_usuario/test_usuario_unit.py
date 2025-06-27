import pytest 
from app.services.usuario_service import UsuarioService
from app.schemas.usuario_schema import UsuarioSchema

usuario_service = UsuarioService()


@pytest.mark.asyncio
async def test_criar_usuario_unitario():
    usuario = UsuarioSchema(
        email="unit@test.com",
        cpf="12345678911",
        telefone="61999998888",
        senha="senha123"
    )
    resultado = await usuario_service.criar(usuario)
    assert isinstance(resultado, str)