import pytest
from scraper.core.storage import DataStore


def test_datastore_rejects_bad_source_id(tmp_path):
    with pytest.raises(ValueError):
        DataStore(tmp_path, source_id='../outside')

def test_raw_filename_rejects_parent_directory(tmp_path):
    store = DataStore(tmp_path)
    with pytest.raises(ValueError):
        store.write_raw('../outside.json', {})

def test_normalized_filename_rejects_parent_directory(tmp_path):
    store = DataStore(tmp_path)
    with pytest.raises(ValueError):
        store.write_normalized('../outside.json', {})

def test_season_slug_rejects_traversal(tmp_path):
    store = DataStore(tmp_path)
    with pytest.raises(ValueError):
        store.write_season_bundle('..secret', {})

def test_safe_raw_filename_stores_payload(tmp_path):
    store = DataStore(tmp_path)
    path = store.write_raw('events.json', {'items': []})
    assert path.is_file()

def test_safe_normalized_filename_stores_payload(tmp_path):
    store = DataStore(tmp_path)
    path = store.write_normalized('tables.json', {'items': []})
    assert path.is_file()

def test_valid_season_bundle_is_written(tmp_path):
    store = DataStore(tmp_path)
    path = store.write_season_bundle('2026-27', {'season': '2026-27'})
    assert path.is_file()
