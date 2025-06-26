from unittest.mock import AsyncMock, patch
import pytest
from app.schemas.vacina_schema import VacinaSchema
from app.services import vacina_service

@pytest.mark.asyncio
@patch("app.services.vacina_service.vacina_repository")
async def test_criar_vacina_unit(mock_repo):
    mock_repo.criar = AsyncMock(return_value="123")

    objeto = VacinaSchema(nome="Vacina")
    result = await vacina_service.criar(objeto)
    assert result is not None