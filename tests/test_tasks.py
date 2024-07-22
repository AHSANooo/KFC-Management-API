# tests/test_tasks.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_place_order():
    client.post("/auth/register", json={"username": "user1", "password": "pass123"})
    token_response = client.post("/auth/token", data={"username": "user1", "password": "pass123"})
    token = token_response.json()["access_token"]

    response = client.post("/tasks/", json={"product_name": "burger", "quantity": 1},
                           headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"product_name": "burger", "quantity": 1}


def test_list_orders():
    client.post("/auth/register", json={"username": "user1", "password": "pass123"})
    token_response = client.post("/auth/token", data={"username": "user1", "password": "pass123"})
    token = token_response.json()["access_token"]

    client.post("/tasks/", json={"product_name": "burger", "quantity": 1}, headers={"Authorization": f"Bearer {token}"})
    response = client.get("/tasks/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == [{"product_name": "burger", "quantity": 1}]
