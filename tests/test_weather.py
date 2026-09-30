"""Test file for transport.py"""

from src.config import config
from src.fetching.weather import fetch_weather


def test_fetch_location() -> None:
    """Checks if gtfs_rf data is a dict"""
    
    assert config.WEATHER_API_ENDPOINT is not None

    result = fetch_weather(url=config.WEATHER_API_ENDPOINT)

    assert isinstance(result, list)
