from fastapi.testclient import TestClient
from api.app import create_app


def test_invalid_season_slug_rejected(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    response = client.get('/seasons/..evil')
    assert response.status_code == 400


def test_valid_slug_still_uses_data_lookup(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    response = client.get('/seasons/2026-27')
    assert response.status_code == 404
