"""
Auto-generated contract tests for Users client.

This module contains tests that validate the request/response contracts
of the Users client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.users.client import UsersClient
from xdk import Client


class TestUsersContracts:
    """Test the API contracts of UsersClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.users_client = getattr(self.client, "users")

    def test_search_users_request_structure(self):
        """Test searchUsers request structure."""

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

            kwargs["query"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "search_users")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/search"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for searchUsers: {e}")

    def test_search_users_required_parameters(self):
        """Test that searchUsers requires necessary parameters."""
        method = getattr(self.users_client, "search_users")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_search_users_response_structure(self):
        """Test searchUsers response structure validation."""

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

            kwargs["query"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "search_users")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_by_usernames_request_structure(self):
        """Test getUsersByUsernames request structure."""

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

            kwargs["usernames"] = ["test_item"]

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "get_users_by_usernames")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/by"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersByUsernames: {e}")

    def test_get_users_by_usernames_required_parameters(self):
        """Test that getUsersByUsernames requires necessary parameters."""
        method = getattr(self.users_client, "get_users_by_usernames")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_by_usernames_response_structure(self):
        """Test getUsersByUsernames response structure validation."""

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

            kwargs["usernames"] = ["test"]

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "get_users_by_usernames")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_blocking_request_structure(self):
        """Test getUsersBlocking request structure."""

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
                method = getattr(self.users_client, "get_users_blocking")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/blocking"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersBlocking: {e}")

    def test_get_users_blocking_required_parameters(self):
        """Test that getUsersBlocking requires necessary parameters."""
        method = getattr(self.users_client, "get_users_blocking")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_blocking_response_structure(self):
        """Test getUsersBlocking response structure validation."""

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
            method = getattr(self.users_client, "get_users_blocking")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_unmute_user_request_structure(self):
        """Test unmuteUser request structure."""

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

            kwargs["source_user_id"] = "test_value"

            kwargs["target_user_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "unmute_user")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{source_user_id}/muting/{target_user_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for unmuteUser: {e}")

    def test_unmute_user_required_parameters(self):
        """Test that unmuteUser requires necessary parameters."""
        method = getattr(self.users_client, "unmute_user")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_unmute_user_response_structure(self):
        """Test unmuteUser response structure validation."""

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

            kwargs["source_user_id"] = "test"

            kwargs["target_user_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "unmute_user")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_my_user_request_structure(self):
        """Test getMyUser request structure."""

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
                method = getattr(self.users_client, "get_my_user")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/me"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getMyUser: {e}")

    def test_get_my_user_required_parameters(self):
        """Test that getMyUser requires necessary parameters."""
        method = getattr(self.users_client, "get_my_user")

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

    def test_get_my_user_response_structure(self):
        """Test getMyUser response structure validation."""

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
            method = getattr(self.users_client, "get_my_user")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_muting_request_structure(self):
        """Test getUsersMuting request structure."""

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
                method = getattr(self.users_client, "get_users_muting")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/muting"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersMuting: {e}")

    def test_get_users_muting_required_parameters(self):
        """Test that getUsersMuting requires necessary parameters."""
        method = getattr(self.users_client, "get_users_muting")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_muting_response_structure(self):
        """Test getUsersMuting response structure validation."""

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
            method = getattr(self.users_client, "get_users_muting")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_mute_user_request_structure(self):
        """Test muteUser request structure."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.users_client, "mute_user")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/muting"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for muteUser: {e}")

    def test_mute_user_required_parameters(self):
        """Test that muteUser requires necessary parameters."""
        method = getattr(self.users_client, "mute_user")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_mute_user_response_structure(self):
        """Test muteUser response structure validation."""

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

            kwargs["id"] = "test"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.users_client, "mute_user")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_unfollow_user_request_structure(self):
        """Test unfollowUser request structure."""

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

            kwargs["source_user_id"] = "test_value"

            kwargs["target_user_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "unfollow_user")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{source_user_id}/following/{target_user_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for unfollowUser: {e}")

    def test_unfollow_user_required_parameters(self):
        """Test that unfollowUser requires necessary parameters."""
        method = getattr(self.users_client, "unfollow_user")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_unfollow_user_response_structure(self):
        """Test unfollowUser response structure validation."""

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

            kwargs["source_user_id"] = "test"

            kwargs["target_user_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "unfollow_user")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_unblock_users_dms_request_structure(self):
        """Test unblockUsersDms request structure."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "unblock_users_dms")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/dm/unblock"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for unblockUsersDms: {e}")

    def test_unblock_users_dms_required_parameters(self):
        """Test that unblockUsersDms requires necessary parameters."""
        method = getattr(self.users_client, "unblock_users_dms")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_unblock_users_dms_response_structure(self):
        """Test unblockUsersDms response structure validation."""

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

            kwargs["id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "unblock_users_dms")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_reposted_by_request_structure(self):
        """Test getPostsRepostedBy request structure."""

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
                method = getattr(self.users_client, "get_posts_reposted_by")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{id}/retweeted_by"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsRepostedBy: {e}")

    def test_get_posts_reposted_by_required_parameters(self):
        """Test that getPostsRepostedBy requires necessary parameters."""
        method = getattr(self.users_client, "get_posts_reposted_by")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_reposted_by_response_structure(self):
        """Test getPostsRepostedBy response structure validation."""

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
            method = getattr(self.users_client, "get_posts_reposted_by")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_followers_request_structure(self):
        """Test getUsersFollowers request structure."""

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
                method = getattr(self.users_client, "get_users_followers")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/followers"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersFollowers: {e}")

    def test_get_users_followers_required_parameters(self):
        """Test that getUsersFollowers requires necessary parameters."""
        method = getattr(self.users_client, "get_users_followers")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_followers_response_structure(self):
        """Test getUsersFollowers response structure validation."""

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
            method = getattr(self.users_client, "get_users_followers")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_lists_members_request_structure(self):
        """Test getListsMembers request structure."""

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
                method = getattr(self.users_client, "get_lists_members")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/lists/{id}/members"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getListsMembers: {e}")

    def test_get_lists_members_required_parameters(self):
        """Test that getListsMembers requires necessary parameters."""
        method = getattr(self.users_client, "get_lists_members")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_lists_members_response_structure(self):
        """Test getListsMembers response structure validation."""

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
            method = getattr(self.users_client, "get_lists_members")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_by_id_request_structure(self):
        """Test getUsersById request structure."""

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
                method = getattr(self.users_client, "get_users_by_id")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersById: {e}")

    def test_get_users_by_id_required_parameters(self):
        """Test that getUsersById requires necessary parameters."""
        method = getattr(self.users_client, "get_users_by_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_by_id_response_structure(self):
        """Test getUsersById response structure validation."""

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
            method = getattr(self.users_client, "get_users_by_id")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_reposts_of_me_request_structure(self):
        """Test getUsersRepostsOfMe request structure."""

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
                method = getattr(self.users_client, "get_users_reposts_of_me")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/reposts_of_me"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersRepostsOfMe: {e}")

    def test_get_users_reposts_of_me_required_parameters(self):
        """Test that getUsersRepostsOfMe requires necessary parameters."""
        method = getattr(self.users_client, "get_users_reposts_of_me")

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

    def test_get_users_reposts_of_me_response_structure(self):
        """Test getUsersRepostsOfMe response structure validation."""

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
            method = getattr(self.users_client, "get_users_reposts_of_me")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_lists_followers_request_structure(self):
        """Test getListsFollowers request structure."""

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
                method = getattr(self.users_client, "get_lists_followers")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/lists/{id}/followers"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getListsFollowers: {e}")

    def test_get_lists_followers_required_parameters(self):
        """Test that getListsFollowers requires necessary parameters."""
        method = getattr(self.users_client, "get_lists_followers")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_lists_followers_response_structure(self):
        """Test getListsFollowers response structure validation."""

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
            method = getattr(self.users_client, "get_lists_followers")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_liking_users_request_structure(self):
        """Test getPostsLikingUsers request structure."""

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
                method = getattr(self.users_client, "get_posts_liking_users")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{id}/liking_users"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsLikingUsers: {e}")

    def test_get_posts_liking_users_required_parameters(self):
        """Test that getPostsLikingUsers requires necessary parameters."""
        method = getattr(self.users_client, "get_posts_liking_users")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_liking_users_response_structure(self):
        """Test getPostsLikingUsers response structure validation."""

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
            method = getattr(self.users_client, "get_posts_liking_users")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_following_request_structure(self):
        """Test getUsersFollowing request structure."""

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
                method = getattr(self.users_client, "get_users_following")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/following"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersFollowing: {e}")

    def test_get_users_following_required_parameters(self):
        """Test that getUsersFollowing requires necessary parameters."""
        method = getattr(self.users_client, "get_users_following")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_following_response_structure(self):
        """Test getUsersFollowing response structure validation."""

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
            method = getattr(self.users_client, "get_users_following")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_follow_user_request_structure(self):
        """Test followUser request structure."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.users_client, "follow_user")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/following"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for followUser: {e}")

    def test_follow_user_required_parameters(self):
        """Test that followUser requires necessary parameters."""
        method = getattr(self.users_client, "follow_user")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_follow_user_response_structure(self):
        """Test followUser response structure validation."""

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

            kwargs["id"] = "test"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.users_client, "follow_user")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_block_users_dms_request_structure(self):
        """Test blockUsersDms request structure."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "block_users_dms")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/dm/block"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for blockUsersDms: {e}")

    def test_block_users_dms_required_parameters(self):
        """Test that blockUsersDms requires necessary parameters."""
        method = getattr(self.users_client, "block_users_dms")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_block_users_dms_response_structure(self):
        """Test blockUsersDms response structure validation."""

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

            kwargs["id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "block_users_dms")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_by_ids_request_structure(self):
        """Test getUsersByIds request structure."""

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

            kwargs["ids"] = ["test_item"]

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "get_users_by_ids")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersByIds: {e}")

    def test_get_users_by_ids_required_parameters(self):
        """Test that getUsersByIds requires necessary parameters."""
        method = getattr(self.users_client, "get_users_by_ids")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_by_ids_response_structure(self):
        """Test getUsersByIds response structure validation."""

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

            kwargs["ids"] = ["test"]

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "get_users_by_ids")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_by_username_request_structure(self):
        """Test getUsersByUsername request structure."""

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

            kwargs["username"] = "test_username"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.users_client, "get_users_by_username")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/by/username/{username}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersByUsername: {e}")

    def test_get_users_by_username_required_parameters(self):
        """Test that getUsersByUsername requires necessary parameters."""
        method = getattr(self.users_client, "get_users_by_username")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_by_username_response_structure(self):
        """Test getUsersByUsername response structure validation."""

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

            kwargs["username"] = "test_value"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.users_client, "get_users_by_username")
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

            method = getattr(self.users_client, "search_users")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["query"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_by_usernames")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["usernames"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_blocking")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "unmute_user")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["source_user_id"] = "test"

                kwargs["target_user_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_my_user")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_muting")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "mute_user")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.users_client, "unfollow_user")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["source_user_id"] = "test"

                kwargs["target_user_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "unblock_users_dms")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_posts_reposted_by")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_followers")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_lists_members")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_by_id")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_reposts_of_me")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_lists_followers")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_posts_liking_users")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_following")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "follow_user")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.users_client, "block_users_dms")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_by_ids")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["ids"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.users_client, "get_users_by_username")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["username"] = "test"

                # Add request body if required

                method(**kwargs)
