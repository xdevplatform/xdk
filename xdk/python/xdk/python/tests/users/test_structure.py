"""
Auto-generated structural tests for Users client.

This module contains tests that validate the structure and API surface
of the Users client. These tests ensure that all expected methods
exist and have the correct signatures.

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


    def test_get_users_blocking_exists(self):
        """Test that get_users_blocking method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_blocking", None)
        assert (
            method is not None
        ), f"Method get_users_blocking does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_blocking is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_blocking should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_blocking"
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


    def test_get_users_blocking_return_annotation(self):
        """Test that get_users_blocking has proper return type annotation."""
        method = getattr(UsersClient, "get_users_blocking")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_blocking should have return type annotation"


    def test_get_users_blocking_pagination_params(self):
        """Test that get_users_blocking has pagination parameters."""
        method = getattr(UsersClient, "get_users_blocking")
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
        ), f"Paginated method get_users_blocking should have pagination parameters"


    def test_get_lists_members_exists(self):
        """Test that get_lists_members method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_lists_members", None)
        assert (
            method is not None
        ), f"Method get_lists_members does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_lists_members is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_lists_members should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_lists_members"
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


    def test_get_lists_members_return_annotation(self):
        """Test that get_lists_members has proper return type annotation."""
        method = getattr(UsersClient, "get_lists_members")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_lists_members should have return type annotation"


    def test_get_lists_members_pagination_params(self):
        """Test that get_lists_members has pagination parameters."""
        method = getattr(UsersClient, "get_lists_members")
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
        ), f"Paginated method get_lists_members should have pagination parameters"


    def test_get_users_by_usernames_exists(self):
        """Test that get_users_by_usernames method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_by_usernames", None)
        assert (
            method is not None
        ), f"Method get_users_by_usernames does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_by_usernames is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_by_usernames should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_by_usernames"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_by_usernames_return_annotation(self):
        """Test that get_users_by_usernames has proper return type annotation."""
        method = getattr(UsersClient, "get_users_by_usernames")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_by_usernames should have return type annotation"


    def test_get_users_reposts_of_me_exists(self):
        """Test that get_users_reposts_of_me method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_reposts_of_me", None)
        assert (
            method is not None
        ), f"Method get_users_reposts_of_me does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_reposts_of_me is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_reposts_of_me should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_users_reposts_of_me"
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


    def test_get_users_reposts_of_me_return_annotation(self):
        """Test that get_users_reposts_of_me has proper return type annotation."""
        method = getattr(UsersClient, "get_users_reposts_of_me")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_reposts_of_me should have return type annotation"


    def test_get_users_reposts_of_me_pagination_params(self):
        """Test that get_users_reposts_of_me has pagination parameters."""
        method = getattr(UsersClient, "get_users_reposts_of_me")
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
        ), f"Paginated method get_users_reposts_of_me should have pagination parameters"


    def test_search_users_exists(self):
        """Test that search_users method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "search_users", None)
        assert method is not None, f"Method search_users does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"search_users is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search_users should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from search_users"
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


    def test_search_users_return_annotation(self):
        """Test that search_users has proper return type annotation."""
        method = getattr(UsersClient, "search_users")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_users should have return type annotation"


    def test_search_users_pagination_params(self):
        """Test that search_users has pagination parameters."""
        method = getattr(UsersClient, "search_users")
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
        ), f"Paginated method search_users should have pagination parameters"


    def test_get_users_followers_exists(self):
        """Test that get_users_followers method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_followers", None)
        assert (
            method is not None
        ), f"Method get_users_followers does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_followers is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_followers should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_followers"
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


    def test_get_users_followers_return_annotation(self):
        """Test that get_users_followers has proper return type annotation."""
        method = getattr(UsersClient, "get_users_followers")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_followers should have return type annotation"


    def test_get_users_followers_pagination_params(self):
        """Test that get_users_followers has pagination parameters."""
        method = getattr(UsersClient, "get_users_followers")
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
        ), f"Paginated method get_users_followers should have pagination parameters"


    def test_get_users_following_exists(self):
        """Test that get_users_following method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_following", None)
        assert (
            method is not None
        ), f"Method get_users_following does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_following is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_following should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_following"
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


    def test_get_users_following_return_annotation(self):
        """Test that get_users_following has proper return type annotation."""
        method = getattr(UsersClient, "get_users_following")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_following should have return type annotation"


    def test_get_users_following_pagination_params(self):
        """Test that get_users_following has pagination parameters."""
        method = getattr(UsersClient, "get_users_following")
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
        ), f"Paginated method get_users_following should have pagination parameters"


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


    def test_get_posts_liking_users_exists(self):
        """Test that get_posts_liking_users method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_posts_liking_users", None)
        assert (
            method is not None
        ), f"Method get_posts_liking_users does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_posts_liking_users is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_liking_users should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_liking_users"
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


    def test_get_posts_liking_users_return_annotation(self):
        """Test that get_posts_liking_users has proper return type annotation."""
        method = getattr(UsersClient, "get_posts_liking_users")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_liking_users should have return type annotation"


    def test_get_posts_liking_users_pagination_params(self):
        """Test that get_posts_liking_users has pagination parameters."""
        method = getattr(UsersClient, "get_posts_liking_users")
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
        ), f"Paginated method get_posts_liking_users should have pagination parameters"


    def test_get_posts_reposted_by_exists(self):
        """Test that get_posts_reposted_by method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_posts_reposted_by", None)
        assert (
            method is not None
        ), f"Method get_posts_reposted_by does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_posts_reposted_by is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_reposted_by should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_reposted_by"
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


    def test_get_posts_reposted_by_return_annotation(self):
        """Test that get_posts_reposted_by has proper return type annotation."""
        method = getattr(UsersClient, "get_posts_reposted_by")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_reposted_by should have return type annotation"


    def test_get_posts_reposted_by_pagination_params(self):
        """Test that get_posts_reposted_by has pagination parameters."""
        method = getattr(UsersClient, "get_posts_reposted_by")
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
        ), f"Paginated method get_posts_reposted_by should have pagination parameters"


    def test_get_users_by_id_exists(self):
        """Test that get_users_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_by_id", None)
        assert (
            method is not None
        ), f"Method get_users_by_id does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_by_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_by_id_return_annotation(self):
        """Test that get_users_by_id has proper return type annotation."""
        method = getattr(UsersClient, "get_users_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_by_id should have return type annotation"


    def test_get_users_by_ids_exists(self):
        """Test that get_users_by_ids method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_by_ids", None)
        assert (
            method is not None
        ), f"Method get_users_by_ids does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_by_ids is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_by_ids should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_by_ids"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_by_ids_return_annotation(self):
        """Test that get_users_by_ids has proper return type annotation."""
        method = getattr(UsersClient, "get_users_by_ids")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_by_ids should have return type annotation"


    def test_get_my_user_exists(self):
        """Test that get_my_user method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_my_user", None)
        assert method is not None, f"Method get_my_user does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_my_user is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_my_user should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_my_user"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_my_user_return_annotation(self):
        """Test that get_my_user has proper return type annotation."""
        method = getattr(UsersClient, "get_my_user")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_my_user should have return type annotation"


    def test_get_lists_followers_exists(self):
        """Test that get_lists_followers method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_lists_followers", None)
        assert (
            method is not None
        ), f"Method get_lists_followers does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_lists_followers is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_lists_followers should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_lists_followers"
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


    def test_get_lists_followers_return_annotation(self):
        """Test that get_lists_followers has proper return type annotation."""
        method = getattr(UsersClient, "get_lists_followers")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_lists_followers should have return type annotation"


    def test_get_lists_followers_pagination_params(self):
        """Test that get_lists_followers has pagination parameters."""
        method = getattr(UsersClient, "get_lists_followers")
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
        ), f"Paginated method get_lists_followers should have pagination parameters"


    def test_block_users_dms_exists(self):
        """Test that block_users_dms method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "block_users_dms", None)
        assert (
            method is not None
        ), f"Method block_users_dms does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"block_users_dms is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"block_users_dms should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from block_users_dms"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_block_users_dms_return_annotation(self):
        """Test that block_users_dms has proper return type annotation."""
        method = getattr(UsersClient, "block_users_dms")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method block_users_dms should have return type annotation"


    def test_unblock_users_dms_exists(self):
        """Test that unblock_users_dms method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "unblock_users_dms", None)
        assert (
            method is not None
        ), f"Method unblock_users_dms does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"unblock_users_dms is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"unblock_users_dms should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from unblock_users_dms"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_unblock_users_dms_return_annotation(self):
        """Test that unblock_users_dms has proper return type annotation."""
        method = getattr(UsersClient, "unblock_users_dms")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unblock_users_dms should have return type annotation"


    def test_get_users_muting_exists(self):
        """Test that get_users_muting method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_muting", None)
        assert (
            method is not None
        ), f"Method get_users_muting does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_muting is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_muting should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_muting"
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


    def test_get_users_muting_return_annotation(self):
        """Test that get_users_muting has proper return type annotation."""
        method = getattr(UsersClient, "get_users_muting")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_muting should have return type annotation"


    def test_get_users_muting_pagination_params(self):
        """Test that get_users_muting has pagination parameters."""
        method = getattr(UsersClient, "get_users_muting")
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
        ), f"Paginated method get_users_muting should have pagination parameters"


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


    def test_get_users_by_username_exists(self):
        """Test that get_users_by_username method exists with correct signature."""
        # Check method exists
        method = getattr(UsersClient, "get_users_by_username", None)
        assert (
            method is not None
        ), f"Method get_users_by_username does not exist on UsersClient"
        # Check method is callable
        assert callable(method), f"get_users_by_username is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_by_username should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_by_username"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_users_by_username_return_annotation(self):
        """Test that get_users_by_username has proper return type annotation."""
        method = getattr(UsersClient, "get_users_by_username")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_by_username should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_users_blocking",
            "get_lists_members",
            "get_users_by_usernames",
            "get_users_reposts_of_me",
            "search_users",
            "get_users_followers",
            "get_users_following",
            "follow_user",
            "get_posts_liking_users",
            "get_posts_reposted_by",
            "get_users_by_id",
            "get_users_by_ids",
            "get_my_user",
            "get_lists_followers",
            "block_users_dms",
            "unblock_users_dms",
            "get_users_muting",
            "mute_user",
            "unfollow_user",
            "unmute_user",
            "get_users_by_username",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                UsersClient, expected_method
            ), f"Expected method '{expected_method}' not found on UsersClient"
            assert callable(
                getattr(UsersClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
