""" Downloads the  """

import requests
import json

from src.config import config

def fetch_municipality() -> dict:
    response = requests.post(
        f"{config.MUNICIPALITY_XLSX}",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
