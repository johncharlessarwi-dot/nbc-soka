from api.app import _season_id_for_slug


def test_non_object_source_records_do_not_crash_lookup():
    payload = {'items': [None, 'bad', 7, {'slug': '2026-27', 'id': 431}]}
    assert _season_id_for_slug(payload, '2026-27') == 431
