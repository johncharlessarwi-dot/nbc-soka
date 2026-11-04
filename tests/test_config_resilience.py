from scraper.core.config import enabled_resources


def test_malformed_resource_config_does_not_crash():
    config = {'sportspress': {'resources': [None, 'bad', {'name': 'teams', 'priority': 'wrong'}, {'name': 'events', 'priority': 1}]}}
    assert [r['name'] for r in enabled_resources(config)] == ['events', 'teams']
