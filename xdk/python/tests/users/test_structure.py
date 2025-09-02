"""
Auto-generated structural tests for {"class_name": "Users", "display_name": "users", "import_name": "users", "original": ["users"], "property_name": "users"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Users", "display_name": "users", "import_name": "users", "original": ["users"], "property_name": "users"} client. These tests ensure that all expected methods
exist, have correct signatures, and proper type annotations for robust API contracts.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.users.client import UsersClient
from xdk import Client


class TestUsersStructure:
    """Test the structure of UsersClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.users_client = getattr(self.client, "users")


    def test_get_list_memberships_exists(self):
        """Test that get_list_memberships method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_list_memberships", None)
        assert (
            method is not None
        ), f"Method get_list_memberships does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_list_memberships is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_list_memberships should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_list_memberships"
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


    def test_get_list_memberships_return_annotation(self):
        """Test that get_list_memberships has proper return type annotation."""
        method = getattr(UsersClient, "get_list_memberships")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_list_memberships should have return type annotation"


    def test_get_list_memberships_pagination_params(self):
        """Test that get_list_memberships has pagination parameters."""
        method = getattr(UsersClient, "get_list_memberships")
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
        ), f"Paginated method get_list_memberships should have pagination parameters"


    def test_search_exists(self):
        """Test that search method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "search", None)
        assert method is not None, f"Method search does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"search is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "query",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from search"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "next_token",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_search_return_annotation(self):
        """Test that search has proper return type annotation."""
        method = getattr(UsersClient, "search")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search should have return type annotation"


    def test_search_pagination_params(self):
        """Test that search has pagination parameters."""
        method = getattr(UsersClient, "search")
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
        ), f"Paginated method search should have pagination parameters"


    def test_like_post_exists(self):
        """Test that like_post method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "like_post", None)
        assert method is not None, f"Method like_post does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"like_post is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"like_post should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from like_post"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_like_post_return_annotation(self):
        """Test that like_post has proper return type annotation."""
        method = getattr(UsersClient, "like_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method like_post should have return type annotation"


    def test_get_blocking_exists(self):
        """Test that get_blocking method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_blocking", None)
        assert method is not None, f"Method get_blocking does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_blocking is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_blocking should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_blocking"
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


    def test_get_blocking_return_annotation(self):
        """Test that get_blocking has proper return type annotation."""
        method = getattr(UsersClient, "get_blocking")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_blocking should have return type annotation"


    def test_get_blocking_pagination_params(self):
        """Test that get_blocking has pagination parameters."""
        method = getattr(UsersClient, "get_blocking")
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
        ), f"Paginated method get_blocking should have pagination parameters"


    def test_unrepost_post_exists(self):
        """Test that unrepost_post method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unrepost_post", None)
        assert method is not None, f"Method unrepost_post does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"unrepost_post is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unrepost_post should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "id",
            "source_tweet_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from unrepost_post"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unrepost_post_return_annotation(self):
        """Test that unrepost_post has proper return type annotation."""
        method = getattr(UsersClient, "unrepost_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unrepost_post should have return type annotation"


    def test_get_liked_posts_exists(self):
        """Test that get_liked_posts method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_liked_posts", None)
        assert (
            method is not None
        ), f"Method get_liked_posts does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_liked_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_liked_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_liked_posts"
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


    def test_get_liked_posts_return_annotation(self):
        """Test that get_liked_posts has proper return type annotation."""
        method = getattr(UsersClient, "get_liked_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_liked_posts should have return type annotation"


    def test_get_liked_posts_pagination_params(self):
        """Test that get_liked_posts has pagination parameters."""
        method = getattr(UsersClient, "get_liked_posts")
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
        ), f"Paginated method get_liked_posts should have pagination parameters"


    def test_get_by_ids_exists(self):
        """Test that get_by_ids method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_by_ids", None)
        assert method is not None, f"Method get_by_ids does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_by_ids is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_by_ids should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "ids",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_by_ids"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_ids_return_annotation(self):
        """Test that get_by_ids has proper return type annotation."""
        method = getattr(UsersClient, "get_by_ids")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_ids should have return type annotation"


    def test_get_by_id_exists(self):
        """Test that get_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_by_id", None)
        assert method is not None, f"Method get_by_id does not exist on UsersClient"
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
        method = getattr(UsersClient, "get_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_id should have return type annotation"


    def test_get_by_username_exists(self):
        """Test that get_by_username method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_by_username", None)
        assert (
            method is not None
        ), f"Method get_by_username does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_by_username is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_by_username should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "username",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_by_username"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_username_return_annotation(self):
        """Test that get_by_username has proper return type annotation."""
        method = getattr(UsersClient, "get_by_username")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_username should have return type annotation"


    def test_get_bookmarks_exists(self):
        """Test that get_bookmarks method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_bookmarks", None)
        assert method is not None, f"Method get_bookmarks does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_bookmarks is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_bookmarks should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_bookmarks"
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


    def test_get_bookmarks_return_annotation(self):
        """Test that get_bookmarks has proper return type annotation."""
        method = getattr(UsersClient, "get_bookmarks")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_bookmarks should have return type annotation"


    def test_get_bookmarks_pagination_params(self):
        """Test that get_bookmarks has pagination parameters."""
        method = getattr(UsersClient, "get_bookmarks")
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
        ), f"Paginated method get_bookmarks should have pagination parameters"


    def test_create_bookmark_exists(self):
        """Test that create_bookmark method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "create_bookmark", None)
        assert (
            method is not None
        ), f"Method create_bookmark does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"create_bookmark is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_bookmark should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from create_bookmark"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_bookmark_return_annotation(self):
        """Test that create_bookmark has proper return type annotation."""
        method = getattr(UsersClient, "create_bookmark")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_bookmark should have return type annotation"


    def test_get_muting_exists(self):
        """Test that get_muting method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_muting", None)
        assert method is not None, f"Method get_muting does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_muting is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_muting should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_muting"
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


    def test_get_muting_return_annotation(self):
        """Test that get_muting has proper return type annotation."""
        method = getattr(UsersClient, "get_muting")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_muting should have return type annotation"


    def test_get_muting_pagination_params(self):
        """Test that get_muting has pagination parameters."""
        method = getattr(UsersClient, "get_muting")
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
        ), f"Paginated method get_muting should have pagination parameters"


    def test_mute_user_exists(self):
        """Test that mute_user method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "mute_user", None)
        assert method is not None, f"Method mute_user does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"mute_user is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"mute_user should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from mute_user"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_mute_user_return_annotation(self):
        """Test that mute_user has proper return type annotation."""
        method = getattr(UsersClient, "mute_user")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method mute_user should have return type annotation"


    def test_get_bookmark_folders_exists(self):
        """Test that get_bookmark_folders method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_bookmark_folders", None)
        assert (
            method is not None
        ), f"Method get_bookmark_folders does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_bookmark_folders is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_bookmark_folders should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_bookmark_folders"
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


    def test_get_bookmark_folders_return_annotation(self):
        """Test that get_bookmark_folders has proper return type annotation."""
        method = getattr(UsersClient, "get_bookmark_folders")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_bookmark_folders should have return type annotation"


    def test_get_bookmark_folders_pagination_params(self):
        """Test that get_bookmark_folders has pagination parameters."""
        method = getattr(UsersClient, "get_bookmark_folders")
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
        ), f"Paginated method get_bookmark_folders should have pagination parameters"


    def test_unfollow_list_exists(self):
        """Test that unfollow_list method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unfollow_list", None)
        assert method is not None, f"Method unfollow_list does not exist on UsersClient"
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
        method = getattr(UsersClient, "unfollow_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unfollow_list should have return type annotation"


    def test_unfollow_user_exists(self):
        """Test that unfollow_user method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unfollow_user", None)
        assert method is not None, f"Method unfollow_user does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"unfollow_user is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unfollow_user should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "source_user_id",
            "target_user_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from unfollow_user"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unfollow_user_return_annotation(self):
        """Test that unfollow_user has proper return type annotation."""
        method = getattr(UsersClient, "unfollow_user")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unfollow_user should have return type annotation"


    def test_unlike_post_exists(self):
        """Test that unlike_post method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unlike_post", None)
        assert method is not None, f"Method unlike_post does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"unlike_post is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unlike_post should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from unlike_post"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unlike_post_return_annotation(self):
        """Test that unlike_post has proper return type annotation."""
        method = getattr(UsersClient, "unlike_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unlike_post should have return type annotation"


    def test_get_following_exists(self):
        """Test that get_following method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_following", None)
        assert method is not None, f"Method get_following does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_following is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_following should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_following"
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


    def test_get_following_return_annotation(self):
        """Test that get_following has proper return type annotation."""
        method = getattr(UsersClient, "get_following")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_following should have return type annotation"


    def test_get_following_pagination_params(self):
        """Test that get_following has pagination parameters."""
        method = getattr(UsersClient, "get_following")
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
        ), f"Paginated method get_following should have pagination parameters"


    def test_follow_user_exists(self):
        """Test that follow_user method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "follow_user", None)
        assert method is not None, f"Method follow_user does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"follow_user is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"follow_user should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from follow_user"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_follow_user_return_annotation(self):
        """Test that follow_user has proper return type annotation."""
        method = getattr(UsersClient, "follow_user")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method follow_user should have return type annotation"


    def test_repost_post_exists(self):
        """Test that repost_post method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "repost_post", None)
        assert method is not None, f"Method repost_post does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"repost_post is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"repost_post should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from repost_post"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_repost_post_return_annotation(self):
        """Test that repost_post has proper return type annotation."""
        method = getattr(UsersClient, "repost_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method repost_post should have return type annotation"


    def test_get_timeline_exists(self):
        """Test that get_timeline method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_timeline", None)
        assert method is not None, f"Method get_timeline does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_timeline is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_timeline should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_timeline"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "since_id",
            "until_id",
            "max_results",
            "pagination_token",
            "exclude",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_timeline_return_annotation(self):
        """Test that get_timeline has proper return type annotation."""
        method = getattr(UsersClient, "get_timeline")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_timeline should have return type annotation"


    def test_get_timeline_pagination_params(self):
        """Test that get_timeline has pagination parameters."""
        method = getattr(UsersClient, "get_timeline")
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
        ), f"Paginated method get_timeline should have pagination parameters"


    def test_unmute_user_exists(self):
        """Test that unmute_user method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unmute_user", None)
        assert method is not None, f"Method unmute_user does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"unmute_user is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unmute_user should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "source_user_id",
            "target_user_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from unmute_user"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unmute_user_return_annotation(self):
        """Test that unmute_user has proper return type annotation."""
        method = getattr(UsersClient, "unmute_user")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unmute_user should have return type annotation"


    def test_delete_bookmark_exists(self):
        """Test that delete_bookmark method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "delete_bookmark", None)
        assert (
            method is not None
        ), f"Method delete_bookmark does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"delete_bookmark is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_bookmark should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from delete_bookmark"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_bookmark_return_annotation(self):
        """Test that delete_bookmark has proper return type annotation."""
        method = getattr(UsersClient, "delete_bookmark")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_bookmark should have return type annotation"


    def test_get_by_usernames_exists(self):
        """Test that get_by_usernames method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_by_usernames", None)
        assert (
            method is not None
        ), f"Method get_by_usernames does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_by_usernames is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_by_usernames should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "usernames",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_by_usernames"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_by_usernames_return_annotation(self):
        """Test that get_by_usernames has proper return type annotation."""
        method = getattr(UsersClient, "get_by_usernames")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_usernames should have return type annotation"


    def test_get_reposts_of_me_exists(self):
        """Test that get_reposts_of_me method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_reposts_of_me", None)
        assert (
            method is not None
        ), f"Method get_reposts_of_me does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_reposts_of_me is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_reposts_of_me should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_reposts_of_me"
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


    def test_get_reposts_of_me_return_annotation(self):
        """Test that get_reposts_of_me has proper return type annotation."""
        method = getattr(UsersClient, "get_reposts_of_me")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_reposts_of_me should have return type annotation"


    def test_get_reposts_of_me_pagination_params(self):
        """Test that get_reposts_of_me has pagination parameters."""
        method = getattr(UsersClient, "get_reposts_of_me")
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
        ), f"Paginated method get_reposts_of_me should have pagination parameters"


    def test_get_mentions_exists(self):
        """Test that get_mentions method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_mentions", None)
        assert method is not None, f"Method get_mentions does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_mentions is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_mentions should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_mentions"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "since_id",
            "until_id",
            "max_results",
            "pagination_token",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_mentions_return_annotation(self):
        """Test that get_mentions has proper return type annotation."""
        method = getattr(UsersClient, "get_mentions")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_mentions should have return type annotation"


    def test_get_mentions_pagination_params(self):
        """Test that get_mentions has pagination parameters."""
        method = getattr(UsersClient, "get_mentions")
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
        ), f"Paginated method get_mentions should have pagination parameters"


    def test_get_owned_lists_exists(self):
        """Test that get_owned_lists method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_owned_lists", None)
        assert (
            method is not None
        ), f"Method get_owned_lists does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_owned_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_owned_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_owned_lists"
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


    def test_get_owned_lists_return_annotation(self):
        """Test that get_owned_lists has proper return type annotation."""
        method = getattr(UsersClient, "get_owned_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_owned_lists should have return type annotation"


    def test_get_owned_lists_pagination_params(self):
        """Test that get_owned_lists has pagination parameters."""
        method = getattr(UsersClient, "get_owned_lists")
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
        ), f"Paginated method get_owned_lists should have pagination parameters"


    def test_get_posts_exists(self):
        """Test that get_posts method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_posts", None)
        assert method is not None, f"Method get_posts does not exist on UsersClient"
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
            "since_id",
            "until_id",
            "max_results",
            "pagination_token",
            "exclude",
            "start_time",
            "end_time",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_posts_return_annotation(self):
        """Test that get_posts has proper return type annotation."""
        method = getattr(UsersClient, "get_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts should have return type annotation"


    def test_get_posts_pagination_params(self):
        """Test that get_posts has pagination parameters."""
        method = getattr(UsersClient, "get_posts")
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


    def test_get_me_exists(self):
        """Test that get_me method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_me", None)
        assert method is not None, f"Method get_me does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_me is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_me should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_me"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_me_return_annotation(self):
        """Test that get_me has proper return type annotation."""
        method = getattr(UsersClient, "get_me")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_me should have return type annotation"


    def test_get_bookmarks_by_folder_id_exists(self):
        """Test that get_bookmarks_by_folder_id method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_bookmarks_by_folder_id", None)
        assert (
            method is not None
        ), f"Method get_bookmarks_by_folder_id does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_bookmarks_by_folder_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_bookmarks_by_folder_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_bookmarks_by_folder_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_bookmarks_by_folder_id_return_annotation(self):
        """Test that get_bookmarks_by_folder_id has proper return type annotation."""
        method = getattr(UsersClient, "get_bookmarks_by_folder_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_bookmarks_by_folder_id should have return type annotation"


    def test_unblock_dms_exists(self):
        """Test that unblock_dms method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unblock_dms", None)
        assert method is not None, f"Method unblock_dms does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"unblock_dms is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"unblock_dms should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from unblock_dms"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unblock_dms_return_annotation(self):
        """Test that unblock_dms has proper return type annotation."""
        method = getattr(UsersClient, "unblock_dms")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unblock_dms should have return type annotation"


    def test_get_followed_lists_exists(self):
        """Test that get_followed_lists method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_followed_lists", None)
        assert (
            method is not None
        ), f"Method get_followed_lists does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_followed_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_followed_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_followed_lists"
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


    def test_get_followed_lists_return_annotation(self):
        """Test that get_followed_lists has proper return type annotation."""
        method = getattr(UsersClient, "get_followed_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_followed_lists should have return type annotation"


    def test_get_followed_lists_pagination_params(self):
        """Test that get_followed_lists has pagination parameters."""
        method = getattr(UsersClient, "get_followed_lists")
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
        ), f"Paginated method get_followed_lists should have pagination parameters"


    def test_follow_list_exists(self):
        """Test that follow_list method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "follow_list", None)
        assert method is not None, f"Method follow_list does not exist on UsersClient"
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
        method = getattr(UsersClient, "follow_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method follow_list should have return type annotation"


    def test_get_followers_exists(self):
        """Test that get_followers method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_followers", None)
        assert method is not None, f"Method get_followers does not exist on UsersClient"
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
        method = getattr(UsersClient, "get_followers")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_followers should have return type annotation"


    def test_get_followers_pagination_params(self):
        """Test that get_followers has pagination parameters."""
        method = getattr(UsersClient, "get_followers")
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


    def test_get_pinned_lists_exists(self):
        """Test that get_pinned_lists method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_pinned_lists", None)
        assert (
            method is not None
        ), f"Method get_pinned_lists does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_pinned_lists is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_pinned_lists should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_pinned_lists"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_pinned_lists_return_annotation(self):
        """Test that get_pinned_lists has proper return type annotation."""
        method = getattr(UsersClient, "get_pinned_lists")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_pinned_lists should have return type annotation"


    def test_pin_list_exists(self):
        """Test that pin_list method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "pin_list", None)
        assert method is not None, f"Method pin_list does not exist on UsersClient"
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
        method = getattr(UsersClient, "pin_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method pin_list should have return type annotation"


    def test_block_dms_exists(self):
        """Test that block_dms method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "block_dms", None)
        assert method is not None, f"Method block_dms does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"block_dms is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"block_dms should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from block_dms"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_block_dms_return_annotation(self):
        """Test that block_dms has proper return type annotation."""
        method = getattr(UsersClient, "block_dms")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method block_dms should have return type annotation"


    def test_unpin_list_exists(self):
        """Test that unpin_list method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unpin_list", None)
        assert method is not None, f"Method unpin_list does not exist on UsersClient"
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
        method = getattr(UsersClient, "unpin_list")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unpin_list should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_list_memberships",
            "search",
            "like_post",
            "get_blocking",
            "unrepost_post",
            "get_liked_posts",
            "get_by_ids",
            "get_by_id",
            "get_by_username",
            "get_bookmarks",
            "create_bookmark",
            "get_muting",
            "mute_user",
            "get_bookmark_folders",
            "unfollow_list",
            "unfollow_user",
            "unlike_post",
            "get_following",
            "follow_user",
            "repost_post",
            "get_timeline",
            "unmute_user",
            "delete_bookmark",
            "get_by_usernames",
            "get_reposts_of_me",
            "get_mentions",
            "get_owned_lists",
            "get_posts",
            "get_me",
            "get_bookmarks_by_folder_id",
            "unblock_dms",
            "get_followed_lists",
            "follow_list",
            "get_followers",
            "get_pinned_lists",
            "pin_list",
            "block_dms",
            "unpin_list",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                UsersClient, expected_method
            ), f"Expected method '{expected_method}' not found on UsersClient"
            assert callable(
                getattr(UsersClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
