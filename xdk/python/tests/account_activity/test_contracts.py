"""
Auto-generated contract tests for {"class_name": "AccountActivity", "display_name": "account activity", "import_name": "account_activity", "original": ["account", "activity"], "property_name": "account_activity"} client.

This module contains tests that validate the request/response contracts
of the {"class_name": "AccountActivity", "display_name": "account activity", "import_name": "account_activity", "original": ["account", "activity"], "property_name": "account_activity"} client against the OpenAPI specification.

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
    
    
    def test_get_subscription_count_request_structure(self):
        """Test get_subscription_count request structure."""
        
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
            
            
            # Add request body if required
            
            
            # Call the method
            try:
                method = getattr(self.account_activity_client, "get_subscription_count")
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
                    mock_streaming_response.__enter__ = Mock(return_value=mock_streaming_response)
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
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/account_activity/subscriptions/count"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(result, types.GeneratorType), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for get_subscription_count: {e}")
    
    def test_get_subscription_count_required_parameters(self):
        """Test that get_subscription_count handles parameters correctly."""
        method = getattr(self.account_activity_client, "get_subscription_count")
        
        
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
        
    
    def test_get_subscription_count_response_structure(self):
        """Test get_subscription_count response structure validation."""
        
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
            
            
            # Add request body if required
            
            
            # Call method and verify response structure
            method = getattr(self.account_activity_client, "get_subscription_count")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    def test_validate_subscription_request_structure(self):
        """Test validate_subscription request structure."""
        
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
            
            
            kwargs["webhook_id"] = "test_value"
            
            
            
            # Add request body if required
            
            
            # Call the method
            try:
                method = getattr(self.account_activity_client, "validate_subscription")
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
                    mock_streaming_response.__enter__ = Mock(return_value=mock_streaming_response)
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
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(result, types.GeneratorType), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for validate_subscription: {e}")
    
    def test_validate_subscription_required_parameters(self):
        """Test that validate_subscription handles parameters correctly."""
        method = getattr(self.account_activity_client, "validate_subscription")
        
        
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, 'session') as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.get.return_value = mock_response
            
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()
        
    
    def test_validate_subscription_response_structure(self):
        """Test validate_subscription response structure validation."""
        
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
            
            
            kwargs["webhook_id"] = "test"
            
            
            
            # Add request body if required
            
            
            # Call method and verify response structure
            method = getattr(self.account_activity_client, "validate_subscription")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    def test_create_subscription_request_structure(self):
        """Test create_subscription request structure."""
        
        # Mock the session to capture request details
        with patch.object(self.client, 'session') as mock_session:
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
            from xdk.account_activity.models import CreateSubscriptionRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateSubscriptionRequest()
            
            
            # Call the method
            try:
                method = getattr(self.account_activity_client, "create_subscription")
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
                    mock_streaming_response.__enter__ = Mock(return_value=mock_streaming_response)
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
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(result, types.GeneratorType), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for create_subscription: {e}")
    
    def test_create_subscription_required_parameters(self):
        """Test that create_subscription handles parameters correctly."""
        method = getattr(self.account_activity_client, "create_subscription")
        
        
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, 'session') as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.post.return_value = mock_response
            
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()
        
    
    def test_create_subscription_response_structure(self):
        """Test create_subscription response structure validation."""
        
        with patch.object(self.client, 'session') as mock_session:
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
            from xdk.account_activity.models import CreateSubscriptionRequest
            # Create instance with minimal valid data (empty instance should work for most cases)
            kwargs["body"] = CreateSubscriptionRequest()
            
            
            # Call method and verify response structure
            method = getattr(self.account_activity_client, "create_subscription")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    def test_create_replay_job_request_structure(self):
        """Test create_replay_job request structure."""
        
        # Mock the session to capture request details
        with patch.object(self.client, 'session') as mock_session:
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
                method = getattr(self.account_activity_client, "create_replay_job")
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
                    mock_streaming_response.__enter__ = Mock(return_value=mock_streaming_response)
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
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(result, types.GeneratorType), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for create_replay_job: {e}")
    
    def test_create_replay_job_required_parameters(self):
        """Test that create_replay_job handles parameters correctly."""
        method = getattr(self.account_activity_client, "create_replay_job")
        
        
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, 'session') as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.post.return_value = mock_response
            
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()
        
    
    def test_create_replay_job_response_structure(self):
        """Test create_replay_job response structure validation."""
        
        with patch.object(self.client, 'session') as mock_session:
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
            method = getattr(self.account_activity_client, "create_replay_job")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    def test_delete_subscription_request_structure(self):
        """Test delete_subscription request structure."""
        
        # Mock the session to capture request details
        with patch.object(self.client, 'session') as mock_session:
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
                method = getattr(self.account_activity_client, "delete_subscription")
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
                    mock_streaming_response.__enter__ = Mock(return_value=mock_streaming_response)
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
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(result, types.GeneratorType), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for delete_subscription: {e}")
    
    def test_delete_subscription_required_parameters(self):
        """Test that delete_subscription handles parameters correctly."""
        method = getattr(self.account_activity_client, "delete_subscription")
        
        
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, 'session') as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.delete.return_value = mock_response
            
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()
        
    
    def test_delete_subscription_response_structure(self):
        """Test delete_subscription response structure validation."""
        
        with patch.object(self.client, 'session') as mock_session:
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
            method = getattr(self.account_activity_client, "delete_subscription")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    
    def test_get_subscriptions_request_structure(self):
        """Test get_subscriptions request structure."""
        
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
            
            
            kwargs["webhook_id"] = "test_value"
            
            
            
            # Add request body if required
            
            
            # Call the method
            try:
                method = getattr(self.account_activity_client, "get_subscriptions")
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
                    mock_streaming_response.__enter__ = Mock(return_value=mock_streaming_response)
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
                called_url = call_args[0][0] if call_args[0] else call_args[1].get('url', '')
                expected_path = "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list"
                assert expected_path.replace('{', '').replace('}', '') in called_url or \
                       any(param in called_url for param in ["test_", "42"]), \
                       f"URL should contain path template elements: {called_url}"
                
                # Verify response structure
                if is_streaming:
                    # For streaming, verify we got a generator
                    assert isinstance(result, types.GeneratorType), "Streaming method should return a generator"
                else:
                    # For regular operations, verify we got a result
                    assert result is not None, "Method should return a result"
                
            except Exception as e:
                pytest.fail(f"Contract test failed for get_subscriptions: {e}")
    
    def test_get_subscriptions_required_parameters(self):
        """Test that get_subscriptions handles parameters correctly."""
        method = getattr(self.account_activity_client, "get_subscriptions")
        
        
        # Test with missing required parameters - mock the request to avoid network calls
        with patch.object(self.client, 'session') as mock_session:
            # Mock a 400 response (typical for missing required parameters)
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.return_value = {"error": "Missing required parameters"}
            mock_response.raise_for_status.side_effect = Exception("Bad Request")
            mock_session.get.return_value = mock_response
            
            # Call without required parameters should either raise locally or via server response
            with pytest.raises((TypeError, ValueError, Exception)):
                method()
        
    
    def test_get_subscriptions_response_structure(self):
        """Test get_subscriptions response structure validation."""
        
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
            
            
            kwargs["webhook_id"] = "test"
            
            
            
            # Add request body if required
            
            
            # Call method and verify response structure
            method = getattr(self.account_activity_client, "get_subscriptions")
            result = method(**kwargs)
            
            # Verify response object has expected attributes
            
            
            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(f"Accessing optional field 'data' should not cause errors: {e}")
            
            
    