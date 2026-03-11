from fastapi.testclient import TestClient
from App.Main import app

client = TestClient(app)

def test_create_short_url():

    response = client.post(
        "/shorten",
        json={"url": "https://example.com"}
    )

    assert response.status_code == 200
    assert "short_id" in response.json()

def test_stats():

    create = client.post(
        "/shorten",
        json={"url": "https://example.com"}
    )

    short_id = create.json()["short_id"]

    stats = client.get(f"/stats/{short_id}")

    assert stats.status_code == 200
    assert stats.json()["clicks"] == 0
