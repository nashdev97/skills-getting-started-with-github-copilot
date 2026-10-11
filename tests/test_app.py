from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_signup_and_unregister_participant():
    activity_name = "Chess Club"
    email = "student@example.com"

    signup_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200
    assert email in signup_response.json()["message"]

    unregister_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    assert unregister_response.status_code == 200
    assert "unregistered" in unregister_response.json()["message"].lower()

    get_response = client.get("/activities")
    activities = get_response.json()
    assert email not in activities[activity_name]["participants"]
