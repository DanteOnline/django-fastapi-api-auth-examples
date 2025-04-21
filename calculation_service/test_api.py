from fastapi.testclient import TestClient
import pytest
from api import app


@pytest.fixture
def client():
    return TestClient(app)


def test_random_expression_api_view(client):
    response = client.get("/api/random-expression/")
    assert response.status_code == 200
    data = response.json()
    assert "expression" in data
    assert isinstance(data["expression"], str)


def test_calculate_api_view(client):
    response = client.post("/api/calculate/", json={"expression": "2 + 3 * 4"})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert isinstance(data["result"], (int, float))
    assert data["result"] == 14
