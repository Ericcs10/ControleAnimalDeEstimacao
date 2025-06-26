import pytest

@pytest.mark.parametrize("nome", ["", "a", "1234567890123456789012345678901234567890"])
def test_criar_animal_com_nome_invalido(client, nome):
    data = {
        "nome": nome
    }
    response = client.post("/animais/", json=data)
    assert response.status_code in [400, 422]