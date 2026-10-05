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


def test_chat_without_matching_products_returns_a_helpful_response():
    client = TestClient(app)
    response = client.post(
        "/api/chat",
        json={"message": "I need a desktop workstation under ₹10,000."},
    )

    assert response.status_code == 200
    assert "couldn't find a product" in response.json()["response"]


def test_products_endpoint_returns_catalog_details():
    client = TestClient(app)
    response = client.get("/api/products")

    assert response.status_code == 200
    products = response.json()
    assert products
    assert {"product_id", "name", "price", "category", "description"} <= products[0].keys()
