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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_stream_likes_compliance_request_structure(self):
        """Test streamLikesCompliance request structure."""
        
        # Mock the session to capture request details
        with patch.object(self.client, 'session') as mock_session:
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
            
            
            # Call the method
            try:
                method = getattr(self.likes_client, "stream_likes_compliance")
                result = method(**kwargs)
                
                # Verify the request was made
                mock_session.get.assert_called_once()
                
                # Verify request structure
                call_args = mock_session.get.call_args
                
                # Check URL structure
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/likes/compliance/stream"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for streamLikesCompliance: {e}")
    
    def test_stream_likes_compliance_required_parameters(self):
        """Test that streamLikesCompliance requires necessary parameters."""
        method = getattr(self.likes_client, "stream_likes_compliance")
        
        # Test with missing required parameters should fail
        
        # No required parameters, method should be callable without args
        with patch.object(self.client, 'session') as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            
            try:
                method()
            except Exception as e:
                pytest.fail(f"Method with no required params should be callable: {e}")
        
    
    def test_stream_likes_compliance_response_structure(self):
        """Test streamLikesCompliance response structure validation."""
        
        with patch.object(self.client, 'session') as mock_session:
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
            
            
            # Call method and verify response structure
            method = getattr(self.likes_client, "stream_likes_compliance")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_stream_likes_firehose_request_structure(self):
        """Test streamLikesFirehose request structure."""
        
        # Mock the session to capture request details
        with patch.object(self.client, 'session') as mock_session:
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
            
            
            
            # Call the method
            try:
                method = getattr(self.likes_client, "stream_likes_firehose")
                result = method(**kwargs)
                
                # Verify the request was made
                mock_session.get.assert_called_once()
                
                # Verify request structure
                call_args = mock_session.get.call_args
                
                # Check URL structure
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/likes/firehose/stream"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for streamLikesFirehose: {e}")
    
    def test_stream_likes_firehose_required_parameters(self):
        """Test that streamLikesFirehose requires necessary parameters."""
        method = getattr(self.likes_client, "stream_likes_firehose")
        
        # Test with missing required parameters should fail
        
        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()
        
    
    def test_stream_likes_firehose_response_structure(self):
        """Test streamLikesFirehose response structure validation."""
        
        with patch.object(self.client, 'session') as mock_session:
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
            
            
            
            # Call method and verify response structure
            method = getattr(self.likes_client, "stream_likes_firehose")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    
    
    
    
    
    
    def test_stream_likes_sample10_request_structure(self):
        """Test streamLikesSample10 request structure."""
        
        # Mock the session to capture request details
        with patch.object(self.client, 'session') as mock_session:
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
            
            
            
            # Call the method
            try:
                method = getattr(self.likes_client, "stream_likes_sample10")
                result = method(**kwargs)
                
                # Verify the request was made
                mock_session.get.assert_called_once()
                
                # Verify request structure
                call_args = mock_session.get.call_args
                
                # Check URL structure
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/likes/sample10/stream"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for streamLikesSample10: {e}")
    
    def test_stream_likes_sample10_required_parameters(self):
        """Test that streamLikesSample10 requires necessary parameters."""
        method = getattr(self.likes_client, "stream_likes_sample10")
        
        # Test with missing required parameters should fail
        
        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()
        
    
    def test_stream_likes_sample10_response_structure(self):
        """Test streamLikesSample10 response structure validation."""
        
        with patch.object(self.client, 'session') as mock_session:
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
            
            
            
            # Call method and verify response structure
            method = getattr(self.likes_client, "stream_likes_sample10")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_error_responses(self):
        """Test that error responses are handled correctly."""
        
        with patch.object(self.client, 'session') as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response
            
            # Pick first available method for testing
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            method = getattr(self.likes_client, "stream_likes_compliance")
            
            with pytest.raises(Exception):
                kwargs = {}
                
                method(**kwargs)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            