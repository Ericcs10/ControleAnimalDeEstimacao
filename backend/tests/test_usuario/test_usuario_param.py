import pytest

@pytest.mark.parametrize("cpf", ["", "123", "abcdef12345", "1234567890", "00000000000"])
def test_criar_usuario_com_cpf_invalido(client, cpf):
    usuario = {
        "email": "teste@example.com",
        "cpf": cpf,
        "telefone": "61999999999",
        "senha": "123456"
    }
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == 422