"""
Auto-generated structural tests for Community_Notes client.

This module contains tests that validate the structure and API surface
of the Community_Notes client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.community_notes.client import CommunityNotesClient
from xdk import Client


class TestCommunityNotesStructure:
    """Test the structure of CommunityNotesClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.community_notes_client = getattr(self.client, "community_notes")


    def test_create_notes_exists(self):
        """Test that create_notes method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "create_notes", None)
        assert (
            method is not None
        ), f"Method create_notes does not exist on CommunityNotesClient"
        # Check method is callable
        assert callable(method), f"create_notes is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"create_notes should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_notes"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_notes_return_annotation(self):
        """Test that create_notes has proper return type annotation."""
        method = getattr(CommunityNotesClient, "create_notes")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_notes should have return type annotation"


    def test_search_notes_written_exists(self):
        """Test that search_notes_written method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "search_notes_written", None)
        assert (
            method is not None
        ), f"Method search_notes_written does not exist on CommunityNotesClient"
        # Check method is callable
        assert callable(method), f"search_notes_written is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"search_notes_written should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "test_mode",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from search_notes_written"
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


    def test_search_notes_written_return_annotation(self):
        """Test that search_notes_written has proper return type annotation."""
        method = getattr(CommunityNotesClient, "search_notes_written")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_notes_written should have return type annotation"


    def test_search_notes_written_pagination_params(self):
        """Test that search_notes_written has pagination parameters."""
        method = getattr(CommunityNotesClient, "search_notes_written")
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
        ), f"Paginated method search_notes_written should have pagination parameters"


    def test_search_for_eligible_posts_exists(self):
        """Test that search_for_eligible_posts method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "search_for_eligible_posts", None)
        assert (
            method is not None
        ), f"Method search_for_eligible_posts does not exist on CommunityNotesClient"
        # Check method is callable
        assert callable(method), f"search_for_eligible_posts is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"search_for_eligible_posts should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "test_mode",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from search_for_eligible_posts"
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


    def test_search_for_eligible_posts_return_annotation(self):
        """Test that search_for_eligible_posts has proper return type annotation."""
        method = getattr(CommunityNotesClient, "search_for_eligible_posts")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method search_for_eligible_posts should have return type annotation"


    def test_search_for_eligible_posts_pagination_params(self):
        """Test that search_for_eligible_posts has pagination parameters."""
        method = getattr(CommunityNotesClient, "search_for_eligible_posts")
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
        ), f"Paginated method search_for_eligible_posts should have pagination parameters"


    def test_delete_notes_exists(self):
        """Test that delete_notes method exists with correct signature."""
        # Check method exists
        method = getattr(CommunityNotesClient, "delete_notes", None)
        assert (
            method is not None
        ), f"Method delete_notes does not exist on CommunityNotesClient"
        # Check method is callable
        assert callable(method), f"delete_notes is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"delete_notes should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from delete_notes"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_notes_return_annotation(self):
        """Test that delete_notes has proper return type annotation."""
        method = getattr(CommunityNotesClient, "delete_notes")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_notes should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "create_notes",
            "search_notes_written",
            "search_for_eligible_posts",
            "delete_notes",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                CommunityNotesClient, expected_method
            ), f"Expected method '{expected_method}' not found on CommunityNotesClient"
            assert callable(
                getattr(CommunityNotesClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
