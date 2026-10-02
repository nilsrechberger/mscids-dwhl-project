"""Test file for gtfs_rt.py"""

from src.loaders.gtfs_rt import fetch_gtfs_rt


def test_fetch_gtfs_rt() -> None:
    """Checks if gtfs_rf data is a dict"""

    result = fetch_gtfs_rt()

    assert isinstance(result, dict)
