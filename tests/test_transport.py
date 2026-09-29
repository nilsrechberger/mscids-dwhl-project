from unittest.mock import Mock, patch

from src.fetching.transport import fetch_locations


def test_fetch_locations_returns_json():
    fake_response = Mock()
    fake_response.json.return_value = {"stations": []}

    with patch("src.fetching.transport.requests.get", return_value=fake_response) as get:
        result = fetch_locations("Basel")

    assert result == {"stations": []}
    assert get.call_args.kwargs["params"] == {"query": "Basel"}
    fake_response.raise_for_status.assert_called_once()
