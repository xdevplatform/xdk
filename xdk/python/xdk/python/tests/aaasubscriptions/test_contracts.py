"""
Auto-generated contract tests for AAASubscriptions client.

This module contains tests that validate the request/response contracts
of the AAASubscriptions client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.aaasubscriptions.client import AaasubscriptionsClient
from xdk import Client


class TestAaasubscriptionsContracts:
    """Test the API contracts of AaasubscriptionsClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.aaasubscriptions_client = getattr(self.client, "aaasubscriptions")


    def test_create_account_activity_subscription_request_structure(self):
        """Test create_account_activity_subscription request structure."""
        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response
            # Prepare test parameters
            kwargs = {}
            # Add required parameters
            kwargs["webhook_id"] = "test_value"
            # Add request body if required
            # Import and create proper request model instance
            from xdk.aaasubscriptions.models import (
                CreateaccountactivitysubscriptionRequest,
            )
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateaccountactivitysubscriptionRequest()
            # Call the method
            try:
                method = getattr(
                    self.aaasubscriptions_client, "create_account_activity_subscription"
                )
                result = method(**kwargs)
                # Verify the request was made
                mock_session.post.assert_called_once()
                # Verify request structure
                call_args = mock_session.post.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = (
                    "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"
                )
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(
                    f"Contract test failed for create_account_activity_subscription: {e}"
                )


    def test_create_account_activity_subscription_required_parameters(self):
        """Test that create_account_activity_subscription handles parameters correctly."""
        method = getattr(
            self.aaasubscriptions_client, "create_account_activity_subscription"
        )
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.post.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_create_account_activity_subscription_response_structure(self):
        """Test create_account_activity_subscription response structure validation."""
        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response
            # Prepare minimal valid parameters
            kwargs = {}
            kwargs["webhook_id"] = "test"
            # Add request body if required
            # Import and create proper request model instance
            from xdk.aaasubscriptions.models import (
                CreateaccountactivitysubscriptionRequest,
            )
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateaccountactivitysubscriptionRequest()
            # Call method and verify response structure
            method = getattr(
                self.aaasubscriptions_client, "create_account_activity_subscription"
            )
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
