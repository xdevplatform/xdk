"""
Auto-generated structural tests for {"class_name": "Compliance", "display_name": "compliance", "import_name": "compliance", "original": ["compliance"], "property_name": "compliance"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Compliance", "display_name": "compliance", "import_name": "compliance", "original": ["compliance"], "property_name": "compliance"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.compliance.client import ComplianceClient
from xdk import Client


class TestComplianceStructure:
    """Test the structure of ComplianceClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.compliance_client = getattr(self.client, "compliance")


    def test_get_jobs_by_id_exists(self):
        """Test that get_jobs_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "get_jobs_by_id", None)
        assert (
            method is not None
        ), f"Method get_jobs_by_id does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"get_jobs_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_jobs_by_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_jobs_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_jobs_by_id_return_annotation(self):
        """Test that get_jobs_by_id has proper return type annotation."""
        method = getattr(ComplianceClient, "get_jobs_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_jobs_by_id should have return type annotation"


    def test_get_jobs_exists(self):
        """Test that get_jobs method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "get_jobs", None)
        assert method is not None, f"Method get_jobs does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"get_jobs is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_jobs should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "type",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_jobs"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "status",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_jobs_return_annotation(self):
        """Test that get_jobs has proper return type annotation."""
        method = getattr(ComplianceClient, "get_jobs")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_jobs should have return type annotation"


    def test_create_jobs_exists(self):
        """Test that create_jobs method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "create_jobs", None)
        assert (
            method is not None
        ), f"Method create_jobs does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"create_jobs is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_jobs should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_jobs"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_jobs_return_annotation(self):
        """Test that create_jobs has proper return type annotation."""
        method = getattr(ComplianceClient, "create_jobs")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_jobs should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_jobs_by_id",
            "get_jobs",
            "create_jobs",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                ComplianceClient, expected_method
            ), f"Expected method '{expected_method}' not found on ComplianceClient"
            assert callable(
                getattr(ComplianceClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
