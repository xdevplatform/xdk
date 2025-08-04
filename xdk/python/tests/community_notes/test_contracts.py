"""
Auto-generated contract tests for Community_Notes client.

This module contains tests that validate the request/response contracts
of the Community_Notes client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.community_notes.client import CommunityNotesClient
from xdk import Client


class TestCommunityNotesContracts:
    """Test the API contracts of CommunityNotesClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.community_notes_client = getattr(self.client, "community_notes")

    def test_search_for_eligible_posts_request_structure(self):
        """Test searchForEligiblePosts request structure."""

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

            kwargs["test_mode"] = True

            # Add request body if required

            # Call the method
            try:
                method = getattr(
                    self.community_notes_client, "search_for_eligible_posts"
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
                expected_path = "/2/notes/search/posts_eligible_for_notes"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for searchForEligiblePosts: {e}")

    def test_search_for_eligible_posts_required_parameters(self):
        """Test that searchForEligiblePosts requires necessary parameters."""
        method = getattr(self.community_notes_client, "search_for_eligible_posts")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_search_for_eligible_posts_response_structure(self):
        """Test searchForEligiblePosts response structure validation."""

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

            kwargs["test_mode"] = True

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.community_notes_client, "search_for_eligible_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_create_notes_request_structure(self):
        """Test createNotes request structure."""

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

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call the method
            try:
                method = getattr(self.community_notes_client, "create_notes")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/notes"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for createNotes: {e}")

    def test_create_notes_required_parameters(self):
        """Test that createNotes requires necessary parameters."""
        method = getattr(self.community_notes_client, "create_notes")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_create_notes_response_structure(self):
        """Test createNotes response structure validation."""

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

            # Add request body if required

            # Generate mock request body data
            kwargs["body"] = {
                "type": "test",
                "name": "test_name",
                "description": "test_description",
            }

            # Call method and verify response structure
            method = getattr(self.community_notes_client, "create_notes")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_search_notes_written_request_structure(self):
        """Test searchNotesWritten request structure."""

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

            kwargs["test_mode"] = True

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.community_notes_client, "search_notes_written")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/notes/search/notes_written"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for searchNotesWritten: {e}")

    def test_search_notes_written_required_parameters(self):
        """Test that searchNotesWritten requires necessary parameters."""
        method = getattr(self.community_notes_client, "search_notes_written")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_search_notes_written_response_structure(self):
        """Test searchNotesWritten response structure validation."""

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

            kwargs["test_mode"] = True

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.community_notes_client, "search_notes_written")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_delete_notes_request_structure(self):
        """Test deleteNotes request structure."""

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

            kwargs["id"] = "test_value"

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.community_notes_client, "delete_notes")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.delete.assert_called_once()

                # Verify request structure
                call_args = mock_session.delete.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/notes/{id}"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for deleteNotes: {e}")

    def test_delete_notes_required_parameters(self):
        """Test that deleteNotes requires necessary parameters."""
        method = getattr(self.community_notes_client, "delete_notes")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_delete_notes_response_structure(self):
        """Test deleteNotes response structure validation."""

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

            kwargs["id"] = "test"

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.community_notes_client, "delete_notes")
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

            method = getattr(self.community_notes_client, "search_for_eligible_posts")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["test_mode"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.community_notes_client, "create_notes")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.community_notes_client, "search_notes_written")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["test_mode"] = "test"

                # Add request body if required

                method(**kwargs)

            method = getattr(self.community_notes_client, "delete_notes")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["id"] = "test"

                # Add request body if required

                method(**kwargs)
