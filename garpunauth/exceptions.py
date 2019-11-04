class GarpunAuthError(Exception):
    """Base class for all google.auth errors."""


class TransportError(GarpunAuthError):
    """Used to indicate an error occurred during an HTTP request."""


class RefreshError(GarpunAuthError):
    """Used to indicate that an refreshing the credentials' access token
    failed."""


class DefaultCredentialsError(GarpunAuthError):
    """Used to indicate that acquiring default credentials failed."""
