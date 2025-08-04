"""
Auto-generated contract tests for Account_Activity client.

This module contains tests that validate the request/response contracts
of the Account_Activity client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.account_activity.client import AccountActivityClient
from xdk import Client


class TestAccountActivityContracts:
    """Test the API contracts of AccountActivityClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.account_activity_client = getattr(self.client, "account_activity")

    def test_error_responses(self):
        """Test that error responses are handled correctly."""
        with patch.object(self.client, "session") as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response

            # Pick first available method for testing
