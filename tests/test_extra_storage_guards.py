import pytest
from scraper.core.storage import DataStore


def test_datastore_rejects_bad_source_id(tmp_path):
    with pytest.raises(ValueError):
        DataStore(tmp_path, source_id='../outside')
