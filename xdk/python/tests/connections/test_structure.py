"""
Auto-generated structural tests for {"class_name": "Connections", "display_name": "connections", "import_name": "connections", "original": ["connections"], "property_name": "connections"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Connections", "display_name": "connections", "import_name": "connections", "original": ["connections"], "property_name": "connections"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.connections.client import ConnectionsClient
from xdk import Client


class TestConnectionsStructure:
    """Test the structure of ConnectionsClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.connections_client = getattr(self.client, "connections")


    def test_delete_all_exists(self):
        """Test that delete_all method exists with correct signature."""
        # Check method exists
        method = getattr(ConnectionsClient, "delete_all", None)
        assert (
            method is not None
        ), f"Method delete_all does not exist on ConnectionsClient"
        # Check method is callable
        assert callable(method), f"delete_all is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete_all should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_all"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_all_return_annotation(self):
        """Test that delete_all has proper return type annotation."""
        method = getattr(ConnectionsClient, "delete_all")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_all should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "delete_all",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                ConnectionsClient, expected_method
            ), f"Expected method '{expected_method}' not found on ConnectionsClient"
            assert callable(
                getattr(ConnectionsClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
