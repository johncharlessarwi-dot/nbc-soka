from scraper.core.config import http_settings


def test_malformed_http_settings_default_to_empty():
    assert http_settings({'http': ['unexpected']}) == {}
    assert http_settings({'http': 42}) == {}
    assert http_settings({'http': {'timeout_seconds': 5}}) == {'timeout_seconds': 5}
