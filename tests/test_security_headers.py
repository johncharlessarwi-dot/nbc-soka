from fastapi.testclient import TestClient
from api.app import create_app


def test_api_security_headers_on_public_health(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    response = client.get('/health')
    assert response.headers['x-content-type-options'] == 'nosniff'
    assert response.headers['referrer-policy'] == 'no-referrer'
