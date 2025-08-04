"""
Auto-generated contract tests for Communities client.

This module contains tests that validate the request/response contracts
of the Communities client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.communities.client import CommunitiesClient
from xdk import Client


class TestCommunitiesContracts:
    """Test the API contracts of CommunitiesClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.communities_client = getattr(self.client, "communities")

    def test_search_communities_request_structure(self):
        """Test searchCommunities request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["query"] = "test_query"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.communities_client, "search_communities")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/communities/search"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for searchCommunities: {e}")

    def test_search_communities_required_parameters(self):
        """Test that searchCommunities requires necessary parameters."""
        method = getattr(self.communities_client, "search_communities")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_search_communities_response_structure(self):
        """Test searchCommunities response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["query"] = "test_value"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.communities_client, "search_communities")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_communities_by_id_request_structure(self):
        """Test getCommunitiesById request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.communities_client, "get_communities_by_id")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/communities/{id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getCommunitiesById: {e}")

    def test_get_communities_by_id_required_parameters(self):
        """Test that getCommunitiesById requires necessary parameters."""
        method = getattr(self.communities_client, "get_communities_by_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_communities_by_id_response_structure(self):
        """Test getCommunitiesById response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.communities_client, "get_communities_by_id")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_error_responses(self):
        """Test that error responses are handled correctly."""

        with patch.object(self.client, "session") as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response

            # Pick first available method for testing

            method = getattr(self.communities_client, "search_communities")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["query"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.communities_client, "get_communities_by_id")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)
