from fastapi.testclient import TestClient
from api.app import create_app


def test_versioned_season_rejects_invalid_slug(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/seasons/not-a-season').status_code == 400

def test_raw_resource_rejects_dot_traversal(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/raw/..secret').status_code == 400

def test_raw_resource_rejects_uppercase(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/raw/EVENTS').status_code == 400

def test_raw_resource_valid_name_goes_to_data_lookup(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/raw/events').status_code == 404

def test_versioned_season_rejects_slashlike_slug(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/seasons/2026_27').status_code == 400

def test_versioned_season_valid_missing_returns_not_found(tmp_path):
    client = TestClient(create_app(data_dir=tmp_path))
    assert client.get('/api/v1/sources/ligikuu/seasons/2026-27').status_code == 404
