def test_get_habits(client):
    response = client.get("/habits")
    assert response.status_code == 200
    assert response.json == []
