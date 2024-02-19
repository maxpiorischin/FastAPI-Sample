from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the root of the app."}


def test_sample():
    response = client.get("/sample")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a sample function"}
