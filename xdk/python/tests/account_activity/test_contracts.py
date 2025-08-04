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

    def test_delete_account_activity_subscription_request_structure(self):
        """Test deleteAccountActivitySubscription request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.delete.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["webhook_id"] = "test_value"

            kwargs["user_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.account_activity_client, "delete_account_activity_subscription"
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(
                    f"Contract test failed for deleteAccountActivitySubscription: {e}"
                )

    def test_delete_account_activity_subscription_required_parameters(self):
        """Test that deleteAccountActivitySubscription requires necessary parameters."""
        method = getattr(
            self.account_activity_client, "delete_account_activity_subscription"
        )

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_delete_account_activity_subscription_response_structure(self):
        """Test deleteAccountActivitySubscription response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.delete.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["webhook_id"] = "test"

            kwargs["user_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.account_activity_client, "delete_account_activity_subscription"
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

    def test_create_account_activity_replay_job_request_structure(self):
        """Test createAccountActivityReplayJob request structure."""

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

            kwargs["from_date"] = "test_from_date"

            kwargs["to_date"] = "test_to_date"

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.account_activity_client, "create_account_activity_replay_job"
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
                    "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all"
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
                    f"Contract test failed for createAccountActivityReplayJob: {e}"
                )

    def test_create_account_activity_replay_job_required_parameters(self):
        """Test that createAccountActivityReplayJob requires necessary parameters."""
        method = getattr(
            self.account_activity_client, "create_account_activity_replay_job"
        )

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_create_account_activity_replay_job_response_structure(self):
        """Test createAccountActivityReplayJob response structure validation."""

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

            kwargs["from_date"] = "test_value"

            kwargs["to_date"] = "test_value"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.account_activity_client, "create_account_activity_replay_job"
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

    def test_get_account_activity_subscriptions_request_structure(self):
        """Test getAccountActivitySubscriptions request structure."""

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

            kwargs["webhook_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.account_activity_client, "get_account_activity_subscriptions"
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = (
                    "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list"
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
                    f"Contract test failed for getAccountActivitySubscriptions: {e}"
                )

    def test_get_account_activity_subscriptions_required_parameters(self):
        """Test that getAccountActivitySubscriptions requires necessary parameters."""
        method = getattr(
            self.account_activity_client, "get_account_activity_subscriptions"
        )

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_account_activity_subscriptions_response_structure(self):
        """Test getAccountActivitySubscriptions response structure validation."""

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

            kwargs["webhook_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.account_activity_client, "get_account_activity_subscriptions"
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

    def test_get_account_activity_subscription_count_request_structure(self):
        """Test getAccountActivitySubscriptionCount request structure."""

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

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.account_activity_client,
                    "get_account_activity_subscription_count",
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/account_activity/subscriptions/count"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(
                    f"Contract test failed for getAccountActivitySubscriptionCount: {e}"
                )

    def test_get_account_activity_subscription_count_required_parameters(self):
        """Test that getAccountActivitySubscriptionCount requires necessary parameters."""
        method = getattr(
            self.account_activity_client, "get_account_activity_subscription_count"
        )

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

    def test_get_account_activity_subscription_count_response_structure(self):
        """Test getAccountActivitySubscriptionCount response structure validation."""

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

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.account_activity_client, "get_account_activity_subscription_count"
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

    def test_validate_account_activity_subscription_request_structure(self):
        """Test validateAccountActivitySubscription request structure."""

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

            kwargs["webhook_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.account_activity_client,
                    "validate_account_activity_subscription",
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

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
                    f"Contract test failed for validateAccountActivitySubscription: {e}"
                )

    def test_validate_account_activity_subscription_required_parameters(self):
        """Test that validateAccountActivitySubscription requires necessary parameters."""
        method = getattr(
            self.account_activity_client, "validate_account_activity_subscription"
        )

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_validate_account_activity_subscription_response_structure(self):
        """Test validateAccountActivitySubscription response structure validation."""

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

            kwargs["webhook_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.account_activity_client, "validate_account_activity_subscription"
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

    def test_error_responses(self):
        """Test that error responses are handled correctly."""

        with patch.object(self.client, "session") as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response

            # Pick first available method for testing

            method = getattr(
                self.account_activity_client, "delete_account_activity_subscription"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["webhook_id"] = "test"

                kwargs["user_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(
                self.account_activity_client, "create_account_activity_replay_job"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["webhook_id"] = "test"

                kwargs["from_date"] = "test"

                kwargs["to_date"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(
                self.account_activity_client, "get_account_activity_subscriptions"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["webhook_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(
                self.account_activity_client, "get_account_activity_subscription_count"
            )

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(
                self.account_activity_client, "validate_account_activity_subscription"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["webhook_id"] = "test"

                # Add request body if required

                method(**kwargs)
