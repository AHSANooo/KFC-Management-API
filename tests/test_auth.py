# tests/test_auth.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register():
    response = client.post("/auth/register", json={"username": "user1", "password": "pass123"})
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

def test_login():
    client.post("/auth/register", json={"username": "user1", "password": "pass123"})
    response = client.post("/auth/token", data={"username": "user1", "password": "pass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
