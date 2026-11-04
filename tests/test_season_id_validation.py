from api.app import _season_id_for_slug


def test_invalid_season_identifier_is_skipped():
    payload = {'items': [{'slug': '2026-27', 'id': 'invalid'}, {'slug': '2026-27', 'id': 431}]}
    assert _season_id_for_slug(payload, '2026-27') == 431


def test_missing_identifier_returns_none():
    assert _season_id_for_slug({'items': [{'slug': '2025-26'}]}, '2025-26') is None
