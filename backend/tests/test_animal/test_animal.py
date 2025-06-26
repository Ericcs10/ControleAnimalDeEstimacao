def test_crud_animal_completo(client):
    data = {
        "nome": "Totó"
    }

    # Create
    response = client.post("/animais/", json=data)
    assert response.status_code == 201
    item_id = response.json()["id"]

    # Read
    response = client.get(f"/animais/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == data["nome"]

    # Update
    data_atualizada = data.copy()
    data_atualizada["nome"] = "Rex"
    response = client.put(f"/animais/{item_id}", json=data_atualizada)
    assert response.status_code == 200

    # Verify update
    response = client.get(f"/animais/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Rex"

    # Delete
    response = client.delete(f"/animais/{item_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/animais/{item_id}")
    assert response.status_code == 404
