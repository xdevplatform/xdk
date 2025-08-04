"""
Auto-generated structural tests for Webhooks client.

This module contains tests that validate the structure and API surface
of the Webhooks client. These tests ensure that all expected methods
exist and have the correct signatures.

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


    def test_validate_webhooks_exists(self):
        """Test that validate_webhooks method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "validate_webhooks", None)
        assert (
            method is not None
        ), f"Method validate_webhooks does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"validate_webhooks is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"validate_webhooks should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from validate_webhooks"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_validate_webhooks_return_annotation(self):
        """Test that validate_webhooks has proper return type annotation."""
        method = getattr(WebhooksClient, "validate_webhooks")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method validate_webhooks should have return type annotation"


    def test_delete_webhooks_exists(self):
        """Test that delete_webhooks method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "delete_webhooks", None)
        assert (
            method is not None
        ), f"Method delete_webhooks does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"delete_webhooks is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_webhooks should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from delete_webhooks"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_webhooks_return_annotation(self):
        """Test that delete_webhooks has proper return type annotation."""
        method = getattr(WebhooksClient, "delete_webhooks")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_webhooks should have return type annotation"


    def test_get_webhooks_exists(self):
        """Test that get_webhooks method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "get_webhooks", None)
        assert (
            method is not None
        ), f"Method get_webhooks does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"get_webhooks is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_webhooks should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_webhooks"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_webhooks_return_annotation(self):
        """Test that get_webhooks has proper return type annotation."""
        method = getattr(WebhooksClient, "get_webhooks")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_webhooks should have return type annotation"


    def test_create_webhooks_exists(self):
        """Test that create_webhooks method exists with correct signature."""
        # Check method exists
        method = getattr(WebhooksClient, "create_webhooks", None)
        assert (
            method is not None
        ), f"Method create_webhooks does not exist on WebhooksClient"
        # Check method is callable
        assert callable(method), f"create_webhooks is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_webhooks should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_webhooks"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_webhooks_return_annotation(self):
        """Test that create_webhooks has proper return type annotation."""
        method = getattr(WebhooksClient, "create_webhooks")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_webhooks should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "validate_webhooks",
            "delete_webhooks",
            "get_webhooks",
            "create_webhooks",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                WebhooksClient, expected_method
            ), f"Expected method '{expected_method}' not found on WebhooksClient"
            assert callable(
                getattr(WebhooksClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
