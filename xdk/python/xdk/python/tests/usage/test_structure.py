"""
Auto-generated structural tests for Usage client.

This module contains tests that validate the structure and API surface
of the Usage client. These tests ensure that all expected methods
exist and have the correct signatures.

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


    def test_get_usage_exists(self):
        """Test that get_usage method exists with correct signature."""
        # Check method exists
        method = getattr(UsageClient, "get_usage", None)
        assert method is not None, f"Method get_usage does not exist on UsageClient"
        # Check method is callable
        assert callable(method), f"get_usage is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_usage should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_usage"
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


    def test_get_usage_return_annotation(self):
        """Test that get_usage has proper return type annotation."""
        method = getattr(UsageClient, "get_usage")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_usage should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_usage",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                UsageClient, expected_method
            ), f"Expected method '{expected_method}' not found on UsageClient"
            assert callable(
                getattr(UsageClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
