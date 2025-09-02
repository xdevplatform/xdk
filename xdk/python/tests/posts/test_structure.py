"""
Auto-generated structural tests for {"class_name": "Posts", "display_name": "posts", "import_name": "posts", "original": ["posts"], "property_name": "posts"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "Posts", "display_name": "posts", "import_name": "posts", "original": ["posts"], "property_name": "posts"} client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.posts.client import PostsClient
from xdk import Client


class TestPostsStructure:
    """Test the structure of PostsClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.posts_client = getattr(self.client, "posts")


    def test_get_analytics_exists(self):
        """Test that get_analytics method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_analytics", None)
        assert method is not None, f"Method get_analytics does not exist on PostsClient"
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
            "ids",
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
        method = getattr(PostsClient, "get_analytics")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_analytics should have return type annotation"


    def test_get_counts_all_exists(self):
        """Test that get_counts_all method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_counts_all", None)
        assert (
            method is not None
        ), f"Method get_counts_all does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_counts_all is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_counts_all should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_counts_all"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "start_time",
            "end_time",
            "since_id",
            "until_id",
            "next_token",
            "pagination_token",
            "granularity",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_counts_all_return_annotation(self):
        """Test that get_counts_all has proper return type annotation."""
        method = getattr(PostsClient, "get_counts_all")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_counts_all should have return type annotation"


    def test_get_reposts_exists(self):
        """Test that get_reposts method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_reposts", None)
        assert method is not None, f"Method get_reposts does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_reposts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_reposts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_reposts"
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


    def test_get_reposts_return_annotation(self):
        """Test that get_reposts has proper return type annotation."""
        method = getattr(PostsClient, "get_reposts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_reposts should have return type annotation"


    def test_get_reposts_pagination_params(self):
        """Test that get_reposts has pagination parameters."""
        method = getattr(PostsClient, "get_reposts")
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
        ), f"Paginated method get_reposts should have pagination parameters"


    def test_get_reposted_by_exists(self):
        """Test that get_reposted_by method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_reposted_by", None)
        assert (
            method is not None
        ), f"Method get_reposted_by does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_reposted_by is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_reposted_by should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_reposted_by"
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


    def test_get_reposted_by_return_annotation(self):
        """Test that get_reposted_by has proper return type annotation."""
        method = getattr(PostsClient, "get_reposted_by")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_reposted_by should have return type annotation"


    def test_get_reposted_by_pagination_params(self):
        """Test that get_reposted_by has pagination parameters."""
        method = getattr(PostsClient, "get_reposted_by")
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
        ), f"Paginated method get_reposted_by should have pagination parameters"


    def test_hide_reply_exists(self):
        """Test that hide_reply method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "hide_reply", None)
        assert method is not None, f"Method hide_reply does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"hide_reply is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"hide_reply should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "tweet_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from hide_reply"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_hide_reply_return_annotation(self):
        """Test that hide_reply has proper return type annotation."""
        method = getattr(PostsClient, "hide_reply")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method hide_reply should have return type annotation"


    def test_get_counts_recent_exists(self):
        """Test that get_counts_recent method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_counts_recent", None)
        assert (
            method is not None
        ), f"Method get_counts_recent does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_counts_recent is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_counts_recent should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_counts_recent"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "start_time",
            "end_time",
            "since_id",
            "until_id",
            "next_token",
            "pagination_token",
            "granularity",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_counts_recent_return_annotation(self):
        """Test that get_counts_recent has proper return type annotation."""
        method = getattr(PostsClient, "get_counts_recent")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_counts_recent should have return type annotation"


    def test_get_liking_users_exists(self):
        """Test that get_liking_users method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_liking_users", None)
        assert (
            method is not None
        ), f"Method get_liking_users does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_liking_users is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_liking_users should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_liking_users"
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


    def test_get_liking_users_return_annotation(self):
        """Test that get_liking_users has proper return type annotation."""
        method = getattr(PostsClient, "get_liking_users")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_liking_users should have return type annotation"


    def test_get_liking_users_pagination_params(self):
        """Test that get_liking_users has pagination parameters."""
        method = getattr(PostsClient, "get_liking_users")
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
        ), f"Paginated method get_liking_users should have pagination parameters"


    def test_get_insights_historical_exists(self):
        """Test that get_insights_historical method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_insights_historical", None)
        assert (
            method is not None
        ), f"Method get_insights_historical does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_insights_historical is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_insights_historical should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "tweet_ids",
            "end_time",
            "start_time",
            "granularity",
            "requested_metrics",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_insights_historical"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_insights_historical_return_annotation(self):
        """Test that get_insights_historical has proper return type annotation."""
        method = getattr(PostsClient, "get_insights_historical")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_insights_historical should have return type annotation"


    def test_get_by_ids_exists(self):
        """Test that get_by_ids method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_by_ids", None)
        assert method is not None, f"Method get_by_ids does not exist on PostsClient"
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
        method = getattr(PostsClient, "get_by_ids")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_ids should have return type annotation"


    def test_create_exists(self):
        """Test that create method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "create", None)
        assert method is not None, f"Method create does not exist on PostsClient"
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
        method = getattr(PostsClient, "create")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create should have return type annotation"


    def test_search_all_exists(self):
        """Test that search_all method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "search_all", None)
        assert method is not None, f"Method search_all does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"search_all is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search_all should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from search_all"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "start_time",
            "end_time",
            "since_id",
            "until_id",
            "max_results",
            "next_token",
            "pagination_token",
            "sort_order",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_search_all_return_annotation(self):
        """Test that search_all has proper return type annotation."""
        method = getattr(PostsClient, "search_all")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_all should have return type annotation"


    def test_search_all_pagination_params(self):
        """Test that search_all has pagination parameters."""
        method = getattr(PostsClient, "search_all")
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
        ), f"Paginated method search_all should have pagination parameters"


    def test_search_recent_exists(self):
        """Test that search_recent method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "search_recent", None)
        assert method is not None, f"Method search_recent does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"search_recent is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"search_recent should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from search_recent"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "start_time",
            "end_time",
            "since_id",
            "until_id",
            "max_results",
            "next_token",
            "pagination_token",
            "sort_order",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_search_recent_return_annotation(self):
        """Test that search_recent has proper return type annotation."""
        method = getattr(PostsClient, "search_recent")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_recent should have return type annotation"


    def test_search_recent_pagination_params(self):
        """Test that search_recent has pagination parameters."""
        method = getattr(PostsClient, "search_recent")
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
        ), f"Paginated method search_recent should have pagination parameters"


    def test_get_by_id_exists(self):
        """Test that get_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_by_id", None)
        assert method is not None, f"Method get_by_id does not exist on PostsClient"
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
        method = getattr(PostsClient, "get_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_by_id should have return type annotation"


    def test_delete_exists(self):
        """Test that delete method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "delete", None)
        assert method is not None, f"Method delete does not exist on PostsClient"
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
        method = getattr(PostsClient, "delete")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete should have return type annotation"


    def test_get_quoted_exists(self):
        """Test that get_quoted method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_quoted", None)
        assert method is not None, f"Method get_quoted does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_quoted is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_quoted should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_quoted"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "pagination_token",
            "exclude",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_quoted_return_annotation(self):
        """Test that get_quoted has proper return type annotation."""
        method = getattr(PostsClient, "get_quoted")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_quoted should have return type annotation"


    def test_get_quoted_pagination_params(self):
        """Test that get_quoted has pagination parameters."""
        method = getattr(PostsClient, "get_quoted")
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
        ), f"Paginated method get_quoted should have pagination parameters"


    def test_get_insights28hr_exists(self):
        """Test that get_insights28hr method exists with correct signature."""
        # Check method exists
        method = getattr(PostsClient, "get_insights28hr", None)
        assert (
            method is not None
        ), f"Method get_insights28hr does not exist on PostsClient"
        # Check method is callable
        assert callable(method), f"get_insights28hr is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_insights28hr should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "tweet_ids",
            "granularity",
            "requested_metrics",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_insights28hr"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_insights28hr_return_annotation(self):
        """Test that get_insights28hr has proper return type annotation."""
        method = getattr(PostsClient, "get_insights28hr")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_insights28hr should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_analytics",
            "get_counts_all",
            "get_reposts",
            "get_reposted_by",
            "hide_reply",
            "get_counts_recent",
            "get_liking_users",
            "get_insights_historical",
            "get_by_ids",
            "create",
            "search_all",
            "search_recent",
            "get_by_id",
            "delete",
            "get_quoted",
            "get_insights28hr",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                PostsClient, expected_method
            ), f"Expected method '{expected_method}' not found on PostsClient"
            assert callable(
                getattr(PostsClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
