"""
Auto-generated structural tests for Connection client.

This module contains tests that validate the structure and API surface
of the Connection client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.connection.client import ConnectionClient
from xdk import Client


class TestConnectionStructure:
    """Test the structure of ConnectionClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.connection_client = getattr(self.client, "connection")


    def test_delete_all_connections_exists(self):
        """Test that delete_all_connections method exists with correct signature."""
        # Check method exists
        method = getattr(ConnectionClient, "delete_all_connections", None)
        assert (
            method is not None
        ), f"Method delete_all_connections does not exist on ConnectionClient"
        # Check method is callable
        assert callable(method), f"delete_all_connections is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_all_connections should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_all_connections"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_all_connections_return_annotation(self):
        """Test that delete_all_connections has proper return type annotation."""
        method = getattr(ConnectionClient, "delete_all_connections")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_all_connections should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "delete_all_connections",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                ConnectionClient, expected_method
            ), f"Expected method '{expected_method}' not found on ConnectionClient"
            assert callable(
                getattr(ConnectionClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
