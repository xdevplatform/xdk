"""
Auto-generated contract tests for Tweets client.

This module contains tests that validate the request/response contracts
of the Tweets client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.tweets.client import TweetsClient
from xdk import Client


class TestTweetsContracts:
    """Test the API contracts of TweetsClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.tweets_client = getattr(self.client, "tweets")

    def test_unlike_post_request_structure(self):
        """Test unlikePost request structure."""

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

            kwargs["id"] = "test_value"

            kwargs["tweet_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "unlike_post")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/likes/{tweet_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for unlikePost: {e}")

    def test_unlike_post_required_parameters(self):
        """Test that unlikePost requires necessary parameters."""
        method = getattr(self.tweets_client, "unlike_post")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_unlike_post_response_structure(self):
        """Test unlikePost response structure validation."""

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

            kwargs["id"] = "test"

            kwargs["tweet_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "unlike_post")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_spaces_buyers_request_structure(self):
        """Test getSpacesBuyers request structure."""

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

            kwargs["id"] = "test_id"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "get_spaces_buyers")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/spaces/{id}/buyers"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getSpacesBuyers: {e}")

    def test_get_spaces_buyers_required_parameters(self):
        """Test that getSpacesBuyers requires necessary parameters."""
        method = getattr(self.tweets_client, "get_spaces_buyers")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_spaces_buyers_response_structure(self):
        """Test getSpacesBuyers response structure validation."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "get_spaces_buyers")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_analytics_request_structure(self):
        """Test getPostsAnalytics request structure."""

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

            kwargs["end_time"] = "test_end_time"

            kwargs["start_time"] = "test_start_time"

            kwargs["granularity"] = "test_granularity"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "get_posts_analytics")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/analytics"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsAnalytics: {e}")

    def test_get_posts_analytics_required_parameters(self):
        """Test that getPostsAnalytics requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_analytics")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_analytics_response_structure(self):
        """Test getPostsAnalytics response structure validation."""

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

            kwargs["end_time"] = "test_value"

            kwargs["start_time"] = "test_value"

            kwargs["granularity"] = "test_value"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "get_posts_analytics")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_quoted_posts_request_structure(self):
        """Test getPostsQuotedPosts request structure."""

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
                method = getattr(self.tweets_client, "get_posts_quoted_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{id}/quote_tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsQuotedPosts: {e}")

    def test_get_posts_quoted_posts_required_parameters(self):
        """Test that getPostsQuotedPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_quoted_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_quoted_posts_response_structure(self):
        """Test getPostsQuotedPosts response structure validation."""

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
            method = getattr(self.tweets_client, "get_posts_quoted_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_liked_posts_request_structure(self):
        """Test getUsersLikedPosts request structure."""

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
                method = getattr(self.tweets_client, "get_users_liked_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/liked_tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersLikedPosts: {e}")

    def test_get_users_liked_posts_required_parameters(self):
        """Test that getUsersLikedPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_users_liked_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_liked_posts_response_structure(self):
        """Test getUsersLikedPosts response structure validation."""

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
            method = getattr(self.tweets_client, "get_users_liked_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_search_posts_recent_request_structure(self):
        """Test searchPostsRecent request structure."""

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
                method = getattr(self.tweets_client, "search_posts_recent")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/recent"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for searchPostsRecent: {e}")

    def test_search_posts_recent_required_parameters(self):
        """Test that searchPostsRecent requires necessary parameters."""
        method = getattr(self.tweets_client, "search_posts_recent")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_search_posts_recent_response_structure(self):
        """Test searchPostsRecent response structure validation."""

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
            method = getattr(self.tweets_client, "search_posts_recent")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_reposts_request_structure(self):
        """Test getPostsReposts request structure."""

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
                method = getattr(self.tweets_client, "get_posts_reposts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{id}/retweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsReposts: {e}")

    def test_get_posts_reposts_required_parameters(self):
        """Test that getPostsReposts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_reposts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_reposts_response_structure(self):
        """Test getPostsReposts response structure validation."""

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
            method = getattr(self.tweets_client, "get_posts_reposts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_posts_request_structure(self):
        """Test getUsersPosts request structure."""

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
                method = getattr(self.tweets_client, "get_users_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersPosts: {e}")

    def test_get_users_posts_required_parameters(self):
        """Test that getUsersPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_users_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_posts_response_structure(self):
        """Test getUsersPosts response structure validation."""

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
            method = getattr(self.tweets_client, "get_users_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_pt_request_structure(self):
        """Test streamPostsFirehosePt request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_firehose_pt")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/pt"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehosePt: {e}")

    def test_stream_posts_firehose_pt_required_parameters(self):
        """Test that streamPostsFirehosePt requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_firehose_pt")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_pt_response_structure(self):
        """Test streamPostsFirehosePt response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_firehose_pt")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_search_posts_all_request_structure(self):
        """Test searchPostsAll request structure."""

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
                method = getattr(self.tweets_client, "search_posts_all")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/all"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for searchPostsAll: {e}")

    def test_search_posts_all_required_parameters(self):
        """Test that searchPostsAll requires necessary parameters."""
        method = getattr(self.tweets_client, "search_posts_all")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_search_posts_all_response_structure(self):
        """Test searchPostsAll response structure validation."""

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
            method = getattr(self.tweets_client, "search_posts_all")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_counts_recent_request_structure(self):
        """Test getPostsCountsRecent request structure."""

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
                method = getattr(self.tweets_client, "get_posts_counts_recent")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/counts/recent"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsCountsRecent: {e}")

    def test_get_posts_counts_recent_required_parameters(self):
        """Test that getPostsCountsRecent requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_counts_recent")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_counts_recent_response_structure(self):
        """Test getPostsCountsRecent response structure validation."""

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
            method = getattr(self.tweets_client, "get_posts_counts_recent")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_en_request_structure(self):
        """Test streamPostsFirehoseEn request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_firehose_en")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/en"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehoseEn: {e}")

    def test_stream_posts_firehose_en_required_parameters(self):
        """Test that streamPostsFirehoseEn requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_firehose_en")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_en_response_structure(self):
        """Test streamPostsFirehoseEn response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_firehose_en")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_rule_counts_request_structure(self):
        """Test getRuleCounts request structure."""

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
                method = getattr(self.tweets_client, "get_rule_counts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream/rules/counts"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getRuleCounts: {e}")

    def test_get_rule_counts_required_parameters(self):
        """Test that getRuleCounts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_rule_counts")

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

    def test_get_rule_counts_response_structure(self):
        """Test getRuleCounts response structure validation."""

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
            method = getattr(self.tweets_client, "get_rule_counts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_timeline_request_structure(self):
        """Test getUsersTimeline request structure."""

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
                method = getattr(self.tweets_client, "get_users_timeline")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/timelines/reverse_chronological"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersTimeline: {e}")

    def test_get_users_timeline_required_parameters(self):
        """Test that getUsersTimeline requires necessary parameters."""
        method = getattr(self.tweets_client, "get_users_timeline")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_timeline_response_structure(self):
        """Test getUsersTimeline response structure validation."""

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
            method = getattr(self.tweets_client, "get_users_timeline")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_ja_request_structure(self):
        """Test streamPostsFirehoseJa request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_firehose_ja")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/ja"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehoseJa: {e}")

    def test_stream_posts_firehose_ja_required_parameters(self):
        """Test that streamPostsFirehoseJa requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_firehose_ja")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_ja_response_structure(self):
        """Test streamPostsFirehoseJa response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_firehose_ja")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_insights28_hr_request_structure(self):
        """Test getInsights28Hr request structure."""

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

            kwargs["tweet_ids"] = ["test_item"]

            kwargs["granularity"] = "test_granularity"

            kwargs["requested_metrics"] = ["test_item"]

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "get_insights28_hr")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/insights/28hr"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getInsights28Hr: {e}")

    def test_get_insights28_hr_required_parameters(self):
        """Test that getInsights28Hr requires necessary parameters."""
        method = getattr(self.tweets_client, "get_insights28_hr")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_insights28_hr_response_structure(self):
        """Test getInsights28Hr response structure validation."""

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

            kwargs["tweet_ids"] = ["test"]

            kwargs["granularity"] = "test_value"

            kwargs["requested_metrics"] = ["test"]

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "get_insights28_hr")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_request_structure(self):
        """Test streamPosts request structure."""

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
                method = getattr(self.tweets_client, "stream_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPosts: {e}")

    def test_stream_posts_required_parameters(self):
        """Test that streamPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts")

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

    def test_stream_posts_response_structure(self):
        """Test streamPosts response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_rules_request_structure(self):
        """Test getRules request structure."""

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
                method = getattr(self.tweets_client, "get_rules")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream/rules"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getRules: {e}")

    def test_get_rules_required_parameters(self):
        """Test that getRules requires necessary parameters."""
        method = getattr(self.tweets_client, "get_rules")

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

    def test_get_rules_response_structure(self):
        """Test getRules response structure validation."""

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
            method = getattr(self.tweets_client, "get_rules")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_update_rules_request_structure(self):
        """Test updateRules request structure."""

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

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.tweets_client, "update_rules")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream/rules"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for updateRules: {e}")

    def test_update_rules_required_parameters(self):
        """Test that updateRules requires necessary parameters."""
        method = getattr(self.tweets_client, "update_rules")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_update_rules_response_structure(self):
        """Test updateRules response structure validation."""

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

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.tweets_client, "update_rules")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_hide_posts_reply_request_structure(self):
        """Test hidePostsReply request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.put.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["tweet_id"] = "test_value"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.tweets_client, "hide_posts_reply")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.put.assert_called_once()

                # Verify request structure
                call_args = mock_session.put.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{tweet_id}/hidden"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for hidePostsReply: {e}")

    def test_hide_posts_reply_required_parameters(self):
        """Test that hidePostsReply requires necessary parameters."""
        method = getattr(self.tweets_client, "hide_posts_reply")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_hide_posts_reply_response_structure(self):
        """Test hidePostsReply response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.put.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["tweet_id"] = "test"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.tweets_client, "hide_posts_reply")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_lists_posts_request_structure(self):
        """Test getListsPosts request structure."""

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
                method = getattr(self.tweets_client, "get_lists_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/lists/{id}/tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getListsPosts: {e}")

    def test_get_lists_posts_required_parameters(self):
        """Test that getListsPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_lists_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_lists_posts_response_structure(self):
        """Test getListsPosts response structure validation."""

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
            method = getattr(self.tweets_client, "get_lists_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_spaces_posts_request_structure(self):
        """Test getSpacesPosts request structure."""

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

            kwargs["id"] = "test_id"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "get_spaces_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/spaces/{id}/tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getSpacesPosts: {e}")

    def test_get_spaces_posts_required_parameters(self):
        """Test that getSpacesPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "get_spaces_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_spaces_posts_response_structure(self):
        """Test getSpacesPosts response structure validation."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "get_spaces_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_by_id_request_structure(self):
        """Test getPostsById request structure."""

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
                method = getattr(self.tweets_client, "get_posts_by_id")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsById: {e}")

    def test_get_posts_by_id_required_parameters(self):
        """Test that getPostsById requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_by_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_by_id_response_structure(self):
        """Test getPostsById response structure validation."""

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
            method = getattr(self.tweets_client, "get_posts_by_id")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_delete_posts_request_structure(self):
        """Test deletePosts request structure."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "delete_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/{id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for deletePosts: {e}")

    def test_delete_posts_required_parameters(self):
        """Test that deletePosts requires necessary parameters."""
        method = getattr(self.tweets_client, "delete_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_delete_posts_response_structure(self):
        """Test deletePosts response structure validation."""

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

            kwargs["id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "delete_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_users_mentions_request_structure(self):
        """Test getUsersMentions request structure."""

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
                method = getattr(self.tweets_client, "get_users_mentions")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/mentions"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getUsersMentions: {e}")

    def test_get_users_mentions_required_parameters(self):
        """Test that getUsersMentions requires necessary parameters."""
        method = getattr(self.tweets_client, "get_users_mentions")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_users_mentions_response_structure(self):
        """Test getUsersMentions response structure validation."""

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
            method = getattr(self.tweets_client, "get_users_mentions")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_by_ids_request_structure(self):
        """Test getPostsByIds request structure."""

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
                method = getattr(self.tweets_client, "get_posts_by_ids")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsByIds: {e}")

    def test_get_posts_by_ids_required_parameters(self):
        """Test that getPostsByIds requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_by_ids")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_by_ids_response_structure(self):
        """Test getPostsByIds response structure validation."""

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
            method = getattr(self.tweets_client, "get_posts_by_ids")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_create_posts_request_structure(self):
        """Test createPosts request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 201
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.tweets_client, "create_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for createPosts: {e}")

    def test_create_posts_required_parameters(self):
        """Test that createPosts requires necessary parameters."""
        method = getattr(self.tweets_client, "create_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_create_posts_response_structure(self):
        """Test createPosts response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 201
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.tweets_client, "create_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_unrepost_post_request_structure(self):
        """Test unrepostPost request structure."""

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

            kwargs["id"] = "test_value"

            kwargs["source_tweet_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "unrepost_post")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/retweets/{source_tweet_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for unrepostPost: {e}")

    def test_unrepost_post_required_parameters(self):
        """Test that unrepostPost requires necessary parameters."""
        method = getattr(self.tweets_client, "unrepost_post")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_unrepost_post_response_structure(self):
        """Test unrepostPost response structure validation."""

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

            kwargs["id"] = "test"

            kwargs["source_tweet_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "unrepost_post")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_sample_request_structure(self):
        """Test streamPostsSample request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_sample")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/sample/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsSample: {e}")

    def test_stream_posts_sample_required_parameters(self):
        """Test that streamPostsSample requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_sample")

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

    def test_stream_posts_sample_response_structure(self):
        """Test streamPostsSample response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_sample")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_insights_historical_request_structure(self):
        """Test getInsightsHistorical request structure."""

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

            kwargs["tweet_ids"] = ["test_item"]

            kwargs["end_time"] = "test_end_time"

            kwargs["start_time"] = "test_start_time"

            kwargs["granularity"] = "test_granularity"

            kwargs["requested_metrics"] = ["test_item"]

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.tweets_client, "get_insights_historical")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/insights/historical"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getInsightsHistorical: {e}")

    def test_get_insights_historical_required_parameters(self):
        """Test that getInsightsHistorical requires necessary parameters."""
        method = getattr(self.tweets_client, "get_insights_historical")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_insights_historical_response_structure(self):
        """Test getInsightsHistorical response structure validation."""

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

            kwargs["tweet_ids"] = ["test"]

            kwargs["end_time"] = "test_value"

            kwargs["start_time"] = "test_value"

            kwargs["granularity"] = "test_value"

            kwargs["requested_metrics"] = ["test"]

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.tweets_client, "get_insights_historical")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_repost_post_request_structure(self):
        """Test repostPost request structure."""

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
                method = getattr(self.tweets_client, "repost_post")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/retweets"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for repostPost: {e}")

    def test_repost_post_required_parameters(self):
        """Test that repostPost requires necessary parameters."""
        method = getattr(self.tweets_client, "repost_post")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_repost_post_response_structure(self):
        """Test repostPost response structure validation."""

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
            method = getattr(self.tweets_client, "repost_post")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_posts_counts_all_request_structure(self):
        """Test getPostsCountsAll request structure."""

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
                method = getattr(self.tweets_client, "get_posts_counts_all")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/counts/all"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getPostsCountsAll: {e}")

    def test_get_posts_counts_all_required_parameters(self):
        """Test that getPostsCountsAll requires necessary parameters."""
        method = getattr(self.tweets_client, "get_posts_counts_all")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_posts_counts_all_response_structure(self):
        """Test getPostsCountsAll response structure validation."""

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
            method = getattr(self.tweets_client, "get_posts_counts_all")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_request_structure(self):
        """Test streamPostsFirehose request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_firehose")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehose: {e}")

    def test_stream_posts_firehose_required_parameters(self):
        """Test that streamPostsFirehose requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_firehose")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_response_structure(self):
        """Test streamPostsFirehose response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_firehose")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_like_post_request_structure(self):
        """Test likePost request structure."""

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
                method = getattr(self.tweets_client, "like_post")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/likes"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for likePost: {e}")

    def test_like_post_required_parameters(self):
        """Test that likePost requires necessary parameters."""
        method = getattr(self.tweets_client, "like_post")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_like_post_response_structure(self):
        """Test likePost response structure validation."""

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
            method = getattr(self.tweets_client, "like_post")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_ko_request_structure(self):
        """Test streamPostsFirehoseKo request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_firehose_ko")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/ko"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehoseKo: {e}")

    def test_stream_posts_firehose_ko_required_parameters(self):
        """Test that streamPostsFirehoseKo requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_firehose_ko")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_ko_response_structure(self):
        """Test streamPostsFirehoseKo response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_firehose_ko")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_sample10_request_structure(self):
        """Test streamPostsSample10 request structure."""

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
                method = getattr(self.tweets_client, "stream_posts_sample10")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/sample10/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsSample10: {e}")

    def test_stream_posts_sample10_required_parameters(self):
        """Test that streamPostsSample10 requires necessary parameters."""
        method = getattr(self.tweets_client, "stream_posts_sample10")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_sample10_response_structure(self):
        """Test streamPostsSample10 response structure validation."""

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
            method = getattr(self.tweets_client, "stream_posts_sample10")
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

            method = getattr(self.tweets_client, "unlike_post")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                kwargs["tweet_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_spaces_buyers")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_analytics")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["ids"] = "test"

                kwargs["end_time"] = "test"

                kwargs["start_time"] = "test"

                kwargs["granularity"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_quoted_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_users_liked_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "search_posts_recent")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["query"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_reposts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_users_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_firehose_pt")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "search_posts_all")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["query"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_counts_recent")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["query"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_firehose_en")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_rule_counts")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_users_timeline")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_firehose_ja")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_insights28_hr")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["tweet_ids"] = "test"

                kwargs["granularity"] = "test"

                kwargs["requested_metrics"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_rules")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "update_rules")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.tweets_client, "hide_posts_reply")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["tweet_id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.tweets_client, "get_lists_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_spaces_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_by_id")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "delete_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_users_mentions")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_by_ids")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["ids"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "create_posts")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.tweets_client, "unrepost_post")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                kwargs["source_tweet_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_sample")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "get_insights_historical")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["tweet_ids"] = "test"

                kwargs["end_time"] = "test"

                kwargs["start_time"] = "test"

                kwargs["granularity"] = "test"

                kwargs["requested_metrics"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "repost_post")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.tweets_client, "get_posts_counts_all")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["query"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_firehose")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "like_post")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_firehose_ko")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.tweets_client, "stream_posts_sample10")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)
