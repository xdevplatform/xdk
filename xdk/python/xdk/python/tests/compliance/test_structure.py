"""
Auto-generated structural tests for Compliance client.

This module contains tests that validate the structure and API surface
of the Compliance client. These tests ensure that all expected methods
exist and have the correct signatures.

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


    def test_get_compliance_jobs_exists(self):
        """Test that get_compliance_jobs method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "get_compliance_jobs", None)
        assert (
            method is not None
        ), f"Method get_compliance_jobs does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"get_compliance_jobs is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_compliance_jobs should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_compliance_jobs"
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


    def test_get_compliance_jobs_return_annotation(self):
        """Test that get_compliance_jobs has proper return type annotation."""
        method = getattr(ComplianceClient, "get_compliance_jobs")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_compliance_jobs should have return type annotation"


    def test_create_compliance_jobs_exists(self):
        """Test that create_compliance_jobs method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "create_compliance_jobs", None)
        assert (
            method is not None
        ), f"Method create_compliance_jobs does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"create_compliance_jobs is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_compliance_jobs should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_compliance_jobs"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_compliance_jobs_return_annotation(self):
        """Test that create_compliance_jobs has proper return type annotation."""
        method = getattr(ComplianceClient, "create_compliance_jobs")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_compliance_jobs should have return type annotation"


    def test_get_compliance_jobs_by_id_exists(self):
        """Test that get_compliance_jobs_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "get_compliance_jobs_by_id", None)
        assert (
            method is not None
        ), f"Method get_compliance_jobs_by_id does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"get_compliance_jobs_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_compliance_jobs_by_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_compliance_jobs_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_compliance_jobs_by_id_return_annotation(self):
        """Test that get_compliance_jobs_by_id has proper return type annotation."""
        method = getattr(ComplianceClient, "get_compliance_jobs_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_compliance_jobs_by_id should have return type annotation"


    def test_stream_likes_compliance_exists(self):
        """Test that stream_likes_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "stream_likes_compliance", None)
        assert (
            method is not None
        ), f"Method stream_likes_compliance does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"stream_likes_compliance is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_likes_compliance should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from stream_likes_compliance"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "backfill_minutes",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_stream_likes_compliance_return_annotation(self):
        """Test that stream_likes_compliance has proper return type annotation."""
        method = getattr(ComplianceClient, "stream_likes_compliance")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_likes_compliance should have return type annotation"


    def test_stream_users_compliance_exists(self):
        """Test that stream_users_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "stream_users_compliance", None)
        assert (
            method is not None
        ), f"Method stream_users_compliance does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"stream_users_compliance is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_users_compliance should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "partition",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from stream_users_compliance"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "backfill_minutes",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_stream_users_compliance_return_annotation(self):
        """Test that stream_users_compliance has proper return type annotation."""
        method = getattr(ComplianceClient, "stream_users_compliance")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_users_compliance should have return type annotation"


    def test_stream_labels_compliance_exists(self):
        """Test that stream_labels_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "stream_labels_compliance", None)
        assert (
            method is not None
        ), f"Method stream_labels_compliance does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"stream_labels_compliance is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_labels_compliance should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from stream_labels_compliance"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "backfill_minutes",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_stream_labels_compliance_return_annotation(self):
        """Test that stream_labels_compliance has proper return type annotation."""
        method = getattr(ComplianceClient, "stream_labels_compliance")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_labels_compliance should have return type annotation"


    def test_stream_posts_compliance_exists(self):
        """Test that stream_posts_compliance method exists with correct signature."""
        # Check method exists
        method = getattr(ComplianceClient, "stream_posts_compliance", None)
        assert (
            method is not None
        ), f"Method stream_posts_compliance does not exist on ComplianceClient"
        # Check method is callable
        assert callable(method), f"stream_posts_compliance is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_compliance should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "partition",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from stream_posts_compliance"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "backfill_minutes",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_stream_posts_compliance_return_annotation(self):
        """Test that stream_posts_compliance has proper return type annotation."""
        method = getattr(ComplianceClient, "stream_posts_compliance")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_compliance should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_compliance_jobs",
            "create_compliance_jobs",
            "get_compliance_jobs_by_id",
            "stream_likes_compliance",
            "stream_users_compliance",
            "stream_labels_compliance",
            "stream_posts_compliance",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                ComplianceClient, expected_method
            ), f"Expected method '{expected_method}' not found on ComplianceClient"
            assert callable(
                getattr(ComplianceClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
