from unittest.mock import AsyncMock, patch
import pytest
from app.schemas.raca_schema import RacaSchema
from app.services import raca_service

@pytest.mark.asyncio
@patch("app.services.raca_service.raca_repository")
async def test_criar_raca_unit(mock_repo):
    mock_repo.criar = AsyncMock(return_value="123")

    objeto = RacaSchema(nome="Raca")
    result = await raca_service.criar(objeto)
    assert result is not None