"""
Auto-generated contract tests for {"class_name": "CommunityNotes", "display_name": "community notes", "import_name": "community_notes", "original": ["community", "notes"], "property_name": "community_notes"} client.

This module contains tests that validate the request/response contracts
of the {"class_name": "CommunityNotes", "display_name": "community notes", "import_name": "community_notes", "original": ["community", "notes"], "property_name": "community_notes"} client against the OpenAPI specification.

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


    def test_delete_request_structure(self):
        """Test delete request structure."""
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
                method = getattr(self.community_notes_client, "delete")
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
                expected_path = "/2/notes/{id}"
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
                pytest.fail(f"Contract test failed for delete: {e}")


    def test_delete_required_parameters(self):
        """Test that delete handles parameters correctly."""
        method = getattr(self.community_notes_client, "delete")
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


    def test_delete_response_structure(self):
        """Test delete response structure validation."""
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
            method = getattr(self.community_notes_client, "delete")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_create_request_structure(self):
        """Test create request structure."""
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
            # Import and create proper request model instance
            from xdk.community_notes.models import CreateRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateRequest()
            # Call the method
            try:
                method = getattr(self.community_notes_client, "create")
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
                expected_path = "/2/notes"
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
                pytest.fail(f"Contract test failed for create: {e}")


    def test_create_required_parameters(self):
        """Test that create handles parameters correctly."""
        method = getattr(self.community_notes_client, "create")
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


    def test_create_response_structure(self):
        """Test create response structure validation."""
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
            # Import and create proper request model instance
            from xdk.community_notes.models import CreateRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateRequest()
            # Call method and verify response structure
            method = getattr(self.community_notes_client, "create")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_search_eligible_posts_request_structure(self):
        """Test search_eligible_posts request structure."""
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
            kwargs["test_mode"] = True
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.community_notes_client, "search_eligible_posts")
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
                expected_path = "/2/notes/search/posts_eligible_for_notes"
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
                pytest.fail(f"Contract test failed for search_eligible_posts: {e}")


    def test_search_eligible_posts_required_parameters(self):
        """Test that search_eligible_posts handles parameters correctly."""
        method = getattr(self.community_notes_client, "search_eligible_posts")
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


    def test_search_eligible_posts_response_structure(self):
        """Test search_eligible_posts response structure validation."""
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
            kwargs["test_mode"] = True
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.community_notes_client, "search_eligible_posts")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_search_written_request_structure(self):
        """Test search_written request structure."""
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
            kwargs["test_mode"] = True
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.community_notes_client, "search_written")
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
                expected_path = "/2/notes/search/notes_written"
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
                pytest.fail(f"Contract test failed for search_written: {e}")


    def test_search_written_required_parameters(self):
        """Test that search_written handles parameters correctly."""
        method = getattr(self.community_notes_client, "search_written")
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


    def test_search_written_response_structure(self):
        """Test search_written response structure validation."""
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
            kwargs["test_mode"] = True
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.community_notes_client, "search_written")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
