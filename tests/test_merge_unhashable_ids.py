from scraper.core.merge import merge_items_by_id


def test_unhashable_identifiers_do_not_abort_merge():
    existing = [{'id': [1], 'name': 'bad'}, {'id': 2, 'name': 'good'}]
    updates = [{'id': {'wrong': 3}}, {'id': 2, 'name': 'updated'}]
    assert merge_items_by_id(existing, updates) == [{'id': 2, 'name': 'updated'}]
