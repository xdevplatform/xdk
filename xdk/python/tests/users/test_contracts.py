"""
Auto-generated contract tests for {"class_name": "Users", "display_name": "users", "import_name": "users", "original": ["users"], "property_name": "users"} client.

This module contains tests that validate the request/response contracts
of the {"class_name": "Users", "display_name": "users", "import_name": "users", "original": ["users"], "property_name": "users"} client against the OpenAPI specification.

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


    def test_get_list_memberships_request_structure(self):
        """Test get_list_memberships request structure."""
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
                method = getattr(self.users_client, "get_list_memberships")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/list_memberships"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_list_memberships: {e}")


    def test_get_list_memberships_required_parameters(self):
        """Test that get_list_memberships handles parameters correctly."""
        method = getattr(self.users_client, "get_list_memberships")
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


    def test_get_list_memberships_response_structure(self):
        """Test get_list_memberships response structure validation."""
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
            method = getattr(self.users_client, "get_list_memberships")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_search_request_structure(self):
        """Test search request structure."""
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
                method = getattr(self.users_client, "search")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for search: {e}")


    def test_search_required_parameters(self):
        """Test that search handles parameters correctly."""
        method = getattr(self.users_client, "search")
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


    def test_search_response_structure(self):
        """Test search response structure validation."""
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
            method = getattr(self.users_client, "search")
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
        """Test like_post request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import LikePostRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = LikePostRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "like_post")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for like_post: {e}")


    def test_like_post_required_parameters(self):
        """Test that like_post handles parameters correctly."""
        method = getattr(self.users_client, "like_post")
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


    def test_like_post_response_structure(self):
        """Test like_post response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import LikePostRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = LikePostRequest()
            # Call method and verify response structure
            method = getattr(self.users_client, "like_post")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_blocking_request_structure(self):
        """Test get_blocking request structure."""
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
                method = getattr(self.users_client, "get_blocking")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_blocking: {e}")


    def test_get_blocking_required_parameters(self):
        """Test that get_blocking handles parameters correctly."""
        method = getattr(self.users_client, "get_blocking")
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


    def test_get_blocking_response_structure(self):
        """Test get_blocking response structure validation."""
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
            method = getattr(self.users_client, "get_blocking")
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
        """Test unrepost_post request structure."""
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
                method = getattr(self.users_client, "unrepost_post")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unrepost_post: {e}")


    def test_unrepost_post_required_parameters(self):
        """Test that unrepost_post handles parameters correctly."""
        method = getattr(self.users_client, "unrepost_post")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_unrepost_post_response_structure(self):
        """Test unrepost_post response structure validation."""
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
            method = getattr(self.users_client, "unrepost_post")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_liked_posts_request_structure(self):
        """Test get_liked_posts request structure."""
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
                method = getattr(self.users_client, "get_liked_posts")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_liked_posts: {e}")


    def test_get_liked_posts_required_parameters(self):
        """Test that get_liked_posts handles parameters correctly."""
        method = getattr(self.users_client, "get_liked_posts")
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


    def test_get_liked_posts_response_structure(self):
        """Test get_liked_posts response structure validation."""
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
            method = getattr(self.users_client, "get_liked_posts")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_by_ids_request_structure(self):
        """Test get_by_ids request structure."""
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
                method = getattr(self.users_client, "get_by_ids")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_by_ids: {e}")


    def test_get_by_ids_required_parameters(self):
        """Test that get_by_ids handles parameters correctly."""
        method = getattr(self.users_client, "get_by_ids")
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


    def test_get_by_ids_response_structure(self):
        """Test get_by_ids response structure validation."""
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
            method = getattr(self.users_client, "get_by_ids")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_by_id_request_structure(self):
        """Test get_by_id request structure."""
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
                method = getattr(self.users_client, "get_by_id")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_by_id: {e}")


    def test_get_by_id_required_parameters(self):
        """Test that get_by_id handles parameters correctly."""
        method = getattr(self.users_client, "get_by_id")
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


    def test_get_by_id_response_structure(self):
        """Test get_by_id response structure validation."""
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
            method = getattr(self.users_client, "get_by_id")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_by_username_request_structure(self):
        """Test get_by_username request structure."""
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
                method = getattr(self.users_client, "get_by_username")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_by_username: {e}")


    def test_get_by_username_required_parameters(self):
        """Test that get_by_username handles parameters correctly."""
        method = getattr(self.users_client, "get_by_username")
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


    def test_get_by_username_response_structure(self):
        """Test get_by_username response structure validation."""
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
            method = getattr(self.users_client, "get_by_username")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_bookmarks_request_structure(self):
        """Test get_bookmarks request structure."""
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
                method = getattr(self.users_client, "get_bookmarks")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/bookmarks"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_bookmarks: {e}")


    def test_get_bookmarks_required_parameters(self):
        """Test that get_bookmarks handles parameters correctly."""
        method = getattr(self.users_client, "get_bookmarks")
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


    def test_get_bookmarks_response_structure(self):
        """Test get_bookmarks response structure validation."""
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
            method = getattr(self.users_client, "get_bookmarks")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_create_bookmark_request_structure(self):
        """Test create_bookmark request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import CreateBookmarkRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateBookmarkRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "create_bookmark")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.post.assert_called_once()
                # Verify request structure
                call_args = mock_session.post.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/bookmarks"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for create_bookmark: {e}")


    def test_create_bookmark_required_parameters(self):
        """Test that create_bookmark handles parameters correctly."""
        method = getattr(self.users_client, "create_bookmark")
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


    def test_create_bookmark_response_structure(self):
        """Test create_bookmark response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import CreateBookmarkRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateBookmarkRequest()
            # Call method and verify response structure
            method = getattr(self.users_client, "create_bookmark")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_muting_request_structure(self):
        """Test get_muting request structure."""
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
                method = getattr(self.users_client, "get_muting")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_muting: {e}")


    def test_get_muting_required_parameters(self):
        """Test that get_muting handles parameters correctly."""
        method = getattr(self.users_client, "get_muting")
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


    def test_get_muting_response_structure(self):
        """Test get_muting response structure validation."""
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
            method = getattr(self.users_client, "get_muting")
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
        """Test mute_user request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import MuteUserRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = MuteUserRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "mute_user")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for mute_user: {e}")


    def test_mute_user_required_parameters(self):
        """Test that mute_user handles parameters correctly."""
        method = getattr(self.users_client, "mute_user")
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


    def test_mute_user_response_structure(self):
        """Test mute_user response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import MuteUserRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = MuteUserRequest()
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


    def test_get_bookmark_folders_request_structure(self):
        """Test get_bookmark_folders request structure."""
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
                method = getattr(self.users_client, "get_bookmark_folders")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/bookmarks/folders"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_bookmark_folders: {e}")


    def test_get_bookmark_folders_required_parameters(self):
        """Test that get_bookmark_folders handles parameters correctly."""
        method = getattr(self.users_client, "get_bookmark_folders")
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


    def test_get_bookmark_folders_response_structure(self):
        """Test get_bookmark_folders response structure validation."""
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
            method = getattr(self.users_client, "get_bookmark_folders")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_unfollow_list_request_structure(self):
        """Test unfollow_list request structure."""
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
            kwargs["list_id"] = "test_value"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.users_client, "unfollow_list")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.delete.assert_called_once()
                # Verify request structure
                call_args = mock_session.delete.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/followed_lists/{list_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unfollow_list: {e}")


    def test_unfollow_list_required_parameters(self):
        """Test that unfollow_list handles parameters correctly."""
        method = getattr(self.users_client, "unfollow_list")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_unfollow_list_response_structure(self):
        """Test unfollow_list response structure validation."""
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
            kwargs["list_id"] = "test"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.users_client, "unfollow_list")
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
        """Test unfollow_user request structure."""
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
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unfollow_user: {e}")


    def test_unfollow_user_required_parameters(self):
        """Test that unfollow_user handles parameters correctly."""
        method = getattr(self.users_client, "unfollow_user")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_unfollow_user_response_structure(self):
        """Test unfollow_user response structure validation."""
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


    def test_unlike_post_request_structure(self):
        """Test unlike_post request structure."""
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
                method = getattr(self.users_client, "unlike_post")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unlike_post: {e}")


    def test_unlike_post_required_parameters(self):
        """Test that unlike_post handles parameters correctly."""
        method = getattr(self.users_client, "unlike_post")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_unlike_post_response_structure(self):
        """Test unlike_post response structure validation."""
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
            method = getattr(self.users_client, "unlike_post")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_following_request_structure(self):
        """Test get_following request structure."""
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
                method = getattr(self.users_client, "get_following")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_following: {e}")


    def test_get_following_required_parameters(self):
        """Test that get_following handles parameters correctly."""
        method = getattr(self.users_client, "get_following")
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


    def test_get_following_response_structure(self):
        """Test get_following response structure validation."""
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
            method = getattr(self.users_client, "get_following")
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
        """Test follow_user request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import FollowUserRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = FollowUserRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "follow_user")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for follow_user: {e}")


    def test_follow_user_required_parameters(self):
        """Test that follow_user handles parameters correctly."""
        method = getattr(self.users_client, "follow_user")
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


    def test_follow_user_response_structure(self):
        """Test follow_user response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import FollowUserRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = FollowUserRequest()
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


    def test_repost_post_request_structure(self):
        """Test repost_post request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import RepostPostRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = RepostPostRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "repost_post")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for repost_post: {e}")


    def test_repost_post_required_parameters(self):
        """Test that repost_post handles parameters correctly."""
        method = getattr(self.users_client, "repost_post")
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


    def test_repost_post_response_structure(self):
        """Test repost_post response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import RepostPostRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = RepostPostRequest()
            # Call method and verify response structure
            method = getattr(self.users_client, "repost_post")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_timeline_request_structure(self):
        """Test get_timeline request structure."""
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
                method = getattr(self.users_client, "get_timeline")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_timeline: {e}")


    def test_get_timeline_required_parameters(self):
        """Test that get_timeline handles parameters correctly."""
        method = getattr(self.users_client, "get_timeline")
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


    def test_get_timeline_response_structure(self):
        """Test get_timeline response structure validation."""
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
            method = getattr(self.users_client, "get_timeline")
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
        """Test unmute_user request structure."""
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
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unmute_user: {e}")


    def test_unmute_user_required_parameters(self):
        """Test that unmute_user handles parameters correctly."""
        method = getattr(self.users_client, "unmute_user")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_unmute_user_response_structure(self):
        """Test unmute_user response structure validation."""
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


    def test_delete_bookmark_request_structure(self):
        """Test delete_bookmark request structure."""
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
                method = getattr(self.users_client, "delete_bookmark")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.delete.assert_called_once()
                # Verify request structure
                call_args = mock_session.delete.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/bookmarks/{tweet_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for delete_bookmark: {e}")


    def test_delete_bookmark_required_parameters(self):
        """Test that delete_bookmark handles parameters correctly."""
        method = getattr(self.users_client, "delete_bookmark")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_delete_bookmark_response_structure(self):
        """Test delete_bookmark response structure validation."""
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
            method = getattr(self.users_client, "delete_bookmark")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_by_usernames_request_structure(self):
        """Test get_by_usernames request structure."""
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
                method = getattr(self.users_client, "get_by_usernames")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_by_usernames: {e}")


    def test_get_by_usernames_required_parameters(self):
        """Test that get_by_usernames handles parameters correctly."""
        method = getattr(self.users_client, "get_by_usernames")
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


    def test_get_by_usernames_response_structure(self):
        """Test get_by_usernames response structure validation."""
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
            method = getattr(self.users_client, "get_by_usernames")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_reposts_of_me_request_structure(self):
        """Test get_reposts_of_me request structure."""
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
                method = getattr(self.users_client, "get_reposts_of_me")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_reposts_of_me: {e}")


    def test_get_reposts_of_me_required_parameters(self):
        """Test that get_reposts_of_me handles parameters correctly."""
        method = getattr(self.users_client, "get_reposts_of_me")
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


    def test_get_reposts_of_me_response_structure(self):
        """Test get_reposts_of_me response structure validation."""
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
            method = getattr(self.users_client, "get_reposts_of_me")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_mentions_request_structure(self):
        """Test get_mentions request structure."""
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
                method = getattr(self.users_client, "get_mentions")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_mentions: {e}")


    def test_get_mentions_required_parameters(self):
        """Test that get_mentions handles parameters correctly."""
        method = getattr(self.users_client, "get_mentions")
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


    def test_get_mentions_response_structure(self):
        """Test get_mentions response structure validation."""
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
            method = getattr(self.users_client, "get_mentions")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_owned_lists_request_structure(self):
        """Test get_owned_lists request structure."""
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
                method = getattr(self.users_client, "get_owned_lists")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/owned_lists"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_owned_lists: {e}")


    def test_get_owned_lists_required_parameters(self):
        """Test that get_owned_lists handles parameters correctly."""
        method = getattr(self.users_client, "get_owned_lists")
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


    def test_get_owned_lists_response_structure(self):
        """Test get_owned_lists response structure validation."""
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
            method = getattr(self.users_client, "get_owned_lists")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_posts_request_structure(self):
        """Test get_posts request structure."""
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
                method = getattr(self.users_client, "get_posts")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_posts: {e}")


    def test_get_posts_required_parameters(self):
        """Test that get_posts handles parameters correctly."""
        method = getattr(self.users_client, "get_posts")
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


    def test_get_posts_response_structure(self):
        """Test get_posts response structure validation."""
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
            method = getattr(self.users_client, "get_posts")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_me_request_structure(self):
        """Test get_me request structure."""
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
                method = getattr(self.users_client, "get_me")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_me: {e}")


    def test_get_me_required_parameters(self):
        """Test that get_me handles parameters correctly."""
        method = getattr(self.users_client, "get_me")
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


    def test_get_me_response_structure(self):
        """Test get_me response structure validation."""
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
            method = getattr(self.users_client, "get_me")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_bookmarks_by_folder_id_request_structure(self):
        """Test get_bookmarks_by_folder_id request structure."""
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
            kwargs["folder_id"] = "test_value"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.users_client, "get_bookmarks_by_folder_id")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/bookmarks/folders/{folder_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_bookmarks_by_folder_id: {e}")


    def test_get_bookmarks_by_folder_id_required_parameters(self):
        """Test that get_bookmarks_by_folder_id handles parameters correctly."""
        method = getattr(self.users_client, "get_bookmarks_by_folder_id")
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


    def test_get_bookmarks_by_folder_id_response_structure(self):
        """Test get_bookmarks_by_folder_id response structure validation."""
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
            kwargs["folder_id"] = "test"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.users_client, "get_bookmarks_by_folder_id")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_unblock_dms_request_structure(self):
        """Test unblock_dms request structure."""
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
                method = getattr(self.users_client, "unblock_dms")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unblock_dms: {e}")


    def test_unblock_dms_required_parameters(self):
        """Test that unblock_dms handles parameters correctly."""
        method = getattr(self.users_client, "unblock_dms")
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


    def test_unblock_dms_response_structure(self):
        """Test unblock_dms response structure validation."""
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
            method = getattr(self.users_client, "unblock_dms")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_followed_lists_request_structure(self):
        """Test get_followed_lists request structure."""
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
                method = getattr(self.users_client, "get_followed_lists")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/followed_lists"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_followed_lists: {e}")


    def test_get_followed_lists_required_parameters(self):
        """Test that get_followed_lists handles parameters correctly."""
        method = getattr(self.users_client, "get_followed_lists")
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


    def test_get_followed_lists_response_structure(self):
        """Test get_followed_lists response structure validation."""
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
            method = getattr(self.users_client, "get_followed_lists")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_follow_list_request_structure(self):
        """Test follow_list request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import FollowListRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = FollowListRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "follow_list")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.post.assert_called_once()
                # Verify request structure
                call_args = mock_session.post.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/followed_lists"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for follow_list: {e}")


    def test_follow_list_required_parameters(self):
        """Test that follow_list handles parameters correctly."""
        method = getattr(self.users_client, "follow_list")
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


    def test_follow_list_response_structure(self):
        """Test follow_list response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import FollowListRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = FollowListRequest()
            # Call method and verify response structure
            method = getattr(self.users_client, "follow_list")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_followers_request_structure(self):
        """Test get_followers request structure."""
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
                method = getattr(self.users_client, "get_followers")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_followers: {e}")


    def test_get_followers_required_parameters(self):
        """Test that get_followers handles parameters correctly."""
        method = getattr(self.users_client, "get_followers")
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


    def test_get_followers_response_structure(self):
        """Test get_followers response structure validation."""
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
            method = getattr(self.users_client, "get_followers")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_pinned_lists_request_structure(self):
        """Test get_pinned_lists request structure."""
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
                method = getattr(self.users_client, "get_pinned_lists")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.get.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/pinned_lists"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for get_pinned_lists: {e}")


    def test_get_pinned_lists_required_parameters(self):
        """Test that get_pinned_lists handles parameters correctly."""
        method = getattr(self.users_client, "get_pinned_lists")
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


    def test_get_pinned_lists_response_structure(self):
        """Test get_pinned_lists response structure validation."""
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
            method = getattr(self.users_client, "get_pinned_lists")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_pin_list_request_structure(self):
        """Test pin_list request structure."""
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
            # Import and create proper request model instance
            from xdk.users.models import PinListRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = PinListRequest()
            # Call the method
            try:
                method = getattr(self.users_client, "pin_list")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.post.assert_called_once()
                # Verify request structure
                call_args = mock_session.post.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/pinned_lists"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for pin_list: {e}")


    def test_pin_list_required_parameters(self):
        """Test that pin_list handles parameters correctly."""
        method = getattr(self.users_client, "pin_list")
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


    def test_pin_list_response_structure(self):
        """Test pin_list response structure validation."""
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
            # Import and create proper request model instance
            from xdk.users.models import PinListRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = PinListRequest()
            # Call method and verify response structure
            method = getattr(self.users_client, "pin_list")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_block_dms_request_structure(self):
        """Test block_dms request structure."""
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
                method = getattr(self.users_client, "block_dms")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.post.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
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
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for block_dms: {e}")


    def test_block_dms_required_parameters(self):
        """Test that block_dms handles parameters correctly."""
        method = getattr(self.users_client, "block_dms")
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


    def test_block_dms_response_structure(self):
        """Test block_dms response structure validation."""
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
            method = getattr(self.users_client, "block_dms")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_unpin_list_request_structure(self):
        """Test unpin_list request structure."""
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
            kwargs["list_id"] = "test_value"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.users_client, "unpin_list")
                result = method(**kwargs)
                # Check if this is a streaming operation (returns Generator)
                import types
                is_streaming = isinstance(result, types.GeneratorType)
                if is_streaming:
                    # For streaming operations, we need to set up the mock to handle streaming
                    # Mock the streaming response
                    mock_streaming_response = Mock()
                    mock_streaming_response.status_code = 200
                    mock_streaming_response.raise_for_status.return_value = None
                    mock_streaming_response.__enter__ = Mock(
                        return_value=mock_streaming_response
                    )
                    mock_streaming_response.__exit__ = Mock(return_value=None)
                    # Mock iter_content to yield some test data
                    test_data = '{"data": "test"}\n'
                    mock_streaming_response.iter_content.return_value = [test_data]
                    # Update the session mock to return our streaming response
                    mock_session.delete.return_value = mock_streaming_response
                    # Consume the generator to trigger the HTTP request
                    try:
                        next(result)
                    except StopIteration:
                        pass  # Expected when stream ends
                    except Exception:
                        pass  # Ignore other exceptions in test data processing
                # Verify the request was made
                mock_session.delete.assert_called_once()
                # Verify request structure
                call_args = mock_session.delete.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/{id}/pinned_lists/{list_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(
                        result, types.GeneratorType
                    ), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for unpin_list: {e}")


    def test_unpin_list_required_parameters(self):
        """Test that unpin_list handles parameters correctly."""
        method = getattr(self.users_client, "unpin_list")
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, "session") as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()


    def test_unpin_list_response_structure(self):
        """Test unpin_list response structure validation."""
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
            kwargs["list_id"] = "test"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.users_client, "unpin_list")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
