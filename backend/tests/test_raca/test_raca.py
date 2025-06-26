def test_crud_raca_completo(client):
    data = {
        "nome": "Labrador"
    }

    # Create
    response = client.post("/racas/", json=data)
    assert response.status_code == 201
    item_id = response.json()["id"]

    # Read
    response = client.get(f"/racas/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == data["nome"]

    # Update
    data_atualizada = data.copy()
    data_atualizada["nome"] = "Poodle"
    response = client.put(f"/racas/{item_id}", json=data_atualizada)
    assert response.status_code == 200

    # Verify update
    response = client.get(f"/racas/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Poodle"

    # Delete
    response = client.delete(f"/racas/{item_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/racas/{item_id}")
    assert response.status_code == 404