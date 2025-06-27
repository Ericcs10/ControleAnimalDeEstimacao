from unittest.mock import AsyncMock, patch
import pytest
from app.schemas.especie_schema import EspecieSchema
from app.services import especie_service

@pytest.mark.asyncio
@patch("app.services.especie_service.especie_repository")
async def test_criar_especie_unit(mock_repo):
    mock_repo.criar = AsyncMock(return_value="123")

    objeto = "Especie de Teste"
    result = await especie_service.criar(objeto)
    assert result is not None
