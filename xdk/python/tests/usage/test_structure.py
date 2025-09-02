"""
Auto-generated structural tests for {"class_name": "Usage", "display_name": "usage", "import_name": "usage", "original": ["usage"], "property_name": "usage"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Usage", "display_name": "usage", "import_name": "usage", "original": ["usage"], "property_name": "usage"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.usage.client import UsageClient
from xdk import Client


class TestUsageStructure:
    """Test the structure of UsageClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.usage_client = getattr(self.client, "usage")


    def test_get_exists(self):
        """Test that get method exists with correct signature."""
        # Check method exists
        method = getattr(UsageClient, "get", None)
        assert method is not None, f"Method get does not exist on UsageClient"
        # Check method is callable
        assert callable(method), f"get is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "days",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_return_annotation(self):
        """Test that get has proper return type annotation."""
        method = getattr(UsageClient, "get")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                UsageClient, expected_method
            ), f"Expected method '{expected_method}' not found on UsageClient"
            assert callable(
                getattr(UsageClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
