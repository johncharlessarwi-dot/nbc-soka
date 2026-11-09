from scraper.core.season import (
    build_season_plan,
    classify_league,
    filter_items_by_season_or_league,
)


def test_classify_nbc_premier():
    assert classify_league("nbc-premier-league-2026-2027") == "nbc_premier"
    assert classify_league("nbc-championship-2025-2026") == "nbc_championship"


def test_build_season_plan_includes_2026_27():
    seasons = [
        {"id": 417, "slug": "2025-26", "name": "2025/26"},
        {"id": 431, "slug": "2026-27", "name": "2026/27"},
        {"id": 288, "slug": "2024-25", "name": "2024/25"},
        {"id": 235, "slug": "2023-24", "name": "2023/24"},
    ]
    leagues = [
        {
            "id": 432,
            "slug": "nbc-premier-league-2026-2027",
            "name": "NBC PREMIER LEAGUE 2026/2027",
        },
        {
            "id": 418,
            "slug": "nbc-premier-league-2025-2026",
            "name": "NBC PREMIER LEAGUE 2025/2026",
        },
        {
            "id": 419,
            "slug": "nbc-championship-2025-2026",
            "name": "NBC CHAMPIONSHIP LEAGUE 2025/2026",
        },
        {"id": 999, "slug": "some-other-cup", "name": "Other"},
    ]
    plan = build_season_plan(
        seasons=seasons,
        leagues=leagues,
        keep_recent_seasons=3,
        config_focus={"seasons": [{"id": 431, "slug": "2026-27"}]},
    )
    assert 431 in plan.active_season_ids
    assert 417 in plan.active_season_ids
    assert any(c.id == 432 for c in plan.competitions)
    assert all(c.kind != "other" for c in plan.competitions)


def test_filter_items_by_season():
    items = [
        {"id": 1, "seasons": [431], "leagues": [432]},
        {"id": 2, "seasons": [417], "leagues": [418]},
        {"id": 3, "seasons": [23], "leagues": [20]},
    ]
    out = filter_items_by_season_or_league(items, season_ids={431, 417}, league_ids=set())
    assert [i["id"] for i in out] == [1, 2]


def test_filter_skips_malformed_taxonomy_ids_without_dropping_valid_matches():
    items = [
        {"id": 1, "seasons": ["bad", None, 431, True], "leagues": []},
        {"id": 2, "seasons": {"unexpected": "shape"}, "leagues": ["432", "invalid"]},
        {"id": 3, "seasons": [False, -1, "not-a-number"], "leagues": [""]},
        {"id": 4, "seasons": ["bad"], "leagues": []},
    ]
    result = filter_items_by_season_or_league(items, season_ids={431}, league_ids={432})
    assert [item["id"] for item in result] == [1, 2]


def test_filter_rejects_boolean_taxonomy_id_collision():
    items = [{"id": 5, "seasons": [True], "leagues": [False]}]
    assert filter_items_by_season_or_league(items, season_ids={1}, league_ids={1}) == []


def test_season_plan_skips_malformed_upstream_taxonomy_ids():
    plan = build_season_plan(
        seasons=[{'id': 'bad', 'slug': '2026-27'}, {'id': True, 'slug': '2025-26'}, {'id': 431, 'slug': '2026-27'}],
        leagues=[{'id': None, 'slug': 'nbc-premier-league'}, {'id': 432, 'slug': 'nbc-premier-league-2026'}],
    )
    assert plan.active_season_ids == [431]
    assert [c.id for c in plan.competitions] == [432]
