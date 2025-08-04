"""
Auto-generated contract tests for Likes client.

This module contains tests that validate the request/response contracts
of the Likes client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.likes.client import LikesClient
from xdk import Client


class TestLikesContracts:
    """Test the API contracts of LikesClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.likes_client = getattr(self.client, "likes")


    def test_stream_likes_firehose_request_structure(self):
        """Test stream_likes_firehose request structure."""
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
            kwargs["partition"] = 42
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.likes_client, "stream_likes_firehose")
                result = method(**kwargs)
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/likes/firehose/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for stream_likes_firehose: {e}")


    def test_stream_likes_firehose_required_parameters(self):
        """Test that stream_likes_firehose handles parameters correctly."""
        method = getattr(self.likes_client, "stream_likes_firehose")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.get.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_stream_likes_firehose_response_structure(self):
        """Test stream_likes_firehose response structure validation."""
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
            kwargs["partition"] = 1
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.likes_client, "stream_likes_firehose")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_stream_likes_sample10_request_structure(self):
        """Test stream_likes_sample10 request structure."""
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
            kwargs["partition"] = 42
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.likes_client, "stream_likes_sample10")
                result = method(**kwargs)
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/likes/sample10/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for stream_likes_sample10: {e}")


    def test_stream_likes_sample10_required_parameters(self):
        """Test that stream_likes_sample10 handles parameters correctly."""
        method = getattr(self.likes_client, "stream_likes_sample10")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.get.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_stream_likes_sample10_response_structure(self):
        """Test stream_likes_sample10 response structure validation."""
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
            kwargs["partition"] = 1
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.likes_client, "stream_likes_sample10")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
