from fastapi.testclient import TestClient
from api.app import create_app


def test_versioned_season_rejects_invalid_slug(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/seasons/not-a-season').status_code == 400
