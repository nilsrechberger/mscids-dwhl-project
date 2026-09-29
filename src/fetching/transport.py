import requests
import json

from src.config import config


def fetch_locations(query: str = "Basel") -> dict:
    response = requests.get(
        f"{config.TRANSPORT_API_ENDPOINT_}/locations",
        params={"query": query},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
