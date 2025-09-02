"""
Auto-generated contract tests for {"class_name": "Media", "display_name": "media", "import_name": "media", "original": ["media"], "property_name": "media"} client.

This module contains tests that validate the request/response contracts
of the {"class_name": "Media", "display_name": "media", "import_name": "media", "original": ["media"], "property_name": "media"} client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.media.client import MediaClient
from xdk import Client


class TestMediaContracts:
    """Test the API contracts of MediaClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.media_client = getattr(self.client, "media")


    def test_create_metadata_request_structure(self):
        """Test create_metadata request structure."""
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
            from xdk.media.models import CreateMetadataRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateMetadataRequest()
            # Call the method
            try:
                method = getattr(self.media_client, "create_metadata")
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
                expected_path = "/2/media/metadata"
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
                pytest.fail(f"Contract test failed for create_metadata: {e}")


    def test_create_metadata_required_parameters(self):
        """Test that create_metadata handles parameters correctly."""
        method = getattr(self.media_client, "create_metadata")
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


    def test_create_metadata_response_structure(self):
        """Test create_metadata response structure validation."""
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
            from xdk.media.models import CreateMetadataRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateMetadataRequest()
            # Call method and verify response structure
            method = getattr(self.media_client, "create_metadata")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_analytics_request_structure(self):
        """Test get_analytics request structure."""
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
            kwargs["media_keys"] = ["test_item"]
            kwargs["end_time"] = "test_end_time"
            kwargs["start_time"] = "test_start_time"
            kwargs["granularity"] = "test_granularity"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.media_client, "get_analytics")
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
                expected_path = "/2/media/analytics"
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
                pytest.fail(f"Contract test failed for get_analytics: {e}")


    def test_get_analytics_required_parameters(self):
        """Test that get_analytics handles parameters correctly."""
        method = getattr(self.media_client, "get_analytics")
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


    def test_get_analytics_response_structure(self):
        """Test get_analytics response structure validation."""
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
            kwargs["media_keys"] = ["test"]
            kwargs["end_time"] = "test_value"
            kwargs["start_time"] = "test_value"
            kwargs["granularity"] = "test_value"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.media_client, "get_analytics")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_by_keys_request_structure(self):
        """Test get_by_keys request structure."""
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
            kwargs["media_keys"] = ["test_item"]
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.media_client, "get_by_keys")
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
                expected_path = "/2/media"
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
                pytest.fail(f"Contract test failed for get_by_keys: {e}")


    def test_get_by_keys_required_parameters(self):
        """Test that get_by_keys handles parameters correctly."""
        method = getattr(self.media_client, "get_by_keys")
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


    def test_get_by_keys_response_structure(self):
        """Test get_by_keys response structure validation."""
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
            kwargs["media_keys"] = ["test"]
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.media_client, "get_by_keys")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_finalize_upload_request_structure(self):
        """Test finalize_upload request structure."""
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
                method = getattr(self.media_client, "finalize_upload")
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
                expected_path = "/2/media/upload/{id}/finalize"
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
                pytest.fail(f"Contract test failed for finalize_upload: {e}")


    def test_finalize_upload_required_parameters(self):
        """Test that finalize_upload handles parameters correctly."""
        method = getattr(self.media_client, "finalize_upload")
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


    def test_finalize_upload_response_structure(self):
        """Test finalize_upload response structure validation."""
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
            method = getattr(self.media_client, "finalize_upload")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_append_upload_request_structure(self):
        """Test append_upload request structure."""
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
            from xdk.media.models import AppendUploadRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = AppendUploadRequest()
            # Call the method
            try:
                method = getattr(self.media_client, "append_upload")
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
                expected_path = "/2/media/upload/{id}/append"
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
                pytest.fail(f"Contract test failed for append_upload: {e}")


    def test_append_upload_required_parameters(self):
        """Test that append_upload handles parameters correctly."""
        method = getattr(self.media_client, "append_upload")
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


    def test_append_upload_response_structure(self):
        """Test append_upload response structure validation."""
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
            from xdk.media.models import AppendUploadRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = AppendUploadRequest()
            # Call method and verify response structure
            method = getattr(self.media_client, "append_upload")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_upload_status_request_structure(self):
        """Test get_upload_status request structure."""
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
            kwargs["media_id"] = "test_value"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.media_client, "get_upload_status")
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
                expected_path = "/2/media/upload"
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
                pytest.fail(f"Contract test failed for get_upload_status: {e}")


    def test_get_upload_status_required_parameters(self):
        """Test that get_upload_status handles parameters correctly."""
        method = getattr(self.media_client, "get_upload_status")
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


    def test_get_upload_status_response_structure(self):
        """Test get_upload_status response structure validation."""
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
            kwargs["media_id"] = "test"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.media_client, "get_upload_status")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_upload_request_structure(self):
        """Test upload request structure."""
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
            from xdk.media.models import UploadRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = UploadRequest()
            # Call the method
            try:
                method = getattr(self.media_client, "upload")
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
                expected_path = "/2/media/upload"
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
                pytest.fail(f"Contract test failed for upload: {e}")


    def test_upload_required_parameters(self):
        """Test that upload handles parameters correctly."""
        method = getattr(self.media_client, "upload")
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


    def test_upload_response_structure(self):
        """Test upload response structure validation."""
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
            from xdk.media.models import UploadRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = UploadRequest()
            # Call method and verify response structure
            method = getattr(self.media_client, "upload")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_create_subtitles_request_structure(self):
        """Test create_subtitles request structure."""
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
            from xdk.media.models import CreateSubtitlesRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateSubtitlesRequest()
            # Call the method
            try:
                method = getattr(self.media_client, "create_subtitles")
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
                expected_path = "/2/media/subtitles"
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
                pytest.fail(f"Contract test failed for create_subtitles: {e}")


    def test_create_subtitles_required_parameters(self):
        """Test that create_subtitles handles parameters correctly."""
        method = getattr(self.media_client, "create_subtitles")
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


    def test_create_subtitles_response_structure(self):
        """Test create_subtitles response structure validation."""
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
            from xdk.media.models import CreateSubtitlesRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateSubtitlesRequest()
            # Call method and verify response structure
            method = getattr(self.media_client, "create_subtitles")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_delete_subtitles_request_structure(self):
        """Test delete_subtitles request structure."""
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
            # Add request body if required
            # Import and create proper request model instance
            from xdk.media.models import DeleteSubtitlesRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = DeleteSubtitlesRequest()
            # Call the method
            try:
                method = getattr(self.media_client, "delete_subtitles")
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
                expected_path = "/2/media/subtitles"
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
                pytest.fail(f"Contract test failed for delete_subtitles: {e}")


    def test_delete_subtitles_required_parameters(self):
        """Test that delete_subtitles handles parameters correctly."""
        method = getattr(self.media_client, "delete_subtitles")
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


    def test_delete_subtitles_response_structure(self):
        """Test delete_subtitles response structure validation."""
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
            # Add request body if required
            # Import and create proper request model instance
            from xdk.media.models import DeleteSubtitlesRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = DeleteSubtitlesRequest()
            # Call method and verify response structure
            method = getattr(self.media_client, "delete_subtitles")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_initialize_upload_request_structure(self):
        """Test initialize_upload request structure."""
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
            from xdk.media.models import InitializeUploadRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = InitializeUploadRequest()
            # Call the method
            try:
                method = getattr(self.media_client, "initialize_upload")
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
                expected_path = "/2/media/upload/initialize"
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
                pytest.fail(f"Contract test failed for initialize_upload: {e}")


    def test_initialize_upload_required_parameters(self):
        """Test that initialize_upload handles parameters correctly."""
        method = getattr(self.media_client, "initialize_upload")
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


    def test_initialize_upload_response_structure(self):
        """Test initialize_upload response structure validation."""
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
            from xdk.media.models import InitializeUploadRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = InitializeUploadRequest()
            # Call method and verify response structure
            method = getattr(self.media_client, "initialize_upload")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_by_key_request_structure(self):
        """Test get_by_key request structure."""
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
            kwargs["media_key"] = "test_value"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.media_client, "get_by_key")
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
                expected_path = "/2/media/{media_key}"
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
                pytest.fail(f"Contract test failed for get_by_key: {e}")


    def test_get_by_key_required_parameters(self):
        """Test that get_by_key handles parameters correctly."""
        method = getattr(self.media_client, "get_by_key")
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


    def test_get_by_key_response_structure(self):
        """Test get_by_key response structure validation."""
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
            kwargs["media_key"] = "test"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.media_client, "get_by_key")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
