from unittest.mock import AsyncMock, patch
import pytest
from app.schemas.animal_schema import AnimalSchema
from app.services import animal_service

@pytest.mark.asyncio
@patch("app.services.animal_service.animal_repository")
async def test_criar_animal_unit(mock_repo):
    mock_repo.criar = AsyncMock(return_value="123")

    objeto = AnimalSchema(nome="Animal")
    result = await animal_service.criar(objeto)
    assert result is not None
