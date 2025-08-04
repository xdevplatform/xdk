"""
Auto-generated structural tests for General client.

This module contains tests that validate the structure and API surface
of the General client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.general.client import GeneralClient
from xdk import Client


class TestGeneralStructure:
    """Test the structure of GeneralClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.general_client = getattr(self.client, "general")

    def test_client_exists(self):
        """Test that GeneralClient class exists and is importable."""
        assert GeneralClient is not None
        assert hasattr(GeneralClient, "__name__")
        assert GeneralClient.__name__ == "GeneralClient"

    def test_client_initialization(self):
        """Test that GeneralClient can be initialized properly."""
        assert self.general_client is not None
        assert isinstance(self.general_client, GeneralClient)

    def test_get_open_api_spec_exists(self):
        """Test that get_open_api_spec method exists with correct signature."""
        # Check method exists
        method = getattr(GeneralClient, "get_open_api_spec", None)
        assert (
            method is not None
        ), f"Method get_open_api_spec does not exist on GeneralClient"

        # Check method is callable
        assert callable(method), f"get_open_api_spec is not callable"

        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())

        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_open_api_spec should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"

        # Check required parameters exist (excluding 'self')
        required_params = []

        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_open_api_spec"

        # Check optional parameters have defaults (excluding 'self')
        optional_params = []

        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_open_api_spec_return_annotation(self):
        """Test that get_open_api_spec has proper return type annotation."""
        method = getattr(GeneralClient, "get_open_api_spec")
        sig = inspect.signature(method)

        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_open_api_spec should have return type annotation"

    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_open_api_spec",
        ]

        client_methods = [
            name
            for name in dir(GeneralClient)
            if not name.startswith("_") and callable(getattr(GeneralClient, name))
        ]

        for expected_method in expected_methods:
            assert (
                expected_method in client_methods
            ), f"Expected method '{expected_method}' not found on GeneralClient"

    def test_no_unexpected_public_methods(self):
        """Test that no unexpected public methods exist (helps catch API drift)."""
        expected_methods = set(
            [
                "get_open_api_spec",
            ]
        )

        actual_methods = set(
            [
                name
                for name in dir(GeneralClient)
                if not name.startswith("_") and callable(getattr(GeneralClient, name))
            ]
        )

        # Remove standard methods that might be inherited
        standard_methods = {"__init__"}
        actual_methods = actual_methods - standard_methods

        unexpected_methods = actual_methods - expected_methods

        # This is a warning, not a failure, since new methods might be added
        if unexpected_methods:
            print(
                f"Warning: Unexpected methods found on GeneralClient: {unexpected_methods}"
            )

    def test_imports_work(self):
        """Test that all expected imports work correctly."""
        expected_imports = [
            "typing",
            "requests",
            "pydantic",
        ]

        for import_name in expected_imports:
            try:
                __import__(import_name)
            except ImportError as e:
                pytest.fail(f"Expected import '{import_name}' failed: {e}")
