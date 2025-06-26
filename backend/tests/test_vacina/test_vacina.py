def test_crud_vacina_completo(client):
    data = {
        "nome": "Raiva"
    }

    # Create
    response = client.post("/vacinas/", json=data)
    assert response.status_code == 201
    item_id = response.json()["id"]

    # Read
    response = client.get(f"/vacinas/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == data["nome"]

    # Update
    data_atualizada = data.copy()
    data_atualizada["nome"] = "Antirrábica"
    response = client.put(f"/vacinas/{item_id}", json=data_atualizada)
    assert response.status_code == 200

    # Verify update
    response = client.get(f"/vacinas/{item_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Antirrábica"

    # Delete
    response = client.delete(f"/vacinas/{item_id}")
    assert response.status_code == 200

    # Verify deletion
    response = client.get(f"/vacinas/{item_id}")
    assert response.status_code == 404
