"""
Auto-generated contract tests for {"class_name": "Compliance", "display_name": "compliance", "import_name": "compliance", "original": ["compliance"], "property_name": "compliance"} client.

This module contains tests that validate the request/response contracts
of the {"class_name": "Compliance", "display_name": "compliance", "import_name": "compliance", "original": ["compliance"], "property_name": "compliance"} client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.compliance.client import ComplianceClient
from xdk import Client


class TestComplianceContracts:
    """Test the API contracts of ComplianceClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.compliance_client = getattr(self.client, "compliance")


    def test_get_jobs_by_id_request_structure(self):
        """Test get_jobs_by_id request structure."""
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
                method = getattr(self.compliance_client, "get_jobs_by_id")
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
                expected_path = "/2/compliance/jobs/{id}"
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
                pytest.fail(f"Contract test failed for get_jobs_by_id: {e}")


    def test_get_jobs_by_id_required_parameters(self):
        """Test that get_jobs_by_id handles parameters correctly."""
        method = getattr(self.compliance_client, "get_jobs_by_id")
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


    def test_get_jobs_by_id_response_structure(self):
        """Test get_jobs_by_id response structure validation."""
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
            method = getattr(self.compliance_client, "get_jobs_by_id")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_get_jobs_request_structure(self):
        """Test get_jobs request structure."""
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
            kwargs["type"] = "test_type"
            # Add request body if required
            # Call the method
            try:
                method = getattr(self.compliance_client, "get_jobs")
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
                expected_path = "/2/compliance/jobs"
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
                pytest.fail(f"Contract test failed for get_jobs: {e}")


    def test_get_jobs_required_parameters(self):
        """Test that get_jobs handles parameters correctly."""
        method = getattr(self.compliance_client, "get_jobs")
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


    def test_get_jobs_response_structure(self):
        """Test get_jobs response structure validation."""
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
            kwargs["type"] = "test_value"
            # Add request body if required
            # Call method and verify response structure
            method = getattr(self.compliance_client, "get_jobs")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_create_jobs_request_structure(self):
        """Test create_jobs request structure."""
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
            from xdk.compliance.models import CreateJobsRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateJobsRequest()
            # Call the method
            try:
                method = getattr(self.compliance_client, "create_jobs")
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
                expected_path = "/2/compliance/jobs"
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
                pytest.fail(f"Contract test failed for create_jobs: {e}")


    def test_create_jobs_required_parameters(self):
        """Test that create_jobs handles parameters correctly."""
        method = getattr(self.compliance_client, "create_jobs")
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


    def test_create_jobs_response_structure(self):
        """Test create_jobs response structure validation."""
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
            from xdk.compliance.models import CreateJobsRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateJobsRequest()
            # Call method and verify response structure
            method = getattr(self.compliance_client, "create_jobs")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
