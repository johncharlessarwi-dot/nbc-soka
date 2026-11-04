import pytest
from scraper.core.client import WPClient


def test_negative_throttle_delay_is_invalid():
    with pytest.raises(ValueError, match='min_delay_ms'):
        WPClient(base_url='https://example.org', user_agent='test', min_delay_ms=-1)
