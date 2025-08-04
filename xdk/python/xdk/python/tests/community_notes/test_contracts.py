"""
Auto-generated contract tests for Community_Notes client.

This module contains tests that validate the request/response contracts
of the Community_Notes client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.community_notes.client import CommunityNotesClient
from xdk import Client


class TestCommunityNotesContracts:
    """Test the API contracts of CommunityNotesClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.community_notes_client = getattr(self.client, "community_notes")

    def test_error_responses(self):
        """Test that error responses are handled correctly."""
        with patch.object(self.client, "session") as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response

            # Pick first available method for testing
