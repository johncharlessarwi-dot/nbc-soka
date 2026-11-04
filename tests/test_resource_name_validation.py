from fastapi.testclient import TestClient
from api.app import create_app


def test_resource_name_guard_preserves_public_routes(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    # Valid known resource names still resolve to normal 404 when no data exists.
    for url in ('/teams', '/scores', '/table'):
        assert client.get(url).status_code == 404
