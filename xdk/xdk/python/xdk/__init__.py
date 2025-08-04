"""
XDK Python SDK.

A Python SDK for the X API.
"""

from .client import Client
from .paginator import Cursor, cursor, PaginationError

__version__ = "0.1.0"
__all__ = ["Client", "Cursor", "cursor", "PaginationError"] 