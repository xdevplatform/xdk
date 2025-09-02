"""
Auto-generated structural tests for {"class_name": "Webhooks", "display_name": "webhooks", "import_name": "webhooks", "original": ["webhooks"], "property_name": "webhooks"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Webhooks", "display_name": "webhooks", "import_name": "webhooks", "original": ["webhooks"], "property_name": "webhooks"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.webhooks.client import WebhooksClient
from xdk import Client


class TestWebhooksStructure:
    """Test the structure of WebhooksClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.webhooks_client = getattr(self.client, "webhooks")


    def test_get_exists(self):
        """Test that get method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "get", None)
        assert method is not None, f"Method get does not exist on WebhooksClient"
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
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_return_annotation(self):
        """Test that get has proper return type annotation."""
        method = getattr(WebhooksClient, "get")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get should have return type annotation"


    def test_create_exists(self):
        """Test that create method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "create", None)
        assert method is not None, f"Method create does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"create is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_return_annotation(self):
        """Test that create has proper return type annotation."""
        method = getattr(WebhooksClient, "create")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create should have return type annotation"


    def test_validate_exists(self):
        """Test that validate method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "validate", None)
        assert method is not None, f"Method validate does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"validate is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"validate should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "webhook_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from validate"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_validate_return_annotation(self):
        """Test that validate has proper return type annotation."""
        method = getattr(WebhooksClient, "validate")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method validate should have return type annotation"


    def test_delete_exists(self):
        """Test that delete method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "delete", None)
        assert method is not None, f"Method delete does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"delete is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "webhook_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_return_annotation(self):
        """Test that delete has proper return type annotation."""
        method = getattr(WebhooksClient, "delete")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get",
            "create",
            "validate",
            "delete",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                WebhooksClient, expected_method
            ), f"Expected method '{expected_method}' not found on WebhooksClient"
            assert callable(
                getattr(WebhooksClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
