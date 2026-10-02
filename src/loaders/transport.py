"""Fetch Transport data from Swiss public transport API"""

import requests

from src.config import config


def fetch_locations(query: str = "Basel") -> dict:
    """
    Fetch transport data by location

    Args:
        location: Specifies the location name to search for

    Returns:
        dict: API response
    """
    response = requests.get(
        f"{config.TRANSPORT_API_ENDPOINT}/locations",
        params={"query": query},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
