"""
Auto-generated structural tests for {"class_name": "Communities", "display_name": "communities", "import_name": "communities", "original": ["communities"], "property_name": "communities"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Communities", "display_name": "communities", "import_name": "communities", "original": ["communities"], "property_name": "communities"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.communities.client import CommunitiesClient
from xdk import Client


class TestCommunitiesStructure:
    """Test the structure of CommunitiesClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.communities_client = getattr(self.client, "communities")


    def test_get_by_id_exists(self):
        """Test that get_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(CommunitiesClient, "get_by_id", None)
        assert (
            method is not None
        ), f"Method get_by_id does not exist on CommunitiesClient"
        # Check method is callable
        assert callable(method), f"get_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_by_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_id_return_annotation(self):
        """Test that get_by_id has proper return type annotation."""
        method = getattr(CommunitiesClient, "get_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_id should have return type annotation"


    def test_search_exists(self):
        """Test that search method exists with correct signature."""
        # Check method exists
        method = getattr(CommunitiesClient, "search", None)
        assert method is not None, f"Method search does not exist on CommunitiesClient"
        # Check method is callable
        assert callable(method), f"search is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "query",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from search"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "next_token",
            "pagination_token",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_search_return_annotation(self):
        """Test that search has proper return type annotation."""
        method = getattr(CommunitiesClient, "search")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search should have return type annotation"


    def test_search_pagination_params(self):
        """Test that search has pagination parameters."""
        method = getattr(CommunitiesClient, "search")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have pagination-related parameters
        pagination_params = [
            "pagination_token",
            "max_results",
            "next_token",
            "cursor",
            "limit",
        ]
        has_pagination_param = any(param in params for param in pagination_params)
        assert (
            has_pagination_param
        ), f"Paginated method search should have pagination parameters"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_by_id",
            "search",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                CommunitiesClient, expected_method
            ), f"Expected method '{expected_method}' not found on CommunitiesClient"
            assert callable(
                getattr(CommunitiesClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
