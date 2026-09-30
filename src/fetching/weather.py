""" Fetch historical weather data from Open-Meteo """

import openmeteo_requests

from openmeteo_sdk.WeatherApiResponse import WeatherApiResponse
import requests_cache
from retry_requests import retry

from src.config import config


def fetch_weather(url: str) -> list[WeatherApiResponse]:
    """ 
    Fetch data from Open-Meteo data API

    Args:
        url: API Endpoint

    Returns:
        list: Weather API Responses 
    """
    cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    params = {
        "latitude": 47.0002,
        "longitude": 8.0143,
        "start_date": "2026-09-14",
        "end_date": "2026-09-28",
        "hourly": "temperature_2m",
    }
    responses = openmeteo.weather_api(config.WEATHER_API_ENDPOINT, params=params)
    return responses
