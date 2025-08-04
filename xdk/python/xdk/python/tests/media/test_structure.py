"""
Auto-generated structural tests for Media client.

This module contains tests that validate the structure and API surface
of the Media client. These tests ensure that all expected methods
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


    def test_create_media_subtitles_exists(self):
        """Test that create_media_subtitles method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "create_media_subtitles", None)
        assert (
            method is not None
        ), f"Method create_media_subtitles does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"create_media_subtitles is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_media_subtitles should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_media_subtitles"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_media_subtitles_return_annotation(self):
        """Test that create_media_subtitles has proper return type annotation."""
        method = getattr(MediaClient, "create_media_subtitles")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_media_subtitles should have return type annotation"


    def test_delete_media_subtitles_exists(self):
        """Test that delete_media_subtitles method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "delete_media_subtitles", None)
        assert (
            method is not None
        ), f"Method delete_media_subtitles does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"delete_media_subtitles is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_media_subtitles should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_media_subtitles"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_media_subtitles_return_annotation(self):
        """Test that delete_media_subtitles has proper return type annotation."""
        method = getattr(MediaClient, "delete_media_subtitles")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_media_subtitles should have return type annotation"


    def test_finalize_media_upload_exists(self):
        """Test that finalize_media_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "finalize_media_upload", None)
        assert (
            method is not None
        ), f"Method finalize_media_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"finalize_media_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"finalize_media_upload should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from finalize_media_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_finalize_media_upload_return_annotation(self):
        """Test that finalize_media_upload has proper return type annotation."""
        method = getattr(MediaClient, "finalize_media_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method finalize_media_upload should have return type annotation"


    def test_get_media_by_media_key_exists(self):
        """Test that get_media_by_media_key method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_media_by_media_key", None)
        assert (
            method is not None
        ), f"Method get_media_by_media_key does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_media_by_media_key is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_media_by_media_key should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_media_by_media_key"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_media_by_media_key_return_annotation(self):
        """Test that get_media_by_media_key has proper return type annotation."""
        method = getattr(MediaClient, "get_media_by_media_key")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_media_by_media_key should have return type annotation"


    def test_get_media_by_media_keys_exists(self):
        """Test that get_media_by_media_keys method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_media_by_media_keys", None)
        assert (
            method is not None
        ), f"Method get_media_by_media_keys does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_media_by_media_keys is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_media_by_media_keys should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_media_by_media_keys"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_media_by_media_keys_return_annotation(self):
        """Test that get_media_by_media_keys has proper return type annotation."""
        method = getattr(MediaClient, "get_media_by_media_keys")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_media_by_media_keys should have return type annotation"


    def test_initialize_media_upload_exists(self):
        """Test that initialize_media_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "initialize_media_upload", None)
        assert (
            method is not None
        ), f"Method initialize_media_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"initialize_media_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"initialize_media_upload should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from initialize_media_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_initialize_media_upload_return_annotation(self):
        """Test that initialize_media_upload has proper return type annotation."""
        method = getattr(MediaClient, "initialize_media_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method initialize_media_upload should have return type annotation"


    def test_get_media_upload_status_exists(self):
        """Test that get_media_upload_status method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_media_upload_status", None)
        assert (
            method is not None
        ), f"Method get_media_upload_status does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_media_upload_status is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_media_upload_status should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_media_upload_status"
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


    def test_get_media_upload_status_return_annotation(self):
        """Test that get_media_upload_status has proper return type annotation."""
        method = getattr(MediaClient, "get_media_upload_status")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_media_upload_status should have return type annotation"


    def test_media_upload_exists(self):
        """Test that media_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "media_upload", None)
        assert method is not None, f"Method media_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"media_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"media_upload should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from media_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_media_upload_return_annotation(self):
        """Test that media_upload has proper return type annotation."""
        method = getattr(MediaClient, "media_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method media_upload should have return type annotation"


    def test_get_media_analytics_exists(self):
        """Test that get_media_analytics method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "get_media_analytics", None)
        assert (
            method is not None
        ), f"Method get_media_analytics does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"get_media_analytics is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_media_analytics should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_media_analytics"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_media_analytics_return_annotation(self):
        """Test that get_media_analytics has proper return type annotation."""
        method = getattr(MediaClient, "get_media_analytics")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_media_analytics should have return type annotation"


    def test_create_media_metadata_exists(self):
        """Test that create_media_metadata method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "create_media_metadata", None)
        assert (
            method is not None
        ), f"Method create_media_metadata does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"create_media_metadata is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_media_metadata should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_media_metadata"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_media_metadata_return_annotation(self):
        """Test that create_media_metadata has proper return type annotation."""
        method = getattr(MediaClient, "create_media_metadata")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_media_metadata should have return type annotation"


    def test_append_media_upload_exists(self):
        """Test that append_media_upload method exists with correct signature."""
        # Check method exists
        method = getattr(MediaClient, "append_media_upload", None)
        assert (
            method is not None
        ), f"Method append_media_upload does not exist on MediaClient"
        # Check method is callable
        assert callable(method), f"append_media_upload is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"append_media_upload should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from append_media_upload"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_append_media_upload_return_annotation(self):
        """Test that append_media_upload has proper return type annotation."""
        method = getattr(MediaClient, "append_media_upload")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method append_media_upload should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "create_media_subtitles",
            "delete_media_subtitles",
            "finalize_media_upload",
            "get_media_by_media_key",
            "get_media_by_media_keys",
            "initialize_media_upload",
            "get_media_upload_status",
            "media_upload",
            "get_media_analytics",
            "create_media_metadata",
            "append_media_upload",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                MediaClient, expected_method
            ), f"Expected method '{expected_method}' not found on MediaClient"
            assert callable(
                getattr(MediaClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
