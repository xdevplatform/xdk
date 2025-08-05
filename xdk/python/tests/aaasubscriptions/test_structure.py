"""
Auto-generated structural tests for AAASubscriptions client.

This module contains tests that validate the structure and API surface
of the AAASubscriptions client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.aaasubscriptions.client import AAASubscriptionsClient
from xdk import Client


class TestAAASubscriptionsStructure:
    """Test the structure of AAASubscriptionsClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.aaasubscriptions_client = getattr(self.client, "aaasubscriptions")


    def test_create_account_activity_subscription_exists(self):
        """Test that create_account_activity_subscription method exists with correct signature."""
        # Check method exists
        method = getattr(
            AAASubscriptionsClient, "create_account_activity_subscription", None
        )
        assert (
            method is not None
        ), f"Method create_account_activity_subscription does not exist on AAASubscriptionsClient"
        # Check method is callable
        assert callable(method), f"create_account_activity_subscription is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_account_activity_subscription should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from create_account_activity_subscription"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_account_activity_subscription_return_annotation(self):
        """Test that create_account_activity_subscription has proper return type annotation."""
        method = getattr(AAASubscriptionsClient, "create_account_activity_subscription")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_account_activity_subscription should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "create_account_activity_subscription",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                AAASubscriptionsClient, expected_method
            ), f"Expected method '{expected_method}' not found on AAASubscriptionsClient"
            assert callable(
                getattr(AAASubscriptionsClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
