"""
Auto-generated contract tests for Stream client.

This module contains tests that validate the request/response contracts
of the Stream client against the OpenAPI specification.

Generated automatically - do not edit manually.
"""

import pytest
import json
from unittest.mock import Mock, patch
from xdk.stream.client import StreamClient
from xdk import Client


class TestStreamContracts:
    """Test the API contracts of StreamClient."""

    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.stream_client = getattr(self.client, "stream")

    def test_stream_likes_firehose_request_structure(self):
        """Test streamLikesFirehose request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_likes_firehose")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/likes/firehose/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamLikesFirehose: {e}")

    def test_stream_likes_firehose_required_parameters(self):
        """Test that streamLikesFirehose requires necessary parameters."""
        method = getattr(self.stream_client, "stream_likes_firehose")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_likes_firehose_response_structure(self):
        """Test streamLikesFirehose response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_likes_firehose")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_pt_request_structure(self):
        """Test streamPostsFirehosePt request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_firehose_pt")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/pt"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehosePt: {e}")

    def test_stream_posts_firehose_pt_required_parameters(self):
        """Test that streamPostsFirehosePt requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_firehose_pt")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_pt_response_structure(self):
        """Test streamPostsFirehosePt response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_firehose_pt")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_en_request_structure(self):
        """Test streamPostsFirehoseEn request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_firehose_en")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/en"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehoseEn: {e}")

    def test_stream_posts_firehose_en_required_parameters(self):
        """Test that streamPostsFirehoseEn requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_firehose_en")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_en_response_structure(self):
        """Test streamPostsFirehoseEn response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_firehose_en")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_rule_counts_request_structure(self):
        """Test getRuleCounts request structure."""

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
                method = getattr(self.stream_client, "get_rule_counts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream/rules/counts"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getRuleCounts: {e}")

    def test_get_rule_counts_required_parameters(self):
        """Test that getRuleCounts requires necessary parameters."""
        method = getattr(self.stream_client, "get_rule_counts")

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

    def test_get_rule_counts_response_structure(self):
        """Test getRuleCounts response structure validation."""

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
            method = getattr(self.stream_client, "get_rule_counts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_ja_request_structure(self):
        """Test streamPostsFirehoseJa request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_firehose_ja")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/ja"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehoseJa: {e}")

    def test_stream_posts_firehose_ja_required_parameters(self):
        """Test that streamPostsFirehoseJa requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_firehose_ja")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_ja_response_structure(self):
        """Test streamPostsFirehoseJa response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_firehose_ja")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_request_structure(self):
        """Test streamPosts request structure."""

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
                method = getattr(self.stream_client, "stream_posts")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPosts: {e}")

    def test_stream_posts_required_parameters(self):
        """Test that streamPosts requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts")

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

    def test_stream_posts_response_structure(self):
        """Test streamPosts response structure validation."""

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
            method = getattr(self.stream_client, "stream_posts")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_get_rules_request_structure(self):
        """Test getRules request structure."""

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
                method = getattr(self.stream_client, "get_rules")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream/rules"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for getRules: {e}")

    def test_get_rules_required_parameters(self):
        """Test that getRules requires necessary parameters."""
        method = getattr(self.stream_client, "get_rules")

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

    def test_get_rules_response_structure(self):
        """Test getRules response structure validation."""

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
            method = getattr(self.stream_client, "get_rules")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_update_rules_request_structure(self):
        """Test updateRules request structure."""

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
                method = getattr(self.stream_client, "update_rules")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.post.assert_called_once()

                # Verify request structure
                call_args = mock_session.post.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/search/stream/rules"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for updateRules: {e}")

    def test_update_rules_required_parameters(self):
        """Test that updateRules requires necessary parameters."""
        method = getattr(self.stream_client, "update_rules")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_update_rules_response_structure(self):
        """Test updateRules response structure validation."""

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
            method = getattr(self.stream_client, "update_rules")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_compliance_request_structure(self):
        """Test streamPostsCompliance request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_compliance")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/compliance/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsCompliance: {e}")

    def test_stream_posts_compliance_required_parameters(self):
        """Test that streamPostsCompliance requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_compliance")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_compliance_response_structure(self):
        """Test streamPostsCompliance response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_compliance")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_likes_compliance_request_structure(self):
        """Test streamLikesCompliance request structure."""

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
                method = getattr(self.stream_client, "stream_likes_compliance")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/likes/compliance/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamLikesCompliance: {e}")

    def test_stream_likes_compliance_required_parameters(self):
        """Test that streamLikesCompliance requires necessary parameters."""
        method = getattr(self.stream_client, "stream_likes_compliance")

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

    def test_stream_likes_compliance_response_structure(self):
        """Test streamLikesCompliance response structure validation."""

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
            method = getattr(self.stream_client, "stream_likes_compliance")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_likes_sample10_request_structure(self):
        """Test streamLikesSample10 request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_likes_sample10")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/likes/sample10/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamLikesSample10: {e}")

    def test_stream_likes_sample10_required_parameters(self):
        """Test that streamLikesSample10 requires necessary parameters."""
        method = getattr(self.stream_client, "stream_likes_sample10")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_likes_sample10_response_structure(self):
        """Test streamLikesSample10 response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_likes_sample10")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_labels_compliance_request_structure(self):
        """Test streamLabelsCompliance request structure."""

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
                method = getattr(self.stream_client, "stream_labels_compliance")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/label/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamLabelsCompliance: {e}")

    def test_stream_labels_compliance_required_parameters(self):
        """Test that streamLabelsCompliance requires necessary parameters."""
        method = getattr(self.stream_client, "stream_labels_compliance")

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

    def test_stream_labels_compliance_response_structure(self):
        """Test streamLabelsCompliance response structure validation."""

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
            method = getattr(self.stream_client, "stream_labels_compliance")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_sample_request_structure(self):
        """Test streamPostsSample request structure."""

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
                method = getattr(self.stream_client, "stream_posts_sample")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/sample/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsSample: {e}")

    def test_stream_posts_sample_required_parameters(self):
        """Test that streamPostsSample requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_sample")

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

    def test_stream_posts_sample_response_structure(self):
        """Test streamPostsSample response structure validation."""

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
            method = getattr(self.stream_client, "stream_posts_sample")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_users_compliance_request_structure(self):
        """Test streamUsersCompliance request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_users_compliance")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/users/compliance/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamUsersCompliance: {e}")

    def test_stream_users_compliance_required_parameters(self):
        """Test that streamUsersCompliance requires necessary parameters."""
        method = getattr(self.stream_client, "stream_users_compliance")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_users_compliance_response_structure(self):
        """Test streamUsersCompliance response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_users_compliance")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_request_structure(self):
        """Test streamPostsFirehose request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_firehose")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehose: {e}")

    def test_stream_posts_firehose_required_parameters(self):
        """Test that streamPostsFirehose requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_firehose")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_response_structure(self):
        """Test streamPostsFirehose response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_firehose")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_firehose_ko_request_structure(self):
        """Test streamPostsFirehoseKo request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_firehose_ko")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/firehose/stream/lang/ko"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsFirehoseKo: {e}")

    def test_stream_posts_firehose_ko_required_parameters(self):
        """Test that streamPostsFirehoseKo requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_firehose_ko")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_firehose_ko_response_structure(self):
        """Test streamPostsFirehoseKo response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_firehose_ko")
            result = method(**kwargs)

            # Verify response object has expected attributes

            # Optional field - just check it doesn't cause errors if accessed
            try:
                getattr(result, "data", None)
            except Exception as e:
                pytest.fail(
                    f"Accessing optional field 'data' should not cause errors: {e}"
                )

    def test_stream_posts_sample10_request_structure(self):
        """Test streamPostsSample10 request structure."""

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

            kwargs["partition"] = 42

            # Add request body if required

            # Call the method
            try:
                method = getattr(self.stream_client, "stream_posts_sample10")
                result = method(**kwargs)

                # Verify the request was made
                mock_session.get.assert_called_once()

                # Verify request structure
                call_args = mock_session.get.call_args

                # Check URL structure
                called_url = (
                    call_args[0][0] if call_args[0] else call_args[1].get("url", "")
                )
                expected_path = "/2/tweets/sample10/stream"
                assert expected_path.replace("{", "").replace(
                    "}", ""
                ) in called_url or any(
                    param in called_url for param in ["test_", "42"]
                ), f"URL should contain path template elements: {called_url}"

                # Verify response structure
                assert result is not None, "Method should return a result"

            except Exception as e:
                pytest.fail(f"Contract test failed for streamPostsSample10: {e}")

    def test_stream_posts_sample10_required_parameters(self):
        """Test that streamPostsSample10 requires necessary parameters."""
        method = getattr(self.stream_client, "stream_posts_sample10")

        # Test with missing required parameters should fail

        with pytest.raises((TypeError, ValueError)):
            # Call without required parameters
            method()

    def test_stream_posts_sample10_response_structure(self):
        """Test streamPostsSample10 response structure validation."""

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

            kwargs["partition"] = 1

            # Add request body if required

            # Call method and verify response structure
            method = getattr(self.stream_client, "stream_posts_sample10")
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

            method = getattr(self.stream_client, "stream_likes_firehose")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_firehose_pt")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_firehose_en")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "get_rule_counts")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_firehose_ja")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "get_rules")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "update_rules")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                kwargs["body"] = {"type": "test", "name": "test_name"}

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_compliance")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_likes_compliance")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_likes_sample10")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_labels_compliance")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_sample")

            with pytest.raises(Exception):
                kwargs = {}

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_users_compliance")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_firehose")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_firehose_ko")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)

            method = getattr(self.stream_client, "stream_posts_sample10")

            with pytest.raises(Exception):
                kwargs = {}

                kwargs["partition"] = 1

                # Add request body if required

                method(**kwargs)
