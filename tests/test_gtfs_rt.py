from unittest.mock import Mock, patch

from src.fetching.gtfs_rt import fetch_gtfd_rt


def test_fetch_gtfd_rt_returns_json():
    fake_response = Mock()
    fake_response.json.return_value = {"stations": []}

    with patch("src.fetching.transport.requests.get", return_value=fake_response) as get:
        result = fetch_gtfd_rt()

    assert result == {"stations": []}
    fake_response.raise_for_status.assert_called_once()
