from app import create_app

def test_health_endpoint(monkeypatch):
    app = create_app()
    client=app.test_client()
    response=client.get("/health")
    assert response.status_code in [200,503]
