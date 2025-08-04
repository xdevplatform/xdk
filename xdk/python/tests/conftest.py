"""Test configuration and fixtures."""

import pytest
from unittest.mock import Mock
from xdk import Client


@pytest.fixture


def mock_client():
    """Provide a mock client for testing."""
    return Client(base_url="https://api.example.com")


@pytest.fixture


def mock_session():
    """Provide a mock session for HTTP requests."""
    return Mock()
