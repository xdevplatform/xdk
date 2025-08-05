"""
Auto-generated structural tests for Likes client.

This module contains tests that validate the structure and API surface
of the Likes client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.likes.client import LikesClient
from xdk import Client


class TestLikesStructure:
    """Test the structure of LikesClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.likes_client = getattr(self.client, "likes")


    def test_stream_likes_firehose_exists(self):
        """Test that stream_likes_firehose method exists with correct signature."""
        # Check method exists
        method = getattr(LikesClient, "stream_likes_firehose", None)
        assert (
            method is not None
        ), f"Method stream_likes_firehose does not exist on LikesClient"
        # Check method is callable
        assert callable(method), f"stream_likes_firehose is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_likes_firehose should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_likes_firehose"
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


    def test_stream_likes_firehose_return_annotation(self):
        """Test that stream_likes_firehose has proper return type annotation."""
        method = getattr(LikesClient, "stream_likes_firehose")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_likes_firehose should have return type annotation"


    def test_stream_likes_sample10_exists(self):
        """Test that stream_likes_sample10 method exists with correct signature."""
        # Check method exists
        method = getattr(LikesClient, "stream_likes_sample10", None)
        assert (
            method is not None
        ), f"Method stream_likes_sample10 does not exist on LikesClient"
        # Check method is callable
        assert callable(method), f"stream_likes_sample10 is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"stream_likes_sample10 should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from stream_likes_sample10"
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


    def test_stream_likes_sample10_return_annotation(self):
        """Test that stream_likes_sample10 has proper return type annotation."""
        method = getattr(LikesClient, "stream_likes_sample10")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method stream_likes_sample10 should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "stream_likes_firehose",
            "stream_likes_sample10",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                LikesClient, expected_method
            ), f"Expected method '{expected_method}' not found on LikesClient"
            assert callable(
                getattr(LikesClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
