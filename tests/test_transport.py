"""Test file for transport.py"""

from src.loaders.transport import fetch_locations


def test_fetch_location() -> None:
    """Checks if gtfs_rf data is a dict"""

    result = fetch_locations(query="Bern")

    assert isinstance(result, dict)
