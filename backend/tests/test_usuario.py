def test_crud_usuario_completo(client):
    usuario = {
        "email": "teste@example.com",
        "cpf": "12345678900",
        "telefone": "61999999999",
        "senha": "123456"
    }

    # Create
    response = client.post("/usuarios/", json=usuario)
    assert response.status_code == 201
    usuario_id = response.json()["id"]

    # Read (Get by ID)
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    assert response.json()["email"] == usuario["email"]

    # Update
    usuario_atualizado = usuario.copy()
    usuario_atualizado["telefone"] = "61988888888"
    response = client.put(f"/usuarios/{usuario_id}", json=usuario_atualizado)
    assert response.status_code == 200

    # Confirm update
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 200
    assert response.json()["telefone"] == "61988888888"

    # Delete
    response = client.delete(f"/usuarios/{usuario_id}")
    assert response.status_code == 200

    # Confirm delete
    response = client.get(f"/usuarios/{usuario_id}")
    assert response.status_code == 404
