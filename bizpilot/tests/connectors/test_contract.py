from dataclasses import FrozenInstanceError
from datetime import UTC, datetime

import pytest

from bizpilot.connectors.contract import SourceBatch, SourceRecord
from bizpilot.connectors.errors import (
    InvalidSourceDataError,
    SourceAccessError,
    SourceError,
    UnsupportedFileError,
)


def test_record_keeps_the_values_it_was_given() -> None:
    record = SourceRecord(record_id="olist:orders:abc", source="olist", data={"order_id": "abc"})

    assert record.record_id == "olist:orders:abc"
    assert record.data["order_id"] == "abc"


def test_record_rejects_an_empty_record_id() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        SourceRecord(record_id="", source="olist", data={})


def test_record_id_must_start_with_the_source() -> None:
    with pytest.raises(ValueError, match="must start with 'olist:'"):
        SourceRecord(record_id="orders:abc", source="olist", data={})


def test_record_cannot_be_changed_after_creation() -> None:
    record = SourceRecord(record_id="olist:orders:abc", source="olist", data={})

    with pytest.raises(FrozenInstanceError):
        record.source = "stripe"  # type: ignore[misc]


def test_batch_requires_a_timezone() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        SourceBatch(source="olist", retrieved_at=datetime.now(), records=iter([]))


def test_batch_streams_its_records() -> None:
    record = SourceRecord(record_id="olist:orders:abc", source="olist", data={})
    batch = SourceBatch(source="olist", retrieved_at=datetime.now(UTC), records=iter([record]))

    assert list(batch.records) == [record]


@pytest.mark.parametrize("error", [SourceAccessError, InvalidSourceDataError, UnsupportedFileError])
def test_every_connector_error_is_a_source_error(error: type[Exception]) -> None:
    assert issubclass(error, SourceError)
