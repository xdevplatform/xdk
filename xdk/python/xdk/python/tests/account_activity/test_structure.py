"""
Auto-generated structural tests for Account_Activity client.

This module contains tests that validate the structure and API surface
of the Account_Activity client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.account_activity.client import AccountActivityClient
from xdk import Client


class TestAccountActivityStructure:
    """Test the structure of AccountActivityClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.account_activity_client = getattr(self.client, "account_activity")


    def test_get_account_activity_subscription_count_exists(self):
        """Test that get_account_activity_subscription_count method exists with correct signature."""
        # Check method exists
        method = getattr(
            AccountActivityClient, "get_account_activity_subscription_count", None
        )
        assert (
            method is not None
        ), f"Method get_account_activity_subscription_count does not exist on AccountActivityClient"
        # Check method is callable
        assert callable(
            method
        ), f"get_account_activity_subscription_count is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_account_activity_subscription_count should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_account_activity_subscription_count"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_account_activity_subscription_count_return_annotation(self):
        """Test that get_account_activity_subscription_count has proper return type annotation."""
        method = getattr(
            AccountActivityClient, "get_account_activity_subscription_count"
        )
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_account_activity_subscription_count should have return type annotation"


    def test_validate_account_activity_subscription_exists(self):
        """Test that validate_account_activity_subscription method exists with correct signature."""
        # Check method exists
        method = getattr(
            AccountActivityClient, "validate_account_activity_subscription", None
        )
        assert (
            method is not None
        ), f"Method validate_account_activity_subscription does not exist on AccountActivityClient"
        # Check method is callable
        assert callable(
            method
        ), f"validate_account_activity_subscription is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"validate_account_activity_subscription should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from validate_account_activity_subscription"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_validate_account_activity_subscription_return_annotation(self):
        """Test that validate_account_activity_subscription has proper return type annotation."""
        method = getattr(
            AccountActivityClient, "validate_account_activity_subscription"
        )
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method validate_account_activity_subscription should have return type annotation"


    def test_get_account_activity_subscriptions_exists(self):
        """Test that get_account_activity_subscriptions method exists with correct signature."""
        # Check method exists
        method = getattr(
            AccountActivityClient, "get_account_activity_subscriptions", None
        )
        assert (
            method is not None
        ), f"Method get_account_activity_subscriptions does not exist on AccountActivityClient"
        # Check method is callable
        assert callable(method), f"get_account_activity_subscriptions is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_account_activity_subscriptions should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_account_activity_subscriptions"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_account_activity_subscriptions_return_annotation(self):
        """Test that get_account_activity_subscriptions has proper return type annotation."""
        method = getattr(AccountActivityClient, "get_account_activity_subscriptions")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_account_activity_subscriptions should have return type annotation"


    def test_delete_account_activity_subscription_exists(self):
        """Test that delete_account_activity_subscription method exists with correct signature."""
        # Check method exists
        method = getattr(
            AccountActivityClient, "delete_account_activity_subscription", None
        )
        assert (
            method is not None
        ), f"Method delete_account_activity_subscription does not exist on AccountActivityClient"
        # Check method is callable
        assert callable(method), f"delete_account_activity_subscription is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_account_activity_subscription should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "webhook_id",
            "user_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_account_activity_subscription"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_account_activity_subscription_return_annotation(self):
        """Test that delete_account_activity_subscription has proper return type annotation."""
        method = getattr(AccountActivityClient, "delete_account_activity_subscription")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_account_activity_subscription should have return type annotation"


    def test_create_account_activity_replay_job_exists(self):
        """Test that create_account_activity_replay_job method exists with correct signature."""
        # Check method exists
        method = getattr(
            AccountActivityClient, "create_account_activity_replay_job", None
        )
        assert (
            method is not None
        ), f"Method create_account_activity_replay_job does not exist on AccountActivityClient"
        # Check method is callable
        assert callable(method), f"create_account_activity_replay_job is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_account_activity_replay_job should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "webhook_id",
            "from_date",
            "to_date",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_account_activity_replay_job"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_account_activity_replay_job_return_annotation(self):
        """Test that create_account_activity_replay_job has proper return type annotation."""
        method = getattr(AccountActivityClient, "create_account_activity_replay_job")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_account_activity_replay_job should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_account_activity_subscription_count",
            "validate_account_activity_subscription",
            "get_account_activity_subscriptions",
            "delete_account_activity_subscription",
            "create_account_activity_replay_job",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                AccountActivityClient, expected_method
            ), f"Expected method '{expected_method}' not found on AccountActivityClient"
            assert callable(
                getattr(AccountActivityClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
