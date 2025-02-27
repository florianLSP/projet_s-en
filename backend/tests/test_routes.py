def test_get_habits(client):
    response = client.get("/habits")
    assert response.status_code == 200
    assert response.json == []


def test_post_habit_missing_name(client):
    response = client.post("/habits", json={})
    assert response.status_code == 400
    assert response.json == {"error": "le champ 'name' est requis"}
