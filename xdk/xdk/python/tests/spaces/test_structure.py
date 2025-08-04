"""
Auto-generated structural tests for Spaces client.

This module contains tests that validate the structure and API surface
of the Spaces client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.spaces.client import SpacesClient
from xdk import Client


class TestSpacesStructure:
    """Test the structure of SpacesClient."""
    
    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.spaces_client = getattr(self.client, "spaces")
    
    def test_client_exists(self):
        """Test that SpacesClient class exists and is importable."""
        assert SpacesClient is not None
        assert hasattr(SpacesClient, '__name__')
        assert SpacesClient.__name__ == "SpacesClient"
    
    def test_client_initialization(self):
        """Test that SpacesClient can be initialized properly."""
        assert self.spaces_client is not None
        assert isinstance(self.spaces_client, SpacesClient)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def test_get_spaces_by_ids_exists(self):
        """Test that get_spaces_by_ids method exists with correct signature."""
        # Check method exists
        method = getattr(SpacesClient, "get_spaces_by_ids", None)
        assert method is not None, f"Method get_spaces_by_ids does not exist on SpacesClient"
        
        # Check method is callable
        assert callable(method), f"get_spaces_by_ids is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_spaces_by_ids should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "ids",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_spaces_by_ids"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_spaces_by_ids_return_annotation(self):
        """Test that get_spaces_by_ids has proper return type annotation."""
        method = getattr(SpacesClient, "get_spaces_by_ids")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_spaces_by_ids should have return type annotation"
    
    
    
    
    def test_get_spaces_by_creator_ids_exists(self):
        """Test that get_spaces_by_creator_ids method exists with correct signature."""
        # Check method exists
        method = getattr(SpacesClient, "get_spaces_by_creator_ids", None)
        assert method is not None, f"Method get_spaces_by_creator_ids does not exist on SpacesClient"
        
        # Check method is callable
        assert callable(method), f"get_spaces_by_creator_ids is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_spaces_by_creator_ids should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "user_ids",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_spaces_by_creator_ids"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_spaces_by_creator_ids_return_annotation(self):
        """Test that get_spaces_by_creator_ids has proper return type annotation."""
        method = getattr(SpacesClient, "get_spaces_by_creator_ids")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_spaces_by_creator_ids should have return type annotation"
    
    
    
    
    def test_get_spaces_buyers_exists(self):
        """Test that get_spaces_buyers method exists with correct signature."""
        # Check method exists
        method = getattr(SpacesClient, "get_spaces_buyers", None)
        assert method is not None, f"Method get_spaces_buyers does not exist on SpacesClient"
        
        # Check method is callable
        assert callable(method), f"get_spaces_buyers is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_spaces_buyers should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_spaces_buyers"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "pagination_token",
            
            "max_results",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_spaces_buyers_return_annotation(self):
        """Test that get_spaces_buyers has proper return type annotation."""
        method = getattr(SpacesClient, "get_spaces_buyers")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_spaces_buyers should have return type annotation"
    
    
    def test_get_spaces_buyers_pagination_params(self):
        """Test that get_spaces_buyers has pagination parameters."""
        method = getattr(SpacesClient, "get_spaces_buyers")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method get_spaces_buyers should have pagination parameters"
    
    
    
    def test_get_spaces_by_id_exists(self):
        """Test that get_spaces_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(SpacesClient, "get_spaces_by_id", None)
        assert method is not None, f"Method get_spaces_by_id does not exist on SpacesClient"
        
        # Check method is callable
        assert callable(method), f"get_spaces_by_id is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_spaces_by_id should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_spaces_by_id"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_spaces_by_id_return_annotation(self):
        """Test that get_spaces_by_id has proper return type annotation."""
        method = getattr(SpacesClient, "get_spaces_by_id")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_spaces_by_id should have return type annotation"
    
    
    
    
    def test_search_spaces_exists(self):
        """Test that search_spaces method exists with correct signature."""
        # Check method exists
        method = getattr(SpacesClient, "search_spaces", None)
        assert method is not None, f"Method search_spaces does not exist on SpacesClient"
        
        # Check method is callable
        assert callable(method), f"search_spaces is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search_spaces should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "query",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from search_spaces"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "state",
            
            "max_results",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_search_spaces_return_annotation(self):
        """Test that search_spaces has proper return type annotation."""
        method = getattr(SpacesClient, "search_spaces")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method search_spaces should have return type annotation"
    
    
    def test_search_spaces_pagination_params(self):
        """Test that search_spaces has pagination parameters."""
        method = getattr(SpacesClient, "search_spaces")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method search_spaces should have pagination parameters"
    
    
    
    def test_get_spaces_posts_exists(self):
        """Test that get_spaces_posts method exists with correct signature."""
        # Check method exists
        method = getattr(SpacesClient, "get_spaces_posts", None)
        assert method is not None, f"Method get_spaces_posts does not exist on SpacesClient"
        
        # Check method is callable
        assert callable(method), f"get_spaces_posts is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_spaces_posts should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from get_spaces_posts"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
            "max_results",
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_get_spaces_posts_return_annotation(self):
        """Test that get_spaces_posts has proper return type annotation."""
        method = getattr(SpacesClient, "get_spaces_posts")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method get_spaces_posts should have return type annotation"
    
    
    def test_get_spaces_posts_pagination_params(self):
        """Test that get_spaces_posts has pagination parameters."""
        method = getattr(SpacesClient, "get_spaces_posts")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method get_spaces_posts should have pagination parameters"
    
    
    
    
    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            
            "get_spaces_by_ids",
            
            "get_spaces_by_creator_ids",
            
            "get_spaces_buyers",
            
            "get_spaces_by_id",
            
            "search_spaces",
            
            "get_spaces_posts",
            
        ]
        
        client_methods = [name for name in dir(SpacesClient) 
                         if not name.startswith('_') and callable(getattr(SpacesClient, name))]
        
        for expected_method in expected_methods:
            assert expected_method in client_methods, \
                f"Expected method '{expected_method}' not found on SpacesClient"
    
    def test_no_unexpected_public_methods(self):
        """Test that no unexpected public methods exist (helps catch API drift)."""
        expected_methods = set([
            
            "get_spaces_by_ids",
            
            "get_spaces_by_creator_ids",
            
            "get_spaces_buyers",
            
            "get_spaces_by_id",
            
            "search_spaces",
            
            "get_spaces_posts",
            
        ])
        
        actual_methods = set([name for name in dir(SpacesClient) 
                            if not name.startswith('_') and callable(getattr(SpacesClient, name))])
        
        # Remove standard methods that might be inherited
        standard_methods = {'__init__'}
        actual_methods = actual_methods - standard_methods
        
        unexpected_methods = actual_methods - expected_methods
        
        # This is a warning, not a failure, since new methods might be added
        if unexpected_methods:
            print(f"Warning: Unexpected methods found on SpacesClient: {unexpected_methods}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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