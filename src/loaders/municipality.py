"""Downloads the municipality file from BFS"""

import requests

from src.config import config


def fetch_municipality() -> requests.Response:
    """
    Downloads the static XLSX file from the BFS

    Args:
        None

    Returns:
        requests.Response: Response containing the XLSX file
    """
    response = requests.post(
        f"{config.MUNICIPALITY_XLSX}",
        timeout=10,
    )
    response.raise_for_status()
    return response
