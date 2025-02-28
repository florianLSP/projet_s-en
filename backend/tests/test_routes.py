def test_get_habits(client):
    response = client.get("/habits")
    assert response.status_code == 200
    assert response.json == []


def test_post_habit_missing_name(client):
    response = client.post("/habits", json={})
    assert response.status_code == 400
    assert response.json == {"error": "le champ 'name' est requis"}


def test_create_new_habit(client):
    response = client.post(
        "/habits",
        json={
            "name": "habitude 1",
            "description": "description habitude",
            "habitLogs": [{"date": "2025-02-27"}],
            "creationDate": "2025-02-27",
        },
    )
    assert response.status_code == 201
    assert response.json["message"] == "Habitude ajoutée avec succès"
    assert response.json["habit"]["name"] == "habitude 1"
    assert response.json["habit"]["description"] == "description habitude"
    assert response.json["habit"]["creationDate"] is not None
    assert len(response.json["habit"]["habit_logs"]) == 1
    assert response.json["habit"]["habit_logs"][0]["date"].startswith(
        "Thu, 27 Feb 2025 00:00:00 GMT"
    )
