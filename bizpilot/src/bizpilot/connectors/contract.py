"""The shape every connector must deliver, whatever the source."""

from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


@dataclass(frozen=True, slots=True)
class SourceRecord:
    """One row or object exactly as the source gave it."""

    record_id: str
    source: str
    data: Mapping[str, object]

    def __post_init__(self) -> None:
        if not self.record_id:
            raise ValueError("record_id must not be empty")
        if not self.record_id.startswith(f"{self.source}:"):
            raise ValueError(f"record_id {self.record_id!r} must start with '{self.source}:'")


@dataclass(frozen=True, slots=True)
class SourceBatch:
    """One read from a source: when it happened, plus a lazy stream of records."""

    source: str
    retrieved_at: datetime
    records: Iterator[SourceRecord]

    def __post_init__(self) -> None:
        if self.retrieved_at.tzinfo is None:
            raise ValueError("retrieved_at must be timezone-aware")


class Connector(Protocol):
    """Anything with a name and a fetch method of this shape is a connector."""

    name: str

    def fetch(self, since: datetime | None = None) -> SourceBatch: ...
