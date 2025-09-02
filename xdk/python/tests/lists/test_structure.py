"""
Auto-generated structural tests for {"class_name": "Lists", "display_name": "lists", "import_name": "lists", "original": ["lists"], "property_name": "lists"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Lists", "display_name": "lists", "import_name": "lists", "original": ["lists"], "property_name": "lists"} client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.lists.client import ListsClient
from xdk import Client


class TestListsStructure:
    """Test the structure of ListsClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.lists_client = getattr(self.client, "lists")


    def test_get_by_id_exists(self):
        """Test that get_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_by_id", None)
        assert method is not None, f"Method get_by_id does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_by_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_id_return_annotation(self):
        """Test that get_by_id has proper return type annotation."""
        method = getattr(ListsClient, "get_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_id should have return type annotation"


    def test_update_exists(self):
        """Test that update method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "update", None)
        assert method is not None, f"Method update does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"update is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"update should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from update"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_update_return_annotation(self):
        """Test that update has proper return type annotation."""
        method = getattr(ListsClient, "update")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method update should have return type annotation"


    def test_delete_exists(self):
        """Test that delete method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "delete", None)
        assert method is not None, f"Method delete does not exist on ListsClient"
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
            "id",
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
        method = getattr(ListsClient, "delete")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete should have return type annotation"


    def test_get_posts_exists(self):
        """Test that get_posts method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_posts", None)
        assert method is not None, f"Method get_posts does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts"
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


    def test_get_posts_return_annotation(self):
        """Test that get_posts has proper return type annotation."""
        method = getattr(ListsClient, "get_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts should have return type annotation"


    def test_get_posts_pagination_params(self):
        """Test that get_posts has pagination parameters."""
        method = getattr(ListsClient, "get_posts")
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
        ), f"Paginated method get_posts should have pagination parameters"


    def test_remove_member_by_user_id_exists(self):
        """Test that remove_member_by_user_id method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "remove_member_by_user_id", None)
        assert (
            method is not None
        ), f"Method remove_member_by_user_id does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"remove_member_by_user_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"remove_member_by_user_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
            "user_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from remove_member_by_user_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_remove_member_by_user_id_return_annotation(self):
        """Test that remove_member_by_user_id has proper return type annotation."""
        method = getattr(ListsClient, "remove_member_by_user_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method remove_member_by_user_id should have return type annotation"


    def test_create_exists(self):
        """Test that create method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "create", None)
        assert method is not None, f"Method create does not exist on ListsClient"
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
        method = getattr(ListsClient, "create")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create should have return type annotation"


    def test_get_followers_exists(self):
        """Test that get_followers method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_followers", None)
        assert method is not None, f"Method get_followers does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_followers is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_followers should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_followers"
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


    def test_get_followers_return_annotation(self):
        """Test that get_followers has proper return type annotation."""
        method = getattr(ListsClient, "get_followers")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_followers should have return type annotation"


    def test_get_followers_pagination_params(self):
        """Test that get_followers has pagination parameters."""
        method = getattr(ListsClient, "get_followers")
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
        ), f"Paginated method get_followers should have pagination parameters"


    def test_get_members_exists(self):
        """Test that get_members method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_members", None)
        assert method is not None, f"Method get_members does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_members is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_members should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_members"
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


    def test_get_members_return_annotation(self):
        """Test that get_members has proper return type annotation."""
        method = getattr(ListsClient, "get_members")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_members should have return type annotation"


    def test_get_members_pagination_params(self):
        """Test that get_members has pagination parameters."""
        method = getattr(ListsClient, "get_members")
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
        ), f"Paginated method get_members should have pagination parameters"


    def test_add_member_exists(self):
        """Test that add_member method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "add_member", None)
        assert method is not None, f"Method add_member does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"add_member is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"add_member should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from add_member"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_add_member_return_annotation(self):
        """Test that add_member has proper return type annotation."""
        method = getattr(ListsClient, "add_member")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method add_member should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_by_id",
            "update",
            "delete",
            "get_posts",
            "remove_member_by_user_id",
            "create",
            "get_followers",
            "get_members",
            "add_member",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                ListsClient, expected_method
            ), f"Expected method '{expected_method}' not found on ListsClient"
            assert callable(
                getattr(ListsClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
