"""
Auto-generated structural tests for Lists client.

This module contains tests that validate the structure and API surface
of the Lists client. These tests ensure that all expected methods
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


    def test_unfollow_list_exists(self):
        """Test that unfollow_list method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "unfollow_list", None)
        assert method is not None, f"Method unfollow_list does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"unfollow_list is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unfollow_list should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
            "list_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from unfollow_list"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unfollow_list_return_annotation(self):
        """Test that unfollow_list has proper return type annotation."""
        method = getattr(ListsClient, "unfollow_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unfollow_list should have return type annotation"


    def test_unpin_list_exists(self):
        """Test that unpin_list method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "unpin_list", None)
        assert method is not None, f"Method unpin_list does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"unpin_list is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unpin_list should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
            "list_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from unpin_list"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unpin_list_return_annotation(self):
        """Test that unpin_list has proper return type annotation."""
        method = getattr(ListsClient, "unpin_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unpin_list should have return type annotation"


    def test_add_lists_member_exists(self):
        """Test that add_lists_member method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "add_lists_member", None)
        assert (
            method is not None
        ), f"Method add_lists_member does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"add_lists_member is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"add_lists_member should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from add_lists_member"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_add_lists_member_return_annotation(self):
        """Test that add_lists_member has proper return type annotation."""
        method = getattr(ListsClient, "add_lists_member")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method add_lists_member should have return type annotation"


    def test_remove_lists_member_by_user_id_exists(self):
        """Test that remove_lists_member_by_user_id method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "remove_lists_member_by_user_id", None)
        assert (
            method is not None
        ), f"Method remove_lists_member_by_user_id does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"remove_lists_member_by_user_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"remove_lists_member_by_user_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from remove_lists_member_by_user_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_remove_lists_member_by_user_id_return_annotation(self):
        """Test that remove_lists_member_by_user_id has proper return type annotation."""
        method = getattr(ListsClient, "remove_lists_member_by_user_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method remove_lists_member_by_user_id should have return type annotation"


    def test_get_users_followed_lists_exists(self):
        """Test that get_users_followed_lists method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_users_followed_lists", None)
        assert (
            method is not None
        ), f"Method get_users_followed_lists does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_users_followed_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_followed_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_followed_lists"
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


    def test_get_users_followed_lists_return_annotation(self):
        """Test that get_users_followed_lists has proper return type annotation."""
        method = getattr(ListsClient, "get_users_followed_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_followed_lists should have return type annotation"


    def test_get_users_followed_lists_pagination_params(self):
        """Test that get_users_followed_lists has pagination parameters."""
        method = getattr(ListsClient, "get_users_followed_lists")
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
        ), f"Paginated method get_users_followed_lists should have pagination parameters"


    def test_follow_list_exists(self):
        """Test that follow_list method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "follow_list", None)
        assert method is not None, f"Method follow_list does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"follow_list is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"follow_list should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from follow_list"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_follow_list_return_annotation(self):
        """Test that follow_list has proper return type annotation."""
        method = getattr(ListsClient, "follow_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method follow_list should have return type annotation"


    def test_create_lists_exists(self):
        """Test that create_lists method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "create_lists", None)
        assert method is not None, f"Method create_lists does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"create_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_lists should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_lists"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_lists_return_annotation(self):
        """Test that create_lists has proper return type annotation."""
        method = getattr(ListsClient, "create_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_lists should have return type annotation"


    def test_get_lists_by_id_exists(self):
        """Test that get_lists_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_lists_by_id", None)
        assert (
            method is not None
        ), f"Method get_lists_by_id does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_lists_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_lists_by_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_lists_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_lists_by_id_return_annotation(self):
        """Test that get_lists_by_id has proper return type annotation."""
        method = getattr(ListsClient, "get_lists_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_lists_by_id should have return type annotation"


    def test_update_lists_exists(self):
        """Test that update_lists method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "update_lists", None)
        assert method is not None, f"Method update_lists does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"update_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"update_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from update_lists"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_update_lists_return_annotation(self):
        """Test that update_lists has proper return type annotation."""
        method = getattr(ListsClient, "update_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method update_lists should have return type annotation"


    def test_delete_lists_exists(self):
        """Test that delete_lists method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "delete_lists", None)
        assert method is not None, f"Method delete_lists does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"delete_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from delete_lists"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_lists_return_annotation(self):
        """Test that delete_lists has proper return type annotation."""
        method = getattr(ListsClient, "delete_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_lists should have return type annotation"


    def test_get_users_pinned_lists_exists(self):
        """Test that get_users_pinned_lists method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_users_pinned_lists", None)
        assert (
            method is not None
        ), f"Method get_users_pinned_lists does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_users_pinned_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_pinned_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_pinned_lists"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_pinned_lists_return_annotation(self):
        """Test that get_users_pinned_lists has proper return type annotation."""
        method = getattr(ListsClient, "get_users_pinned_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_pinned_lists should have return type annotation"


    def test_pin_list_exists(self):
        """Test that pin_list method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "pin_list", None)
        assert method is not None, f"Method pin_list does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"pin_list is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"pin_list should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from pin_list"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_pin_list_return_annotation(self):
        """Test that pin_list has proper return type annotation."""
        method = getattr(ListsClient, "pin_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method pin_list should have return type annotation"


    def test_get_users_list_memberships_exists(self):
        """Test that get_users_list_memberships method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_users_list_memberships", None)
        assert (
            method is not None
        ), f"Method get_users_list_memberships does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_users_list_memberships is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_list_memberships should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_list_memberships"
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


    def test_get_users_list_memberships_return_annotation(self):
        """Test that get_users_list_memberships has proper return type annotation."""
        method = getattr(ListsClient, "get_users_list_memberships")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_list_memberships should have return type annotation"


    def test_get_users_list_memberships_pagination_params(self):
        """Test that get_users_list_memberships has pagination parameters."""
        method = getattr(ListsClient, "get_users_list_memberships")
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
        ), f"Paginated method get_users_list_memberships should have pagination parameters"


    def test_get_users_owned_lists_exists(self):
        """Test that get_users_owned_lists method exists with correct signature."""
        # Check method exists
        method = getattr(ListsClient, "get_users_owned_lists", None)
        assert (
            method is not None
        ), f"Method get_users_owned_lists does not exist on ListsClient"
        # Check method is callable
        assert callable(method), f"get_users_owned_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_owned_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_owned_lists"
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


    def test_get_users_owned_lists_return_annotation(self):
        """Test that get_users_owned_lists has proper return type annotation."""
        method = getattr(ListsClient, "get_users_owned_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_owned_lists should have return type annotation"


    def test_get_users_owned_lists_pagination_params(self):
        """Test that get_users_owned_lists has pagination parameters."""
        method = getattr(ListsClient, "get_users_owned_lists")
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
        ), f"Paginated method get_users_owned_lists should have pagination parameters"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "unfollow_list",
            "unpin_list",
            "add_lists_member",
            "remove_lists_member_by_user_id",
            "get_users_followed_lists",
            "follow_list",
            "create_lists",
            "get_lists_by_id",
            "update_lists",
            "delete_lists",
            "get_users_pinned_lists",
            "pin_list",
            "get_users_list_memberships",
            "get_users_owned_lists",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                ListsClient, expected_method
            ), f"Expected method '{expected_method}' not found on ListsClient"
            assert callable(
                getattr(ListsClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
