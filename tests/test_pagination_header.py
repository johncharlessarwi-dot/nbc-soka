from unittest.mock import Mock
import httpx
from scraper.core.client import WPClient


def test_malformed_total_pages_header_stops_safely():
    with WPClient(base_url='https://example.org', user_agent='test', min_delay_ms=0) as client:
        client.get_json = Mock(return_value=([{'id': 1}], httpx.Headers({'X-WP-TotalPages': 'n/a'})))
        rows = client.paginate('/events')
        assert rows == [{'id': 1}]
        assert client.get_json.call_count == 1
