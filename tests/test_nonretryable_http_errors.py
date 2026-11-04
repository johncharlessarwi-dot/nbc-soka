from unittest.mock import Mock
import httpx
import pytest
from scraper.core.client import WPClient, FetchError


def test_http_404_is_not_retried():
    with WPClient(base_url='https://example.org', user_agent='test', min_delay_ms=0, max_retries=4) as client:
        request = httpx.Request('GET', 'https://example.org/missing')
        client._client.get = Mock(return_value=httpx.Response(404, text='Missing', request=request))
        with pytest.raises(FetchError):
            client.get_json('/missing')
        assert client._client.get.call_count == 1
