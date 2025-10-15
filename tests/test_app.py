from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_readyz():
    r = client.get("/readyz")
    assert r.status_code == 200
    assert "ready" in r.json()

def test_version():
    r = client.get("/version")
    assert r.status_code == 200
    body = r.json()
    assert "service" in body and "version" in body

def test_sum_happy_path():
    r = client.post("/sum", json={"a": 1.5, "b": 2.5})
    assert r.status_code == 200
    assert r.json()["result"] == 4.0

def test_get_item_positive_id():
    r = client.get("/items/42")
    assert r.status_code == 200
    assert r.json()["id"] == 42

def test_get_item_negative_id():
    r = client.get("/items/-1")
    assert r.status_code == 400
    assert r.json()["detail"] == "item_id must be >= 0"
