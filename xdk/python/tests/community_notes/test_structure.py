"""
Auto-generated structural tests for {"class_name": "CommunityNotes", "display_name": "community notes", "import_name": "community_notes", "original": ["community", "notes"], "property_name": "community_notes"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "CommunityNotes", "display_name": "community notes", "import_name": "community_notes", "original": ["community", "notes"], "property_name": "community_notes"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.community_notes.client import CommunityNotesClient
from xdk import Client


class TestCommunityNotesStructure:
    """Test the structure of CommunityNotesClient."""
    
    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.community_notes_client = getattr(self.client, "community_notes")
    

    
    
    
    def test_search_written_exists(self):
        """Test that search_written method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "search_written", None)
        assert method is not None, f"Method search_written does not exist on CommunityNotesClient"
        
        # Check method is callable
        assert callable(method), f"search_written is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search_written should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "test_mode",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from search_written"
        
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
    
    def test_search_written_return_annotation(self):
        """Test that search_written has proper return type annotation."""
        method = getattr(CommunityNotesClient, "search_written")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method search_written should have return type annotation"
    
    
    def test_search_written_pagination_params(self):
        """Test that search_written has pagination parameters."""
        method = getattr(CommunityNotesClient, "search_written")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method search_written should have pagination parameters"
    
    
    
    def test_search_eligible_posts_exists(self):
        """Test that search_eligible_posts method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "search_eligible_posts", None)
        assert method is not None, f"Method search_eligible_posts does not exist on CommunityNotesClient"
        
        # Check method is callable
        assert callable(method), f"search_eligible_posts is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search_eligible_posts should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "test_mode",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from search_eligible_posts"
        
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
    
    def test_search_eligible_posts_return_annotation(self):
        """Test that search_eligible_posts has proper return type annotation."""
        method = getattr(CommunityNotesClient, "search_eligible_posts")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method search_eligible_posts should have return type annotation"
    
    
    def test_search_eligible_posts_pagination_params(self):
        """Test that search_eligible_posts has pagination parameters."""
        method = getattr(CommunityNotesClient, "search_eligible_posts")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have pagination-related parameters
        pagination_params = ['pagination_token', 'max_results', 'next_token', 'cursor', 'limit']
        has_pagination_param = any(param in params for param in pagination_params)
        assert has_pagination_param, \
            f"Paginated method search_eligible_posts should have pagination parameters"
    
    
    
    def test_create_exists(self):
        """Test that create method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "create", None)
        assert method is not None, f"Method create does not exist on CommunityNotesClient"
        
        # Check method is callable
        assert callable(method), f"create is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from create"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_create_return_annotation(self):
        """Test that create has proper return type annotation."""
        method = getattr(CommunityNotesClient, "create")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method create should have return type annotation"
    
    
    
    
    def test_delete_exists(self):
        """Test that delete method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "delete", None)
        assert method is not None, f"Method delete does not exist on CommunityNotesClient"
        
        # Check method is callable
        assert callable(method), f"delete is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
            "id",
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from delete"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_delete_return_annotation(self):
        """Test that delete has proper return type annotation."""
        method = getattr(CommunityNotesClient, "delete")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method delete should have return type annotation"
    
    
    
    
    def test_evaluate_exists(self):
        """Test that evaluate method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "evaluate", None)
        assert method is not None, f"Method evaluate does not exist on CommunityNotesClient"
        
        # Check method is callable
        assert callable(method), f"evaluate is not callable"
        
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"evaluate should have at least 'self' parameter"
        assert params[0] == 'self', f"First parameter should be 'self', got '{params[0]}'"
        
        # Check required parameters exist (excluding 'self')
        required_params = [
            
        ]
        
        for required_param in required_params:
            assert required_param in params, f"Required parameter '{required_param}' missing from evaluate"
        
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            
        ]
        
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert param_obj.default is not inspect.Parameter.empty, \
                    f"Optional parameter '{optional_param}' should have a default value"
    
    def test_evaluate_return_annotation(self):
        """Test that evaluate has proper return type annotation."""
        method = getattr(CommunityNotesClient, "evaluate")
        sig = inspect.signature(method)
        
        # Check return annotation exists
        assert sig.return_annotation is not inspect.Signature.empty, \
            f"Method evaluate should have return type annotation"
    
    
    
    
    
    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            
            "search_written",
            
            "search_eligible_posts",
            
            "create",
            
            "delete",
            
            "evaluate",
            
        ]
        
        for expected_method in expected_methods:
            assert hasattr(CommunityNotesClient, expected_method), \
                f"Expected method '{expected_method}' not found on CommunityNotesClient"
            assert callable(getattr(CommunityNotesClient, expected_method)), \
                f"'{expected_method}' exists but is not callable"
    
    
    