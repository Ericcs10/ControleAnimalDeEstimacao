from unittest.mock import AsyncMock, patch
import pytest
from app.schemas.str import str
from app.services import especie_service

@pytest.mark.asyncio
@patch("app.services.especie_service.especie_repository")
async def test_criar_especie_unit(mock_repo):
    mock_repo.criar = AsyncMock(return_value="123")

    objeto = str(nome="Especie")
    result = await especie_service.criar(objeto)
    assert result is not None
