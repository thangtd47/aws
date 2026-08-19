from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_list_item():
    res = client.post("/items", params={"name": "Book"})
    assert res.status_code == 200
    assert res.json()["name"] == "Book"

    res = client.get("/items")
    assert res.status_code == 200
    assert any(i["name"] == "Book" for i in res.json())