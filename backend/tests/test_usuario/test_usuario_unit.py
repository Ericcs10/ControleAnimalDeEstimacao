from unittest.mock import AsyncMock, patch
import pytest
from app.schemas.usuario_schema import UsuarioSchema
from app.services.usuario_service import UsuarioService

@pytest.mark.asyncio
@patch("app.services.usuario_service.usuario_repository")
async def test_criar_usuario_unit(mock_repo):
    mock_repo.criar_usuario = AsyncMock(return_value={"id": "123"})

    usuario = UsuarioSchema(
        email="a@a.com",
        cpf="12345678900",
        telefone="61999999999",
        senha="123456"
    )

    result = await UsuarioService().criar(usuario)
    assert result is not None