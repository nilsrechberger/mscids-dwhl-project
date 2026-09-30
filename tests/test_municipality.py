"""Test file for municipality.py"""

from src.fetching.municipality import fetch_municipality


def test_fetch_municipality() -> None:
    """Tests if municipality is a binary file"""

    result = fetch_municipality()

    assert isinstance(result.content, bytes)
