"""
Auto-generated structural tests for Direct_Messages client.

This module contains tests that validate the structure and API surface
of the Direct_Messages client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.direct_messages.client import DirectMessagesClient
from xdk import Client


class TestDirectMessagesStructure:
    """Test the structure of DirectMessagesClient."""
    
    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.direct_messages_client = getattr(self.client, "direct_messages")
    
    def test_client_exists(self):
        """Test that DirectMessagesClient class exists and is importable."""
        assert DirectMessagesClient is not None
        assert hasattr(DirectMessagesClient, '__name__')
        assert DirectMessagesClient.__name__ == "DirectMessagesClient"
    
    def test_client_initialization(self):
        """Test that DirectMessagesClient can be initialized properly."""
        assert self.direct_messages_client is not None
        assert isinstance(self.direct_messages_client, DirectMessagesClient)
    
    
    
    
    
    
    
    
    
    
    
    
    def test_get_dm_events_by_participant_id_exists(self):
        """Test that get_dm_events_by_participant_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_dm_events_by_participant_id", None)
        assert method is not None, f"Method get_dm_events_by_participant_id does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"get_dm_events_by_participant_id is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_dm_events_by_participant_id should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "participant_id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_dm_events_by_participant_id"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "max_results",
            
            "pagination_token",
            
            "event_types",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_dm_events_by_participant_id_return_annotation(self):
        """Test that get_dm_events_by_participant_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_dm_events_by_participant_id")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_dm_events_by_participant_id should have return type annotation"
    
    
    def test_get_dm_events_by_participant_id_pagination_params(self):
        """Test that get_dm_events_by_participant_id has pagination parameters."""
        method = getattr(DirectMessagesClient, "get_dm_events_by_participant_id")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method get_dm_events_by_participant_id should have pagination parameters"
    
    
    
    def test_get_dm_events_exists(self):
        """Test that get_dm_events method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_dm_events", None)
        assert method is not None, f"Method get_dm_events does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"get_dm_events is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_dm_events should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_dm_events"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "max_results",
            
            "pagination_token",
            
            "event_types",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_dm_events_return_annotation(self):
        """Test that get_dm_events has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_dm_events")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_dm_events should have return type annotation"
    
    
    def test_get_dm_events_pagination_params(self):
        """Test that get_dm_events has pagination parameters."""
        method = getattr(DirectMessagesClient, "get_dm_events")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method get_dm_events should have pagination parameters"
    
    
    
    def test_get_dm_conversations_id_dm_events_exists(self):
        """Test that get_dm_conversations_id_dm_events method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_dm_conversations_id_dm_events", None)
        assert method is not None, f"Method get_dm_conversations_id_dm_events does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"get_dm_conversations_id_dm_events is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_dm_conversations_id_dm_events should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_dm_conversations_id_dm_events"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "max_results",
            
            "pagination_token",
            
            "event_types",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_dm_conversations_id_dm_events_return_annotation(self):
        """Test that get_dm_conversations_id_dm_events has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_dm_conversations_id_dm_events")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_dm_conversations_id_dm_events should have return type annotation"
    
    
    def test_get_dm_conversations_id_dm_events_pagination_params(self):
        """Test that get_dm_conversations_id_dm_events has pagination parameters."""
        method = getattr(DirectMessagesClient, "get_dm_conversations_id_dm_events")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method get_dm_conversations_id_dm_events should have pagination parameters"
    
    
    
    def test_create_dm_by_conversation_id_exists(self):
        """Test that create_dm_by_conversation_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "create_dm_by_conversation_id", None)
        assert method is not None, f"Method create_dm_by_conversation_id does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"create_dm_by_conversation_id is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_dm_by_conversation_id should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "dm_conversation_id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from create_dm_by_conversation_id"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_create_dm_by_conversation_id_return_annotation(self):
        """Test that create_dm_by_conversation_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "create_dm_by_conversation_id")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method create_dm_by_conversation_id should have return type annotation"
    
    
    
    
    def test_get_dm_events_by_id_exists(self):
        """Test that get_dm_events_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_dm_events_by_id", None)
        assert method is not None, f"Method get_dm_events_by_id does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"get_dm_events_by_id is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_dm_events_by_id should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "event_id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_dm_events_by_id"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_dm_events_by_id_return_annotation(self):
        """Test that get_dm_events_by_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_dm_events_by_id")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_dm_events_by_id should have return type annotation"
    
    
    
    
    def test_delete_dm_events_exists(self):
        """Test that delete_dm_events method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "delete_dm_events", None)
        assert method is not None, f"Method delete_dm_events does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"delete_dm_events is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete_dm_events should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "event_id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from delete_dm_events"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_delete_dm_events_return_annotation(self):
        """Test that delete_dm_events has proper return type annotation."""
        method = getattr(DirectMessagesClient, "delete_dm_events")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method delete_dm_events should have return type annotation"
    
    
    
    
    def test_create_dm_conversations_exists(self):
        """Test that create_dm_conversations method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "create_dm_conversations", None)
        assert method is not None, f"Method create_dm_conversations does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"create_dm_conversations is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_dm_conversations should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from create_dm_conversations"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_create_dm_conversations_return_annotation(self):
        """Test that create_dm_conversations has proper return type annotation."""
        method = getattr(DirectMessagesClient, "create_dm_conversations")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method create_dm_conversations should have return type annotation"
    
    
    
    
    def test_create_dm_by_participant_id_exists(self):
        """Test that create_dm_by_participant_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "create_dm_by_participant_id", None)
        assert method is not None, f"Method create_dm_by_participant_id does not exist on DirectMessagesClient"
        
        # Check method is callable
        assert callable(method), f"create_dm_by_participant_id is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_dm_by_participant_id should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "participant_id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from create_dm_by_participant_id"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_create_dm_by_participant_id_return_annotation(self):
        """Test that create_dm_by_participant_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "create_dm_by_participant_id")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method create_dm_by_participant_id should have return type annotation"
    
    
    
    
    
    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            
            "get_dm_events_by_participant_id",
            
            "get_dm_events",
            
            "get_dm_conversations_id_dm_events",
            
            "create_dm_by_conversation_id",
            
            "get_dm_events_by_id",
            
            "delete_dm_events",
            
            "create_dm_conversations",
            
            "create_dm_by_participant_id",
            
        ]
        
        client_methods = [name for name in dir(DirectMessagesClient) 
                         if not name.startswith('_') and callable(getattr(DirectMessagesClient, name))]
        
        for expected_method in expected_methods:
            assert expected_method in client_methods, \
                f"Expected method '{expected_method}' not found on DirectMessagesClient"
    
    def test_no_unexpected_public_methods(self):
        """Test that no unexpected public methods exist (helps catch API drift)."""
        expected_methods = set([
            
            "get_dm_events_by_participant_id",
            
            "get_dm_events",
            
            "get_dm_conversations_id_dm_events",
            
            "create_dm_by_conversation_id",
            
            "get_dm_events_by_id",
            
            "delete_dm_events",
            
            "create_dm_conversations",
            
            "create_dm_by_participant_id",
            
        ])
        
        actual_methods = set([name for name in dir(DirectMessagesClient) 
                            if not name.startswith('_') and callable(getattr(DirectMessagesClient, name))])
        
        # Remove standard methods that might be inherited
        standard_methods = {'__init__'}
        actual_methods = actual_methods - standard_methods
        
        unexpected_methods = actual_methods - expected_methods
        
        # This is a warning, not a failure, since new methods might be added
        if unexpected_methods:
            print(f"Warning: Unexpected methods found on DirectMessagesClient: {unexpected_methods}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_imports_work(self):
        """Test that all expected imports work correctly."""
        expected_imports = [
            
            
            
            
            
            
            
            
            
            
            
            "typing",
            
            "requests",
            
            "pydantic",
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        ]
        
        for import_name in expected_imports:
            try:
                __import__(import_name)
            except ImportError as e:
                pytest.fail(f"Expected import '{import_name}' failed: {e}")