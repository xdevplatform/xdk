"""
Auto-generated contract tests for General client.

This module contains tests that validate the request/response contracts
of the General client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.general.client import GeneralClient
from xdk import Client


class TestGeneralContracts:
    """Test the API contracts of GeneralClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.general_client = getattr(self.client, "general")

    def test_get_open_api_spec_request_structure(self):
        """Test getOpenApiSpec request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.general_client, "get_open_api_spec")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/openapi.json"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getOpenApiSpec: {e}")

    def test_get_open_api_spec_required_parameters(self):
        """Test that getOpenApiSpec requires necessary parameters."""
        method = getattr(self.general_client, "get_open_api_spec")

        # Test with missing required parameters should fail

        # No required parameters, method should be callable without args
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            try:
                method()
            except Exception as e:
                pytest.fail(f"Method with no required params should be callable: {e}")

    def test_get_open_api_spec_response_structure(self):
        """Test getOpenApiSpec response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {}

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.general_client, "get_open_api_spec")
            result = method(**kwargs)

            # Verify response object has expected attributes

    def test_error_responses(self):
        """Test that error responses are handled correctly."""

        with patch.object(self.client, "session") as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response

            # Pick first available method for testing

            method = getattr(self.general_client, "get_open_api_spec")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)
