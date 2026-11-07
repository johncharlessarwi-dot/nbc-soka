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

def test_client_rejects_excessive_retries():
    with pytest.raises(ValueError):
        WPClient(base_url='https://example.org', user_agent='test', max_retries=11)

def test_client_rejects_float_retry_count():
    with pytest.raises(ValueError):
        WPClient(base_url='https://example.org', user_agent='test', max_retries=1.2)

def test_client_rejects_infinite_timeout():
    with pytest.raises(ValueError):
        WPClient(base_url='https://example.org', user_agent='test', timeout_seconds=float('inf'))

def test_client_rejects_excessive_timeout():
    with pytest.raises(ValueError):
        WPClient(base_url='https://example.org', user_agent='test', timeout_seconds=121)

def test_client_rejects_excessive_throttle():
    with pytest.raises(ValueError):
        WPClient(base_url='https://example.org', user_agent='test', min_delay_ms=60001)

def test_client_rejects_invalid_start_page():
    with WPClient(base_url='https://example.org', user_agent='test') as client:
        with pytest.raises(ValueError):
            client.paginate('/events', params={'page': -1})

def test_client_rejects_excessive_page_limit():
    with WPClient(base_url='https://example.org', user_agent='test') as client:
        with pytest.raises(ValueError):
            client.paginate('/events', max_pages=100001)
