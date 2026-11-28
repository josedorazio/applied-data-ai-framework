"""Errors a connector can raise. Callers catch SourceError for all of them."""


class SourceError(Exception):
    """Base for every connector error."""


class SourceAccessError(SourceError):
    """The source can't be reached or opened: missing file, network down, auth failed."""


class InvalidSourceDataError(SourceError):
    """The source was read, but its content doesn't have the expected shape."""


class UnsupportedFileError(SourceError):
    """The file type or format is not one the connector can read."""
