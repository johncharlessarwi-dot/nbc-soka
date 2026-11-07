import pytest
from scraper.core.client import WPClient


def test_client_rejects_non_http_url():
    with pytest.raises(ValueError, match='base URL'):
        WPClient(base_url='file:///etc', user_agent='test')
