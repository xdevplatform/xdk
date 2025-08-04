"""
Auto-generated structural tests for Tweets client.

This module contains tests that validate the structure and API surface
of the Tweets client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.tweets.client import TweetsClient
from xdk import Client


class TestTweetsStructure:
    """Test the structure of TweetsClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.tweets_client = getattr(self.client, "tweets")

    def test_client_exists(self):
        """Test that TweetsClient class exists and is importable."""
        assert TweetsClient is not None
        assert hasattr(TweetsClient, "__name__")
        assert TweetsClient.__name__ == "TweetsClient"

    def test_client_initialization(self):
        """Test that TweetsClient can be initialized properly."""
        assert self.tweets_client is not None
        assert isinstance(self.tweets_client, TweetsClient)

    def test_get_posts_analytics_exists(self):
        """Test that get_posts_analytics method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_analytics", None)
        assert (
            method is not None
        ), f"Method get_posts_analytics does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_analytics is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_analytics should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_analytics"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_posts_analytics_return_annotation(self):
        """Test that get_posts_analytics has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_analytics")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_analytics should have return type annotation"

    def test_stream_posts_firehose_exists(self):
        """Test that stream_posts_firehose method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_firehose", None)
        assert (
            method is not None
        ), f"Method stream_posts_firehose does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_firehose is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_firehose should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_posts_firehose"
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

    def test_stream_posts_firehose_return_annotation(self):
        """Test that stream_posts_firehose has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_firehose")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_firehose should have return type annotation"

    def test_stream_posts_firehose_en_exists(self):
        """Test that stream_posts_firehose_en method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_firehose_en", None)
        assert (
            method is not None
        ), f"Method stream_posts_firehose_en does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_en is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_firehose_en should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_posts_firehose_en"
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

    def test_stream_posts_firehose_en_return_annotation(self):
        """Test that stream_posts_firehose_en has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_firehose_en")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_firehose_en should have return type annotation"

    def test_stream_posts_sample_exists(self):
        """Test that stream_posts_sample method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_sample", None)
        assert (
            method is not None
        ), f"Method stream_posts_sample does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_sample is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_sample should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from stream_posts_sample"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "backfill_minutes",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_stream_posts_sample_return_annotation(self):
        """Test that stream_posts_sample has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_sample")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_sample should have return type annotation"

    def test_stream_posts_exists(self):
        """Test that stream_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts", None)
        assert method is not None, f"Method stream_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"stream_posts should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from stream_posts"
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

    def test_stream_posts_return_annotation(self):
        """Test that stream_posts has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts should have return type annotation"

    def test_get_rule_counts_exists(self):
        """Test that get_rule_counts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_rule_counts", None)
        assert (
            method is not None
        ), f"Method get_rule_counts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_rule_counts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_rule_counts should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_rule_counts"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_rule_counts_return_annotation(self):
        """Test that get_rule_counts has proper return type annotation."""
        method = getattr(TweetsClient, "get_rule_counts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_rule_counts should have return type annotation"

    def test_get_posts_reposts_exists(self):
        """Test that get_posts_reposts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_reposts", None)
        assert (
            method is not None
        ), f"Method get_posts_reposts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_reposts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_reposts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_reposts"
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

    def test_get_posts_reposts_return_annotation(self):
        """Test that get_posts_reposts has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_reposts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_reposts should have return type annotation"

    def test_get_posts_reposts_pagination_params(self):
        """Test that get_posts_reposts has pagination parameters."""
        method = getattr(TweetsClient, "get_posts_reposts")
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
        ), f"Paginated method get_posts_reposts should have pagination parameters"

    def test_get_users_posts_exists(self):
        """Test that get_users_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_users_posts", None)
        assert (
            method is not None
        ), f"Method get_users_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_users_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_posts"
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

    def test_get_users_posts_return_annotation(self):
        """Test that get_users_posts has proper return type annotation."""
        method = getattr(TweetsClient, "get_users_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_posts should have return type annotation"

    def test_get_users_posts_pagination_params(self):
        """Test that get_users_posts has pagination parameters."""
        method = getattr(TweetsClient, "get_users_posts")
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
        ), f"Paginated method get_users_posts should have pagination parameters"

    def test_get_users_mentions_exists(self):
        """Test that get_users_mentions method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_users_mentions", None)
        assert (
            method is not None
        ), f"Method get_users_mentions does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_users_mentions is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_mentions should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_mentions"
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

    def test_get_users_mentions_return_annotation(self):
        """Test that get_users_mentions has proper return type annotation."""
        method = getattr(TweetsClient, "get_users_mentions")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_mentions should have return type annotation"

    def test_get_users_mentions_pagination_params(self):
        """Test that get_users_mentions has pagination parameters."""
        method = getattr(TweetsClient, "get_users_mentions")
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
        ), f"Paginated method get_users_mentions should have pagination parameters"

    def test_get_posts_by_ids_exists(self):
        """Test that get_posts_by_ids method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_by_ids", None)
        assert (
            method is not None
        ), f"Method get_posts_by_ids does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_by_ids is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_by_ids should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_by_ids"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_posts_by_ids_return_annotation(self):
        """Test that get_posts_by_ids has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_by_ids")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_by_ids should have return type annotation"

    def test_create_posts_exists(self):
        """Test that create_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "create_posts", None)
        assert method is not None, f"Method create_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"create_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_posts should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_posts"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_create_posts_return_annotation(self):
        """Test that create_posts has proper return type annotation."""
        method = getattr(TweetsClient, "create_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_posts should have return type annotation"

    def test_stream_posts_firehose_ko_exists(self):
        """Test that stream_posts_firehose_ko method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_firehose_ko", None)
        assert (
            method is not None
        ), f"Method stream_posts_firehose_ko does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_ko is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_firehose_ko should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_posts_firehose_ko"
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

    def test_stream_posts_firehose_ko_return_annotation(self):
        """Test that stream_posts_firehose_ko has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_firehose_ko")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_firehose_ko should have return type annotation"

    def test_stream_posts_firehose_ja_exists(self):
        """Test that stream_posts_firehose_ja method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_firehose_ja", None)
        assert (
            method is not None
        ), f"Method stream_posts_firehose_ja does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_ja is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_firehose_ja should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_posts_firehose_ja"
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

    def test_stream_posts_firehose_ja_return_annotation(self):
        """Test that stream_posts_firehose_ja has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_firehose_ja")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_firehose_ja should have return type annotation"

    def test_get_posts_quoted_posts_exists(self):
        """Test that get_posts_quoted_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_quoted_posts", None)
        assert (
            method is not None
        ), f"Method get_posts_quoted_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_quoted_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_quoted_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_quoted_posts"
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

    def test_get_posts_quoted_posts_return_annotation(self):
        """Test that get_posts_quoted_posts has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_quoted_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_quoted_posts should have return type annotation"

    def test_get_posts_quoted_posts_pagination_params(self):
        """Test that get_posts_quoted_posts has pagination parameters."""
        method = getattr(TweetsClient, "get_posts_quoted_posts")
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
        ), f"Paginated method get_posts_quoted_posts should have pagination parameters"

    def test_get_lists_posts_exists(self):
        """Test that get_lists_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_lists_posts", None)
        assert (
            method is not None
        ), f"Method get_lists_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_lists_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_lists_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_lists_posts"
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

    def test_get_lists_posts_return_annotation(self):
        """Test that get_lists_posts has proper return type annotation."""
        method = getattr(TweetsClient, "get_lists_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_lists_posts should have return type annotation"

    def test_get_lists_posts_pagination_params(self):
        """Test that get_lists_posts has pagination parameters."""
        method = getattr(TweetsClient, "get_lists_posts")
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
        ), f"Paginated method get_lists_posts should have pagination parameters"

    def test_get_spaces_posts_exists(self):
        """Test that get_spaces_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_spaces_posts", None)
        assert (
            method is not None
        ), f"Method get_spaces_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_spaces_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_spaces_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_spaces_posts"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_spaces_posts_return_annotation(self):
        """Test that get_spaces_posts has proper return type annotation."""
        method = getattr(TweetsClient, "get_spaces_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_spaces_posts should have return type annotation"

    def test_get_spaces_posts_pagination_params(self):
        """Test that get_spaces_posts has pagination parameters."""
        method = getattr(TweetsClient, "get_spaces_posts")
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
        ), f"Paginated method get_spaces_posts should have pagination parameters"

    def test_get_posts_counts_all_exists(self):
        """Test that get_posts_counts_all method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_counts_all", None)
        assert (
            method is not None
        ), f"Method get_posts_counts_all does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_counts_all is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_counts_all should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_counts_all"
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

    def test_get_posts_counts_all_return_annotation(self):
        """Test that get_posts_counts_all has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_counts_all")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_counts_all should have return type annotation"

    def test_get_posts_counts_all_pagination_params(self):
        """Test that get_posts_counts_all has pagination parameters."""
        method = getattr(TweetsClient, "get_posts_counts_all")
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
        ), f"Paginated method get_posts_counts_all should have pagination parameters"

    def test_search_posts_recent_exists(self):
        """Test that search_posts_recent method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "search_posts_recent", None)
        assert (
            method is not None
        ), f"Method search_posts_recent does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"search_posts_recent is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"search_posts_recent should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from search_posts_recent"
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

    def test_search_posts_recent_return_annotation(self):
        """Test that search_posts_recent has proper return type annotation."""
        method = getattr(TweetsClient, "search_posts_recent")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_posts_recent should have return type annotation"

    def test_search_posts_recent_pagination_params(self):
        """Test that search_posts_recent has pagination parameters."""
        method = getattr(TweetsClient, "search_posts_recent")
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
        ), f"Paginated method search_posts_recent should have pagination parameters"

    def test_get_posts_counts_recent_exists(self):
        """Test that get_posts_counts_recent method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_counts_recent", None)
        assert (
            method is not None
        ), f"Method get_posts_counts_recent does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_counts_recent is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_counts_recent should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_counts_recent"
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

    def test_get_posts_counts_recent_return_annotation(self):
        """Test that get_posts_counts_recent has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_counts_recent")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_counts_recent should have return type annotation"

    def test_get_posts_counts_recent_pagination_params(self):
        """Test that get_posts_counts_recent has pagination parameters."""
        method = getattr(TweetsClient, "get_posts_counts_recent")
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
        ), f"Paginated method get_posts_counts_recent should have pagination parameters"

    def test_get_users_liked_posts_exists(self):
        """Test that get_users_liked_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_users_liked_posts", None)
        assert (
            method is not None
        ), f"Method get_users_liked_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_users_liked_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_liked_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_liked_posts"
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

    def test_get_users_liked_posts_return_annotation(self):
        """Test that get_users_liked_posts has proper return type annotation."""
        method = getattr(TweetsClient, "get_users_liked_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_liked_posts should have return type annotation"

    def test_get_users_liked_posts_pagination_params(self):
        """Test that get_users_liked_posts has pagination parameters."""
        method = getattr(TweetsClient, "get_users_liked_posts")
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
        ), f"Paginated method get_users_liked_posts should have pagination parameters"

    def test_like_post_exists(self):
        """Test that like_post method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "like_post", None)
        assert method is not None, f"Method like_post does not exist on TweetsClient"
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
        method = getattr(TweetsClient, "like_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method like_post should have return type annotation"

    def test_unrepost_post_exists(self):
        """Test that unrepost_post method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "unrepost_post", None)
        assert (
            method is not None
        ), f"Method unrepost_post does not exist on TweetsClient"
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
        method = getattr(TweetsClient, "unrepost_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unrepost_post should have return type annotation"

    def test_get_rules_exists(self):
        """Test that get_rules method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_rules", None)
        assert method is not None, f"Method get_rules does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_rules is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_rules should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_rules"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "ids",
            "max_results",
            "pagination_token",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_rules_return_annotation(self):
        """Test that get_rules has proper return type annotation."""
        method = getattr(TweetsClient, "get_rules")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_rules should have return type annotation"

    def test_get_rules_pagination_params(self):
        """Test that get_rules has pagination parameters."""
        method = getattr(TweetsClient, "get_rules")
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
        ), f"Paginated method get_rules should have pagination parameters"

    def test_update_rules_exists(self):
        """Test that update_rules method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "update_rules", None)
        assert method is not None, f"Method update_rules does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"update_rules is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"update_rules should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from update_rules"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "dry_run",
            "delete_all",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_update_rules_return_annotation(self):
        """Test that update_rules has proper return type annotation."""
        method = getattr(TweetsClient, "update_rules")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method update_rules should have return type annotation"

    def test_search_posts_all_exists(self):
        """Test that search_posts_all method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "search_posts_all", None)
        assert (
            method is not None
        ), f"Method search_posts_all does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"search_posts_all is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"search_posts_all should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from search_posts_all"
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

    def test_search_posts_all_return_annotation(self):
        """Test that search_posts_all has proper return type annotation."""
        method = getattr(TweetsClient, "search_posts_all")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_posts_all should have return type annotation"

    def test_search_posts_all_pagination_params(self):
        """Test that search_posts_all has pagination parameters."""
        method = getattr(TweetsClient, "search_posts_all")
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
        ), f"Paginated method search_posts_all should have pagination parameters"

    def test_get_posts_by_id_exists(self):
        """Test that get_posts_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_posts_by_id", None)
        assert (
            method is not None
        ), f"Method get_posts_by_id does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_posts_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_posts_by_id should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_posts_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_posts_by_id_return_annotation(self):
        """Test that get_posts_by_id has proper return type annotation."""
        method = getattr(TweetsClient, "get_posts_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_posts_by_id should have return type annotation"

    def test_delete_posts_exists(self):
        """Test that delete_posts method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "delete_posts", None)
        assert method is not None, f"Method delete_posts does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"delete_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete_posts should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from delete_posts"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_delete_posts_return_annotation(self):
        """Test that delete_posts has proper return type annotation."""
        method = getattr(TweetsClient, "delete_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_posts should have return type annotation"

    def test_hide_posts_reply_exists(self):
        """Test that hide_posts_reply method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "hide_posts_reply", None)
        assert (
            method is not None
        ), f"Method hide_posts_reply does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"hide_posts_reply is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"hide_posts_reply should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from hide_posts_reply"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_hide_posts_reply_return_annotation(self):
        """Test that hide_posts_reply has proper return type annotation."""
        method = getattr(TweetsClient, "hide_posts_reply")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method hide_posts_reply should have return type annotation"

    def test_get_spaces_buyers_exists(self):
        """Test that get_spaces_buyers method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_spaces_buyers", None)
        assert (
            method is not None
        ), f"Method get_spaces_buyers does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_spaces_buyers is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_spaces_buyers should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_spaces_buyers"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "pagination_token",
            "max_results",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_spaces_buyers_return_annotation(self):
        """Test that get_spaces_buyers has proper return type annotation."""
        method = getattr(TweetsClient, "get_spaces_buyers")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_spaces_buyers should have return type annotation"

    def test_get_spaces_buyers_pagination_params(self):
        """Test that get_spaces_buyers has pagination parameters."""
        method = getattr(TweetsClient, "get_spaces_buyers")
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
        ), f"Paginated method get_spaces_buyers should have pagination parameters"

    def test_get_users_timeline_exists(self):
        """Test that get_users_timeline method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_users_timeline", None)
        assert (
            method is not None
        ), f"Method get_users_timeline does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_users_timeline is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_users_timeline should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_users_timeline"
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

    def test_get_users_timeline_return_annotation(self):
        """Test that get_users_timeline has proper return type annotation."""
        method = getattr(TweetsClient, "get_users_timeline")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_users_timeline should have return type annotation"

    def test_get_users_timeline_pagination_params(self):
        """Test that get_users_timeline has pagination parameters."""
        method = getattr(TweetsClient, "get_users_timeline")
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
        ), f"Paginated method get_users_timeline should have pagination parameters"

    def test_get_insights_historical_exists(self):
        """Test that get_insights_historical method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_insights_historical", None)
        assert (
            method is not None
        ), f"Method get_insights_historical does not exist on TweetsClient"
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
        method = getattr(TweetsClient, "get_insights_historical")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_insights_historical should have return type annotation"

    def test_stream_posts_sample10_exists(self):
        """Test that stream_posts_sample10 method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_sample10", None)
        assert (
            method is not None
        ), f"Method stream_posts_sample10 does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_sample10 is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_sample10 should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_posts_sample10"
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

    def test_stream_posts_sample10_return_annotation(self):
        """Test that stream_posts_sample10 has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_sample10")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_sample10 should have return type annotation"

    def test_unlike_post_exists(self):
        """Test that unlike_post method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "unlike_post", None)
        assert method is not None, f"Method unlike_post does not exist on TweetsClient"
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
        method = getattr(TweetsClient, "unlike_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method unlike_post should have return type annotation"

    def test_repost_post_exists(self):
        """Test that repost_post method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "repost_post", None)
        assert method is not None, f"Method repost_post does not exist on TweetsClient"
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
        method = getattr(TweetsClient, "repost_post")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method repost_post should have return type annotation"

    def test_get_insights28_hr_exists(self):
        """Test that get_insights28_hr method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "get_insights28_hr", None)
        assert (
            method is not None
        ), f"Method get_insights28_hr does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"get_insights28_hr is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_insights28_hr should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_insights28_hr"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"

    def test_get_insights28_hr_return_annotation(self):
        """Test that get_insights28_hr has proper return type annotation."""
        method = getattr(TweetsClient, "get_insights28_hr")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_insights28_hr should have return type annotation"

    def test_stream_posts_firehose_pt_exists(self):
        """Test that stream_posts_firehose_pt method exists with correct signature."""
        # Check method exists
        method = getattr(TweetsClient, "stream_posts_firehose_pt", None)
        assert (
            method is not None
        ), f"Method stream_posts_firehose_pt does not exist on TweetsClient"
        # Check method is callable
        assert callable(method), f"stream_posts_firehose_pt is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_posts_firehose_pt should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_posts_firehose_pt"
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

    def test_stream_posts_firehose_pt_return_annotation(self):
        """Test that stream_posts_firehose_pt has proper return type annotation."""
        method = getattr(TweetsClient, "stream_posts_firehose_pt")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_posts_firehose_pt should have return type annotation"

    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_posts_analytics",
            "stream_posts_firehose",
            "stream_posts_firehose_en",
            "stream_posts_sample",
            "stream_posts",
            "get_rule_counts",
            "get_posts_reposts",
            "get_users_posts",
            "get_users_mentions",
            "get_posts_by_ids",
            "create_posts",
            "stream_posts_firehose_ko",
            "stream_posts_firehose_ja",
            "get_posts_quoted_posts",
            "get_lists_posts",
            "get_spaces_posts",
            "get_posts_counts_all",
            "search_posts_recent",
            "get_posts_counts_recent",
            "get_users_liked_posts",
            "like_post",
            "unrepost_post",
            "get_rules",
            "update_rules",
            "search_posts_all",
            "get_posts_by_id",
            "delete_posts",
            "hide_posts_reply",
            "get_spaces_buyers",
            "get_users_timeline",
            "get_insights_historical",
            "stream_posts_sample10",
            "unlike_post",
            "repost_post",
            "get_insights28_hr",
            "stream_posts_firehose_pt",
        ]
        client_methods = [
            name
            for name in dir(TweetsClient)
            if not name.startswith("_") and callable(getattr(TweetsClient, name))
        ]
        for expected_method in expected_methods:
            assert (
                expected_method in client_methods
            ), f"Expected method '{expected_method}' not found on TweetsClient"

    def test_no_unexpected_public_methods(self):
        """Test that no unexpected public methods exist (helps catch API drift)."""
        expected_methods = set(
            [
                "get_posts_analytics",
                "stream_posts_firehose",
                "stream_posts_firehose_en",
                "stream_posts_sample",
                "stream_posts",
                "get_rule_counts",
                "get_posts_reposts",
                "get_users_posts",
                "get_users_mentions",
                "get_posts_by_ids",
                "create_posts",
                "stream_posts_firehose_ko",
                "stream_posts_firehose_ja",
                "get_posts_quoted_posts",
                "get_lists_posts",
                "get_spaces_posts",
                "get_posts_counts_all",
                "search_posts_recent",
                "get_posts_counts_recent",
                "get_users_liked_posts",
                "like_post",
                "unrepost_post",
                "get_rules",
                "update_rules",
                "search_posts_all",
                "get_posts_by_id",
                "delete_posts",
                "hide_posts_reply",
                "get_spaces_buyers",
                "get_users_timeline",
                "get_insights_historical",
                "stream_posts_sample10",
                "unlike_post",
                "repost_post",
                "get_insights28_hr",
                "stream_posts_firehose_pt",
            ]
        )
        actual_methods = set(
            [
                name
                for name in dir(TweetsClient)
                if not name.startswith("_") and callable(getattr(TweetsClient, name))
            ]
        )
        # Remove standard methods that might be inherited
        standard_methods = {"__init__"}
        actual_methods = actual_methods - standard_methods
        unexpected_methods = actual_methods - expected_methods
        # This is a warning, not a failure, since new methods might be added
        if unexpected_methods:
            print(
                f"Warning: Unexpected methods found on TweetsClient: {unexpected_methods}"
            )

    def test_imports_work(self):
        """Test that all expected imports work correctly."""
        expected_imports = [
            "typing",
            "requests",
            "pydantic",
        ]
        for import_name in expected_imports:
            try:
                __import__(import_name)
            except ImportError as e:
                pytest.fail(f"Expected import '{import_name}' failed: {e}")
