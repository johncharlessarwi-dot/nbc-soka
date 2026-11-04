import pytest
from scraper.core.client import WPClient


def test_cross_origin_urls_blocked():
    with WPClient(base_url='https://ligikuu.co.tz', user_agent='test') as client:
        with pytest.raises(ValueError, match='Cross-origin'):
            client.get_json('https://untrusted.example/private')


def test_scheme_downgrade_blocked():
    with WPClient(base_url='https://ligikuu.co.tz', user_agent='test') as client:
        with pytest.raises(ValueError):
            client.get_json('http://ligikuu.co.tz/data')
