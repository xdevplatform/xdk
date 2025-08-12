"""
Auto-generated structural tests for {"class_name": "Bookmarks", "display_name": "bookmarks", "import_name": "bookmarks", "original": ["bookmarks"], "property_name": "bookmarks"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Bookmarks", "display_name": "bookmarks", "import_name": "bookmarks", "original": ["bookmarks"], "property_name": "bookmarks"} client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.bookmarks.client import BookmarksClient
from xdk import Client


class TestBookmarksStructure:
    """Test the structure of BookmarksClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.bookmarks_client = getattr(self.client, "bookmarks")


    def test_delete_users_bookmark_exists(self):
        """Test that delete_users_bookmark method exists with correct signature."""
        # Check method exists
        method = getattr(BookmarksClient, "delete_users_bookmark", None)
        assert (
            method is not None
        ), f"Method delete_users_bookmark does not exist on BookmarksClient"
        # Check method is callable
        assert callable(method), f"delete_users_bookmark is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_users_bookmark should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
            "tweet_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_users_bookmark"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_users_bookmark_return_annotation(self):
        """Test that delete_users_bookmark has proper return type annotation."""
        method = getattr(BookmarksClient, "delete_users_bookmark")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_users_bookmark should have return type annotation"


    def test_create_users_bookmark_exists(self):
        """Test that create_users_bookmark method exists with correct signature."""
        # Check method exists
        method = getattr(BookmarksClient, "create_users_bookmark", None)
        assert (
            method is not None
        ), f"Method create_users_bookmark does not exist on BookmarksClient"
        # Check method is callable
        assert callable(method), f"create_users_bookmark is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_users_bookmark should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from create_users_bookmark"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_users_bookmark_return_annotation(self):
        """Test that create_users_bookmark has proper return type annotation."""
        method = getattr(BookmarksClient, "create_users_bookmark")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_users_bookmark should have return type annotation"


    def test_get_users_bookmark_folders_exists(self):
        """Test that get_users_bookmark_folders method exists with correct signature."""
        # Check method exists
        method = getattr(BookmarksClient, "get_users_bookmark_folders", None)
        assert (
            method is not None
        ), f"Method get_users_bookmark_folders does not exist on BookmarksClient"
        # Check method is callable
        assert callable(method), f"get_users_bookmark_folders is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_bookmark_folders should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_bookmark_folders"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "pagination_token",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_bookmark_folders_return_annotation(self):
        """Test that get_users_bookmark_folders has proper return type annotation."""
        method = getattr(BookmarksClient, "get_users_bookmark_folders")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_bookmark_folders should have return type annotation"


    def test_get_users_bookmark_folders_pagination_params(self):
        """Test that get_users_bookmark_folders has pagination parameters."""
        method = getattr(BookmarksClient, "get_users_bookmark_folders")
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have pagination-related parameters
        pagination_params = [
            "pagination_token",
            "max_results",
            "next_token",
            "cursor",
            "limit",
        ]
        has_pagination_param = any(param in params for param in pagination_params)
        assert (
            has_pagination_param
        ), f"Paginated method get_users_bookmark_folders should have pagination parameters"


    def test_get_users_by_folder_id_exists(self):
        """Test that get_users_by_folder_id method exists with correct signature."""
        # Check method exists
        method = getattr(BookmarksClient, "get_users_by_folder_id", None)
        assert (
            method is not None
        ), f"Method get_users_by_folder_id does not exist on BookmarksClient"
        # Check method is callable
        assert callable(method), f"get_users_by_folder_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_by_folder_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
            "folder_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_users_by_folder_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_by_folder_id_return_annotation(self):
        """Test that get_users_by_folder_id has proper return type annotation."""
        method = getattr(BookmarksClient, "get_users_by_folder_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_by_folder_id should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "delete_users_bookmark",
            "create_users_bookmark",
            "get_users_bookmark_folders",
            "get_users_by_folder_id",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                BookmarksClient, expected_method
            ), f"Expected method '{expected_method}' not found on BookmarksClient"
            assert callable(
                getattr(BookmarksClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
