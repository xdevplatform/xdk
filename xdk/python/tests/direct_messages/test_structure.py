"""
Auto-generated structural tests for {"class_name": "DirectMessages", "display_name": "direct messages", "import_name": "direct_messages", "original": ["direct", "messages"], "property_name": "direct_messages"} client.

This module contains tests that validate the structure and API surface
of the {"class_name": "DirectMessages", "display_name": "direct messages", "import_name": "direct_messages", "original": ["direct", "messages"], "property_name": "direct_messages"} client. These tests ensure that all expected methods
exist and have the correct signatures.

Generated automatically - do not edit manually.
"""

import pytest
import inspect
from typing import get_type_hints
from xdk.direct_messages.client import DirectMessagesClient
from xdk import Client


class TestDirectMessagesStructure:
    """Test the structure of DirectMessagesClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.direct_messages_client = getattr(self.client, "direct_messages")


    def test_get_dm_events_by_participant_id_exists(self):
        """Test that get_dm_events_by_participant_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_dm_events_by_participant_id", None)
        assert (
            method is not None
        ), f"Method get_dm_events_by_participant_id does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"get_dm_events_by_participant_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_dm_events_by_participant_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "participant_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_dm_events_by_participant_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "pagination_token",
            "event_types",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_dm_events_by_participant_id_return_annotation(self):
        """Test that get_dm_events_by_participant_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_dm_events_by_participant_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_dm_events_by_participant_id should have return type annotation"


    def test_get_dm_events_by_participant_id_pagination_params(self):
        """Test that get_dm_events_by_participant_id has pagination parameters."""
        method = getattr(DirectMessagesClient, "get_dm_events_by_participant_id")
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
        ), f"Paginated method get_dm_events_by_participant_id should have pagination parameters"


    def test_create_dm_by_participant_id_exists(self):
        """Test that create_dm_by_participant_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "create_dm_by_participant_id", None)
        assert (
            method is not None
        ), f"Method create_dm_by_participant_id does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"create_dm_by_participant_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_dm_by_participant_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "participant_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_dm_by_participant_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_dm_by_participant_id_return_annotation(self):
        """Test that create_dm_by_participant_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "create_dm_by_participant_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_dm_by_participant_id should have return type annotation"


    def test_create_dm_by_conversation_id_exists(self):
        """Test that create_dm_by_conversation_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "create_dm_by_conversation_id", None)
        assert (
            method is not None
        ), f"Method create_dm_by_conversation_id does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"create_dm_by_conversation_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_dm_by_conversation_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "dm_conversation_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_dm_by_conversation_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_dm_by_conversation_id_return_annotation(self):
        """Test that create_dm_by_conversation_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "create_dm_by_conversation_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_dm_by_conversation_id should have return type annotation"


    def test_create_dm_conversations_exists(self):
        """Test that create_dm_conversations method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "create_dm_conversations", None)
        assert (
            method is not None
        ), f"Method create_dm_conversations does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"create_dm_conversations is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"create_dm_conversations should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from create_dm_conversations"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_create_dm_conversations_return_annotation(self):
        """Test that create_dm_conversations has proper return type annotation."""
        method = getattr(DirectMessagesClient, "create_dm_conversations")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method create_dm_conversations should have return type annotation"


    def test_get_events_exists(self):
        """Test that get_events method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_events", None)
        assert (
            method is not None
        ), f"Method get_events does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"get_events is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert len(params) >= 1, f"get_events should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = []
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_events"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "pagination_token",
            "event_types",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_events_return_annotation(self):
        """Test that get_events has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_events")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_events should have return type annotation"


    def test_get_events_pagination_params(self):
        """Test that get_events has pagination parameters."""
        method = getattr(DirectMessagesClient, "get_events")
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
        ), f"Paginated method get_events should have pagination parameters"


    def test_get_dm_conversations_id_dm_events_exists(self):
        """Test that get_dm_conversations_id_dm_events method exists with correct signature."""
        # Check method exists
        method = getattr(
            DirectMessagesClient, "get_dm_conversations_id_dm_events", None
        )
        assert (
            method is not None
        ), f"Method get_dm_conversations_id_dm_events does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"get_dm_conversations_id_dm_events is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_dm_conversations_id_dm_events should have at least 'self' parameter"
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
            ), f"Required parameter '{required_param}' missing from get_dm_conversations_id_dm_events"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = [
            "max_results",
            "pagination_token",
            "event_types",
        ]
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_dm_conversations_id_dm_events_return_annotation(self):
        """Test that get_dm_conversations_id_dm_events has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_dm_conversations_id_dm_events")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_dm_conversations_id_dm_events should have return type annotation"


    def test_get_dm_conversations_id_dm_events_pagination_params(self):
        """Test that get_dm_conversations_id_dm_events has pagination parameters."""
        method = getattr(DirectMessagesClient, "get_dm_conversations_id_dm_events")
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
        ), f"Paginated method get_dm_conversations_id_dm_events should have pagination parameters"


    def test_get_events_by_id_exists(self):
        """Test that get_events_by_id method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "get_events_by_id", None)
        assert (
            method is not None
        ), f"Method get_events_by_id does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"get_events_by_id is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"get_events_by_id should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "event_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from get_events_by_id"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_get_events_by_id_return_annotation(self):
        """Test that get_events_by_id has proper return type annotation."""
        method = getattr(DirectMessagesClient, "get_events_by_id")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method get_events_by_id should have return type annotation"


    def test_delete_dm_events_exists(self):
        """Test that delete_dm_events method exists with correct signature."""
        # Check method exists
        method = getattr(DirectMessagesClient, "delete_dm_events", None)
        assert (
            method is not None
        ), f"Method delete_dm_events does not exist on DirectMessagesClient"
        # Check method is callable
        assert callable(method), f"delete_dm_events is not callable"
        # Check method signature
        sig = inspect.signature(method)
        params = list(sig.parameters.keys())
        # Should have 'self' as first parameter
        assert (
            len(params) >= 1
        ), f"delete_dm_events should have at least 'self' parameter"
        assert (
            params[0] == "self"
        ), f"First parameter should be 'self', got '{params[0]}'"
        # Check required parameters exist (excluding 'self')
        required_params = [
            "event_id",
        ]
        for required_param in required_params:
            assert (
                required_param in params
            ), f"Required parameter '{required_param}' missing from delete_dm_events"
        # Check optional parameters have defaults (excluding 'self')
        optional_params = []
        for optional_param in optional_params:
            if optional_param in params:
                param_obj = sig.parameters[optional_param]
                assert (
                    param_obj.default is not inspect.Parameter.empty
                ), f"Optional parameter '{optional_param}' should have a default value"


    def test_delete_dm_events_return_annotation(self):
        """Test that delete_dm_events has proper return type annotation."""
        method = getattr(DirectMessagesClient, "delete_dm_events")
        sig = inspect.signature(method)
        # Check return annotation exists
        assert (
            sig.return_annotation is not inspect.Signature.empty
        ), f"Method delete_dm_events should have return type annotation"


    def test_all_expected_methods_exist(self):
        """Test that all expected methods exist on the client."""
        expected_methods = [
            "get_dm_events_by_participant_id",
            "create_dm_by_participant_id",
            "create_dm_by_conversation_id",
            "create_dm_conversations",
            "get_events",
            "get_dm_conversations_id_dm_events",
            "get_events_by_id",
            "delete_dm_events",
        ]
        for expected_method in expected_methods:
            assert hasattr(
                DirectMessagesClient, expected_method
            ), f"Expected method '{expected_method}' not found on DirectMessagesClient"
            assert callable(
                getattr(DirectMessagesClient, expected_method)
            ), f"'{expected_method}' exists but is not callable"
