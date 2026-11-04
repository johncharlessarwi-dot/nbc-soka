import pytest
from scraper.core.client import WPClient


def test_pagination_bounds_fail_before_network():
    with WPClient(base_url='https://example.org', user_agent='test') as client:
        with pytest.raises(ValueError):
            client.paginate('/events', per_page=0)
        with pytest.raises(ValueError):
            client.paginate('/events', per_page=101)
        with pytest.raises(ValueError):
            client.paginate('/events', max_pages=0)
