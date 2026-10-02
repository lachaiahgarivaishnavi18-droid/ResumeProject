from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_endpoint_smoke():
    client = TestClient(app)
    response = client.post(
        "/api/chat",
        json={"session_id": "session_001", "user_id": "user_001", "message": "I need a gaming laptop under ₹80,000."},
    )
    assert response.status_code == 200
    data = response.json()
    assert "workflow_id" in data
    assert "response" in data
