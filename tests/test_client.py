from scraper.core.client import FetchError, WPClient


def test_describe_payload_dict():
    text = WPClient._describe_payload({"code": "rest_no_route", "message": "No route"})
    assert "rest_no_route" in text
    assert "No route" in text


def test_fetch_error_retryable_flag():
    err = FetchError("boom")
    assert err.retryable is True


def test_base_url_rejects_embedded_query_parameters():
    import pytest

    with pytest.raises(ValueError, match="Invalid scraper base URL"):
        WPClient(base_url="https://example.com/wp-json?token=secret", user_agent="nbc-soka-test")


def test_base_url_rejects_fragment_that_misroutes_requests():
    import pytest

    with pytest.raises(ValueError, match="Invalid scraper base URL"):
        WPClient(base_url="https://example.com/wp-json#ignored-path", user_agent="nbc-soka-test")


def test_boolean_retry_count_is_rejected():
    import pytest

    with pytest.raises(ValueError, match="max_retries"):
        WPClient(base_url="https://example.com/wp-json", user_agent="nbc-soka-test", max_retries=True)


def test_boolean_throttle_delay_is_rejected():
    import pytest

    with pytest.raises(ValueError, match='min_delay_ms'):
        WPClient(base_url='https://example.com', user_agent='nbc-soka-test', min_delay_ms=False)


def test_fractional_page_size_is_rejected():
    import pytest

    with WPClient(base_url='https://example.com', user_agent='nbc-soka-test') as client:
        with pytest.raises(ValueError, match='per_page'):
            client.paginate('/events', per_page=2.5)


def test_boolean_max_pages_is_rejected():
    import pytest

    with WPClient(base_url='https://example.com', user_agent='nbc-soka-test') as client:
        with pytest.raises(ValueError, match='max_pages'):
            client.paginate('/events', max_pages=True)


def test_json_response_size_limit_rejects_oversized_content_length():
    import httpx
    import pytest

    def respond(request):
        return httpx.Response(200, headers={'Content-Length': '30000000', 'Content-Type': 'application/json'}, content=b'{}')

    with WPClient(base_url='https://example.com', user_agent='nbc-soka-test', max_retries=1) as client:
        client._client.close()
        client._client = httpx.Client(transport=httpx.MockTransport(respond))
        with pytest.raises(FetchError, match='size limit'):
            client.get_json('/events')
