import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ENDPOINT_TRANSPORT = os.getenv('TRANSPORT_API_ENDPOINT')
    GTFS_RT_API_ENDPOINT = os.getenv('GTFS_RT_API_ENDPOINT')
    GTFS_RT_TOKEN_HASH = os.getenv('GTFS_RT_TOKEN_HASH')
    MUNICIPALITY_XLSX = os.getenv('MUNICIPALITY_XLSX')

config = Config()
