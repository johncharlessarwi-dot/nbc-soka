import pytest
from scraper.core.client import WPClient


def test_client_rejects_non_http_url():
    with pytest.raises(ValueError, match='base URL'):
        WPClient(base_url='file:///etc', user_agent='test')

def test_client_rejects_url_credentials():
    with pytest.raises(ValueError):
        WPClient(base_url='https://user:pass@example.org', user_agent='test')

def test_client_rejects_zero_retries():
    with pytest.raises(ValueError):
        WPClient(base_url='https://example.org', user_agent='test', max_retries=0)
