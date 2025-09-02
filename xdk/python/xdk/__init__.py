"""
XDK Python SDK.

A Python SDK for the X API that provides convenient access
to the X API endpoints with type safety and authentication support.

Generated automatically - do not edit manually.
"""

from .client import Client
from .paginator import Cursor, cursor, PaginationError

__version__ = "0.1.0"
__all__ = ["Client", "Cursor", "cursor", "PaginationError"]
