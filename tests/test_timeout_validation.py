import pytest
from scraper.core.client import WPClient


def test_nonpositive_timeout_rejected():
    with pytest.raises(ValueError, match='timeout_seconds'):
        WPClient(base_url='https://example.org', user_agent='test', timeout_seconds=0)
