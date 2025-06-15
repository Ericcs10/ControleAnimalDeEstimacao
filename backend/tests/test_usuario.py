from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_crud_usuario_completo():
    usuario = {
        "email": "teste@example.com",
        "cpf": "12345678900",
        "telefone": "61999999999",
        "senha": "123456"
    }

    # 🔸 Create
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == 201
    usuario_id = response.json()["id"]

    # 🔸 Read
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == usuario["email"]
    assert data["cpf"] == usuario["cpf"]

    # 🔸 Update
    updated_data = {
        "email": "atualizado@example.com",
        "cpf": "12345678900",
        "telefone": "61988888888",
        "senha": "654321"
    }
    response = client.put(f"/usuarios/{usuario_id}", json=updated_data)
    assert response.status_code == 200

    # 🔸 Read after Update
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == updated_data["email"]
    assert data["telefone"] == updated_data["telefone"]

    # 🔸 Delete
    response = client.delete(f"/usuarios/{usuario_id}")
    assert response.status_code == 200

    # 🔸 Confirm Delete
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 404
