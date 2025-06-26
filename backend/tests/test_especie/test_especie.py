def test_crud_especie_completo(client):
    data = {
        "nome": "Cão"
    }

    # Create
    response = client.post("/especies/", json=data)
    assert response.status_code == 201
    item_id = response.json()["id"]

    # Read
    response = client.get(f"/especies/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == data["nome"]

    # Update
    data_atualizada = data.copy()
    data_atualizada["nome"] = "Gato"
    response = client.put(f"/especies/{item_id}", json=data_atualizada)
    assert response.status_code == 200

    # Verify update
    response = client.get(f"/especies/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Gato"

    # Delete
    response = client.delete(f"/especies/{item_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/especies/{item_id}")
    assert response.status_code == 404
