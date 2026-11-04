from scraper.utils.jsonio import read_json, write_json


def test_atomic_json_write_replaces_document(tmp_path):
    path = tmp_path / 'nested' / 'events.json'
    write_json(path, {'count': 1})
    write_json(path, {'count': 2})
    assert read_json(path) == {'count': 2}
    assert list(path.parent.iterdir()) == [path]
