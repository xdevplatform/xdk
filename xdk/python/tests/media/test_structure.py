"""
Auto-generated structural tests for {"class_name": "Media", "display_name": "media", "import_name": "media", "original": ["media"], "property_name": "media"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Media", "display_name": "media", "import_name": "media", "original": ["media"], "property_name": "media"} client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.media.client import MediaClient
from xdk import Client


class TestMediaStructure:
    """Test the structure of MediaClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.media_client = getattr(self.client, "media")


    def test_create_metadata_exists(self):
        """Test that create_metadata method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "create_metadata", None)
        assert (
            method is not None
        ), f"Method create_metadata does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"create_metadata is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_metadata should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_metadata"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_metadata_return_annotation(self):
        """Test that create_metadata has proper return type annotation."""
        method = getattr(MediaClient, "create_metadata")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_metadata should have return type annotation"


    def test_get_analytics_exists(self):
        """Test that get_analytics method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_analytics", None)
        assert method is not None, f"Method get_analytics does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_analytics is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_analytics should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "media_keys",
            "end_time",
            "start_time",
            "granularity",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_analytics"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_analytics_return_annotation(self):
        """Test that get_analytics has proper return type annotation."""
        method = getattr(MediaClient, "get_analytics")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_analytics should have return type annotation"


    def test_get_by_keys_exists(self):
        """Test that get_by_keys method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_by_keys", None)
        assert method is not None, f"Method get_by_keys does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_by_keys is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_by_keys should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "media_keys",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_by_keys"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_keys_return_annotation(self):
        """Test that get_by_keys has proper return type annotation."""
        method = getattr(MediaClient, "get_by_keys")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_keys should have return type annotation"


    def test_finalize_upload_exists(self):
        """Test that finalize_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "finalize_upload", None)
        assert (
            method is not None
        ), f"Method finalize_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"finalize_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"finalize_upload should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from finalize_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_finalize_upload_return_annotation(self):
        """Test that finalize_upload has proper return type annotation."""
        method = getattr(MediaClient, "finalize_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method finalize_upload should have return type annotation"


    def test_append_upload_exists(self):
        """Test that append_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "append_upload", None)
        assert method is not None, f"Method append_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"append_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"append_upload should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from append_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_append_upload_return_annotation(self):
        """Test that append_upload has proper return type annotation."""
        method = getattr(MediaClient, "append_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method append_upload should have return type annotation"


    def test_get_upload_status_exists(self):
        """Test that get_upload_status method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_upload_status", None)
        assert (
            method is not None
        ), f"Method get_upload_status does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_upload_status is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_upload_status should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "media_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_upload_status"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "command",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_upload_status_return_annotation(self):
        """Test that get_upload_status has proper return type annotation."""
        method = getattr(MediaClient, "get_upload_status")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_upload_status should have return type annotation"


    def test_upload_exists(self):
        """Test that upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "upload", None)
        assert method is not None, f"Method upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"upload should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_upload_return_annotation(self):
        """Test that upload has proper return type annotation."""
        method = getattr(MediaClient, "upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method upload should have return type annotation"


    def test_create_subtitles_exists(self):
        """Test that create_subtitles method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "create_subtitles", None)
        assert (
            method is not None
        ), f"Method create_subtitles does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"create_subtitles is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_subtitles should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_subtitles"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_subtitles_return_annotation(self):
        """Test that create_subtitles has proper return type annotation."""
        method = getattr(MediaClient, "create_subtitles")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_subtitles should have return type annotation"


    def test_delete_subtitles_exists(self):
        """Test that delete_subtitles method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "delete_subtitles", None)
        assert (
            method is not None
        ), f"Method delete_subtitles does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"delete_subtitles is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_subtitles should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_subtitles"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_subtitles_return_annotation(self):
        """Test that delete_subtitles has proper return type annotation."""
        method = getattr(MediaClient, "delete_subtitles")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_subtitles should have return type annotation"


    def test_initialize_upload_exists(self):
        """Test that initialize_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "initialize_upload", None)
        assert (
            method is not None
        ), f"Method initialize_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"initialize_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"initialize_upload should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from initialize_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_initialize_upload_return_annotation(self):
        """Test that initialize_upload has proper return type annotation."""
        method = getattr(MediaClient, "initialize_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method initialize_upload should have return type annotation"


    def test_get_by_key_exists(self):
        """Test that get_by_key method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_by_key", None)
        assert method is not None, f"Method get_by_key does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_by_key is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_by_key should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "media_key",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_by_key"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_key_return_annotation(self):
        """Test that get_by_key has proper return type annotation."""
        method = getattr(MediaClient, "get_by_key")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_key should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "create_metadata",
            "get_analytics",
            "get_by_keys",
            "finalize_upload",
            "append_upload",
            "get_upload_status",
            "upload",
            "create_subtitles",
            "delete_subtitles",
            "initialize_upload",
            "get_by_key",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                MediaClient, expected_method
            ), f"Expected method '{expected_method}' not found on MediaClient"
            assert callable(
                getattr(MediaClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
