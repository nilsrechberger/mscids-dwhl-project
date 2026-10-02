"""Test file for storage.py and run.py"""

from datetime import datetime, timezone
from unittest.mock import MagicMock, patch

import pytest

from src.run import run
from src.storage import build_key, write_raw


def test_build_key() -> None:
    """Checks the partitioned key layout"""
    now = datetime(2026, 10, 2, 10, 15, 30, tzinfo=timezone.utc)

    assert build_key("weather", "json", now) == "raw/weather/dt=2026-10-02/101530.json"


def test_write_raw() -> None:
    """Checks that the object is put into the configured bucket"""
    client = MagicMock()
    with patch("src.storage.boto3.client", return_value=client), patch(
        "src.storage.config.S3_BUCKET", "my-bucket"
    ):
        uri = write_raw("transport", b"{}", "json")

    kwargs = client.put_object.call_args.kwargs
    assert kwargs["Bucket"] == "my-bucket"
    assert kwargs["Body"] == b"{}"
    assert uri == f"s3://my-bucket/{kwargs['Key']}"


def test_write_raw_without_bucket() -> None:
    """Fails fast if no bucket is configured"""
    with patch("src.storage.config.S3_BUCKET", None):
        with pytest.raises(RuntimeError):
            write_raw("transport", b"{}", "json")


def test_run_unknown_source() -> None:
    """Rejects unknown source names"""
    with pytest.raises(ValueError):
        run("nope")
