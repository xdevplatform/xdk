"""
Auto-generated contract tests for {"class_name": "Stream", "display_name": "stream", "import_name": "stream", "original": ["stream"], "property_name": "stream"} client.

This module contains tests that validate the request/response contracts
of the {"class_name": "Stream", "display_name": "stream", "import_name": "stream", "original": ["stream"], "property_name": "stream"} client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.stream.client import StreamClient
from xdk import Client


class TestStreamContracts:
    """Test the API contracts of StreamClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.stream_client = getattr(self.client, "stream")


    def test_likes_sample10_request_structure(self):
        """Test likes_sample10 request structure."""
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
                method = getattr(self.stream_client, "likes_sample10")
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
                pytest.fail(f"Contract test failed for likes_sample10: {e}")


    def test_likes_sample10_required_parameters(self):
        """Test that likes_sample10 handles parameters correctly."""
        method = getattr(self.stream_client, "likes_sample10")
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


    def test_likes_sample10_response_structure(self):
        """Test likes_sample10 response structure validation."""
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
            method = getattr(self.stream_client, "likes_sample10")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_sample_request_structure(self):
        """Test posts_sample request structure."""
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
                method = getattr(self.stream_client, "posts_sample")
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
                pytest.fail(f"Contract test failed for posts_sample: {e}")


    def test_posts_sample_required_parameters(self):
        """Test that posts_sample handles parameters correctly."""
        method = getattr(self.stream_client, "posts_sample")
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


    def test_posts_sample_response_structure(self):
        """Test posts_sample response structure validation."""
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
            method = getattr(self.stream_client, "posts_sample")
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
        """Test get_rule_counts request structure."""
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
                method = getattr(self.stream_client, "get_rule_counts")
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
                pytest.fail(f"Contract test failed for get_rule_counts: {e}")


    def test_get_rule_counts_required_parameters(self):
        """Test that get_rule_counts handles parameters correctly."""
        method = getattr(self.stream_client, "get_rule_counts")
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
        """Test get_rule_counts response structure validation."""
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
            method = getattr(self.stream_client, "get_rule_counts")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_firehose_pt_request_structure(self):
        """Test posts_firehose_pt request structure."""
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
                method = getattr(self.stream_client, "posts_firehose_pt")
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
                pytest.fail(f"Contract test failed for posts_firehose_pt: {e}")


    def test_posts_firehose_pt_required_parameters(self):
        """Test that posts_firehose_pt handles parameters correctly."""
        method = getattr(self.stream_client, "posts_firehose_pt")
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


    def test_posts_firehose_pt_response_structure(self):
        """Test posts_firehose_pt response structure validation."""
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
            method = getattr(self.stream_client, "posts_firehose_pt")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_labels_compliance_request_structure(self):
        """Test labels_compliance request structure."""
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
                method = getattr(self.stream_client, "labels_compliance")
                result = method(**kwargs)
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/label/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for labels_compliance: {e}")


    def test_labels_compliance_required_parameters(self):
        """Test that labels_compliance handles parameters correctly."""
        method = getattr(self.stream_client, "labels_compliance")
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


    def test_labels_compliance_response_structure(self):
        """Test labels_compliance response structure validation."""
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
            method = getattr(self.stream_client, "labels_compliance")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_likes_firehose_request_structure(self):
        """Test likes_firehose request structure."""
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
                method = getattr(self.stream_client, "likes_firehose")
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
                pytest.fail(f"Contract test failed for likes_firehose: {e}")


    def test_likes_firehose_required_parameters(self):
        """Test that likes_firehose handles parameters correctly."""
        method = getattr(self.stream_client, "likes_firehose")
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


    def test_likes_firehose_response_structure(self):
        """Test likes_firehose response structure validation."""
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
            method = getattr(self.stream_client, "likes_firehose")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_request_structure(self):
        """Test posts request structure."""
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
                method = getattr(self.stream_client, "posts")
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
                pytest.fail(f"Contract test failed for posts: {e}")


    def test_posts_required_parameters(self):
        """Test that posts handles parameters correctly."""
        method = getattr(self.stream_client, "posts")
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


    def test_posts_response_structure(self):
        """Test posts response structure validation."""
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
            method = getattr(self.stream_client, "posts")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_firehose_request_structure(self):
        """Test posts_firehose request structure."""
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
                method = getattr(self.stream_client, "posts_firehose")
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
                pytest.fail(f"Contract test failed for posts_firehose: {e}")


    def test_posts_firehose_required_parameters(self):
        """Test that posts_firehose handles parameters correctly."""
        method = getattr(self.stream_client, "posts_firehose")
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


    def test_posts_firehose_response_structure(self):
        """Test posts_firehose response structure validation."""
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
            method = getattr(self.stream_client, "posts_firehose")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_compliance_request_structure(self):
        """Test posts_compliance request structure."""
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
                method = getattr(self.stream_client, "posts_compliance")
                result = method(**kwargs)
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/compliance/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for posts_compliance: {e}")


    def test_posts_compliance_required_parameters(self):
        """Test that posts_compliance handles parameters correctly."""
        method = getattr(self.stream_client, "posts_compliance")
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


    def test_posts_compliance_response_structure(self):
        """Test posts_compliance response structure validation."""
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
            method = getattr(self.stream_client, "posts_compliance")
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
        """Test get_rules request structure."""
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
                method = getattr(self.stream_client, "get_rules")
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
                pytest.fail(f"Contract test failed for get_rules: {e}")


    def test_get_rules_required_parameters(self):
        """Test that get_rules handles parameters correctly."""
        method = getattr(self.stream_client, "get_rules")
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
        """Test get_rules response structure validation."""
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
            method = getattr(self.stream_client, "get_rules")
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
        """Test update_rules request structure."""
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
            from xdk.stream.models import UpdateRulesRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = UpdateRulesRequest()
            # Call the method
            try:
                method = getattr(self.stream_client, "update_rules")
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
                pytest.fail(f"Contract test failed for update_rules: {e}")


    def test_update_rules_required_parameters(self):
        """Test that update_rules handles parameters correctly."""
        method = getattr(self.stream_client, "update_rules")
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


    def test_update_rules_response_structure(self):
        """Test update_rules response structure validation."""
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
            from xdk.stream.models import UpdateRulesRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = UpdateRulesRequest()
            # Call method and verify response structure
            method = getattr(self.stream_client, "update_rules")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_likes_compliance_request_structure(self):
        """Test likes_compliance request structure."""
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
                method = getattr(self.stream_client, "likes_compliance")
                result = method(**kwargs)
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/likes/compliance/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for likes_compliance: {e}")


    def test_likes_compliance_required_parameters(self):
        """Test that likes_compliance handles parameters correctly."""
        method = getattr(self.stream_client, "likes_compliance")
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


    def test_likes_compliance_response_structure(self):
        """Test likes_compliance response structure validation."""
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
            method = getattr(self.stream_client, "likes_compliance")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_users_compliance_request_structure(self):
        """Test users_compliance request structure."""
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
                method = getattr(self.stream_client, "users_compliance")
                result = method(**kwargs)
                # Verify the request was made
                mock_session.get.assert_called_once()
                # Verify request structure
                call_args = mock_session.get.call_args
                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/compliance/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"
                # Verify response structure
                assert result is not None, "Method should return a result"
            except Exception as e:
                pytest.fail(f"Contract test failed for users_compliance: {e}")


    def test_users_compliance_required_parameters(self):
        """Test that users_compliance handles parameters correctly."""
        method = getattr(self.stream_client, "users_compliance")
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


    def test_users_compliance_response_structure(self):
        """Test users_compliance response structure validation."""
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
            method = getattr(self.stream_client, "users_compliance")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_firehose_en_request_structure(self):
        """Test posts_firehose_en request structure."""
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
                method = getattr(self.stream_client, "posts_firehose_en")
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
                pytest.fail(f"Contract test failed for posts_firehose_en: {e}")


    def test_posts_firehose_en_required_parameters(self):
        """Test that posts_firehose_en handles parameters correctly."""
        method = getattr(self.stream_client, "posts_firehose_en")
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


    def test_posts_firehose_en_response_structure(self):
        """Test posts_firehose_en response structure validation."""
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
            method = getattr(self.stream_client, "posts_firehose_en")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_firehose_ja_request_structure(self):
        """Test posts_firehose_ja request structure."""
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
                method = getattr(self.stream_client, "posts_firehose_ja")
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
                pytest.fail(f"Contract test failed for posts_firehose_ja: {e}")


    def test_posts_firehose_ja_required_parameters(self):
        """Test that posts_firehose_ja handles parameters correctly."""
        method = getattr(self.stream_client, "posts_firehose_ja")
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


    def test_posts_firehose_ja_response_structure(self):
        """Test posts_firehose_ja response structure validation."""
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
            method = getattr(self.stream_client, "posts_firehose_ja")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_firehose_ko_request_structure(self):
        """Test posts_firehose_ko request structure."""
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
                method = getattr(self.stream_client, "posts_firehose_ko")
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
                pytest.fail(f"Contract test failed for posts_firehose_ko: {e}")


    def test_posts_firehose_ko_required_parameters(self):
        """Test that posts_firehose_ko handles parameters correctly."""
        method = getattr(self.stream_client, "posts_firehose_ko")
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


    def test_posts_firehose_ko_response_structure(self):
        """Test posts_firehose_ko response structure validation."""
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
            method = getattr(self.stream_client, "posts_firehose_ko")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )


    def test_posts_sample10_request_structure(self):
        """Test posts_sample10 request structure."""
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
                method = getattr(self.stream_client, "posts_sample10")
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
                pytest.fail(f"Contract test failed for posts_sample10: {e}")


    def test_posts_sample10_required_parameters(self):
        """Test that posts_sample10 handles parameters correctly."""
        method = getattr(self.stream_client, "posts_sample10")
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


    def test_posts_sample10_response_structure(self):
        """Test posts_sample10 response structure validation."""
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
            method = getattr(self.stream_client, "posts_sample10")
            result = method(**kwargs)
            # Verify response object has expected attributes
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )
