"""
Auto-generated contract tests for Direct_Messages client.

This module contains tests that validate the request/response contracts
of the Direct_Messages client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.direct_messages.client import DirectMessagesClient
from xdk import Client


class TestDirectMessagesContracts:
    """Test the API contracts of DirectMessagesClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.direct_messages_client = getattr(self.client, "direct_messages")

    def test_get_dm_conversations_id_dm_events_request_structure(self):
        """Test getDmConversationsIdDmEvents request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.direct_messages_client, "get_dm_conversations_id_dm_events"
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_conversations/{id}/dm_events"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(
                    f"Contract test failed for getDmConversationsIdDmEvents: {e}"
                )

    def test_get_dm_conversations_id_dm_events_required_parameters(self):
        """Test that getDmConversationsIdDmEvents requires necessary parameters."""
        method = getattr(
            self.direct_messages_client, "get_dm_conversations_id_dm_events"
        )

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_dm_conversations_id_dm_events_response_structure(self):
        """Test getDmConversationsIdDmEvents response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.direct_messages_client, "get_dm_conversations_id_dm_events"
            )
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_dm_events_by_id_request_structure(self):
        """Test getDmEventsById request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["event_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.direct_messages_client, "get_dm_events_by_id")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_events/{event_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getDmEventsById: {e}")

    def test_get_dm_events_by_id_required_parameters(self):
        """Test that getDmEventsById requires necessary parameters."""
        method = getattr(self.direct_messages_client, "get_dm_events_by_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_dm_events_by_id_response_structure(self):
        """Test getDmEventsById response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["event_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.direct_messages_client, "get_dm_events_by_id")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_delete_dm_events_request_structure(self):
        """Test deleteDmEvents request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.delete.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["event_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.direct_messages_client, "delete_dm_events")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_events/{event_id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for deleteDmEvents: {e}")

    def test_delete_dm_events_required_parameters(self):
        """Test that deleteDmEvents requires necessary parameters."""
        method = getattr(self.direct_messages_client, "delete_dm_events")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_delete_dm_events_response_structure(self):
        """Test deleteDmEvents response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.delete.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["event_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.direct_messages_client, "delete_dm_events")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_dm_events_request_structure(self):
        """Test getDmEvents request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.direct_messages_client, "get_dm_events")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_events"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getDmEvents: {e}")

    def test_get_dm_events_required_parameters(self):
        """Test that getDmEvents requires necessary parameters."""
        method = getattr(self.direct_messages_client, "get_dm_events")

        # Test with missing required parameters should fail

        # No required parameters, method should be callable without args
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            try:
                method()
            except Exception as e:
                pytest.fail(f"Method with no required params should be callable: {e}")

    def test_get_dm_events_response_structure(self):
        """Test getDmEvents response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.direct_messages_client, "get_dm_events")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_create_dm_by_conversation_id_request_structure(self):
        """Test createDmByConversationId request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["dm_conversation_id"] = "test_dm_conversation_id"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(
                    self.direct_messages_client, "create_dm_by_conversation_id"
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_conversations/{dm_conversation_id}/messages"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for createDmByConversationId: {e}")

    def test_create_dm_by_conversation_id_required_parameters(self):
        """Test that createDmByConversationId requires necessary parameters."""
        method = getattr(self.direct_messages_client, "create_dm_by_conversation_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_create_dm_by_conversation_id_response_structure(self):
        """Test createDmByConversationId response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["dm_conversation_id"] = "test_value"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(
                self.direct_messages_client, "create_dm_by_conversation_id"
            )
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_dm_events_by_participant_id_request_structure(self):
        """Test getDmEventsByParticipantId request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["participant_id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.direct_messages_client, "get_dm_events_by_participant_id"
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_conversations/with/{participant_id}/dm_events"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getDmEventsByParticipantId: {e}")

    def test_get_dm_events_by_participant_id_required_parameters(self):
        """Test that getDmEventsByParticipantId requires necessary parameters."""
        method = getattr(self.direct_messages_client, "get_dm_events_by_participant_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_get_dm_events_by_participant_id_response_structure(self):
        """Test getDmEventsByParticipantId response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["participant_id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(
                self.direct_messages_client, "get_dm_events_by_participant_id"
            )
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_create_dm_conversations_request_structure(self):
        """Test createDmConversations request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 201
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.direct_messages_client, "create_dm_conversations")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_conversations"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for createDmConversations: {e}")

    def test_create_dm_conversations_required_parameters(self):
        """Test that createDmConversations requires necessary parameters."""
        method = getattr(self.direct_messages_client, "create_dm_conversations")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_create_dm_conversations_response_structure(self):
        """Test createDmConversations response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 201
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.direct_messages_client, "create_dm_conversations")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_create_dm_by_participant_id_request_structure(self):
        """Test createDmByParticipantId request structure."""

        # Mock the session to capture request details
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": None,
            }
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare test parameters
            kwargs = {}

            # Add required parameters

            kwargs["participant_id"] = "test_value"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(
                    self.direct_messages_client, "create_dm_by_participant_id"
                )
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/dm_conversations/with/{participant_id}/messages"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for createDmByParticipantId: {e}")

    def test_create_dm_by_participant_id_required_parameters(self):
        """Test that createDmByParticipantId requires necessary parameters."""
        method = getattr(self.direct_messages_client, "create_dm_by_participant_id")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_create_dm_by_participant_id_response_structure(self):
        """Test createDmByParticipantId response structure validation."""

        with patch.object(self.client, "session") as mock_session:
            # Create mock response with expected structure
            mock_response_data = {
                "data": None,
            }

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = mock_response_data
            mock_response.raise_for_status.return_value = None
            mock_session.post.return_value = mock_response

            # Prepare minimal valid parameters
            kwargs = {}

            kwargs["participant_id"] = "test"

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.direct_messages_client, "create_dm_by_participant_id")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_error_responses(self):
        """Test that error responses are handled correctly."""

        with patch.object(self.client, "session") as mock_session:
            # Test 404 response
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = Exception("Not Found")
            mock_session.get.return_value = mock_response

            # Pick first available method for testing

            method = getattr(
                self.direct_messages_client, "get_dm_conversations_id_dm_events"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.direct_messages_client, "get_dm_events_by_id")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["event_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.direct_messages_client, "delete_dm_events")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["event_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.direct_messages_client, "get_dm_events")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(
                self.direct_messages_client, "create_dm_by_conversation_id"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["dm_conversation_id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(
                self.direct_messages_client, "get_dm_events_by_participant_id"
            )

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["participant_id"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.direct_messages_client, "create_dm_conversations")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.direct_messages_client, "create_dm_by_participant_id")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["participant_id"] = "test"

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)
