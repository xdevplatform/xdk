"""
Auto-generated pagination tests for {"class_name": "Users", "display_name": "users", "import_name": "users", "original": ["users"], "property_name": "users"} client.

This module contains tests that validate pagination functionality
using the Cursor class for methods that support pagination. Tests verify
proper handling of pagination tokens, page limits, and item iteration.

Generated automatically - do not edit manually.
"""

import pytest
from unittest.mock import Mock, patch
from xdk.users.client import UsersClient
from xdk import Client, Cursor, cursor, PaginationError


class TestUsersPagination:
    """Test pagination functionality for UsersClient."""


    def setup_class(self):
        """Set up test fixtures."""
        self.client = Client(base_url="https://api.example.com")
        self.users_client = getattr(self.client, "users")


    def test_get_list_memberships_cursor_creation(self):
        """Test that get_list_memberships can be used with Cursor."""
        method = getattr(self.users_client, "get_list_memberships")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_list_memberships should support pagination")


    def test_get_list_memberships_cursor_pages(self):
        """Test pagination with pages() for get_list_memberships."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_list_memberships")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_list_memberships_cursor_items(self):
        """Test pagination with items() for get_list_memberships."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_list_memberships")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_list_memberships_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_list_memberships."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_list_memberships")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_search_cursor_creation(self):
        """Test that search can be used with Cursor."""
        method = getattr(self.users_client, "search")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_query", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method search should support pagination")


    def test_search_cursor_pages(self):
        """Test pagination with pages() for search."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "search")
            test_cursor = cursor(method, "test_query", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_search_cursor_items(self):
        """Test pagination with items() for search."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "search")
            test_cursor = cursor(method, "test_query", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_search_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for search."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "search")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_query", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_query", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "next_token" in second_params
                ), "Second request should include next_token"
                assert (
                    second_params["next_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_blocking_cursor_creation(self):
        """Test that get_blocking can be used with Cursor."""
        method = getattr(self.users_client, "get_blocking")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_blocking should support pagination")


    def test_get_blocking_cursor_pages(self):
        """Test pagination with pages() for get_blocking."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_blocking")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_blocking_cursor_items(self):
        """Test pagination with items() for get_blocking."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_blocking")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_blocking_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_blocking."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_blocking")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_liked_posts_cursor_creation(self):
        """Test that get_liked_posts can be used with Cursor."""
        method = getattr(self.users_client, "get_liked_posts")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_liked_posts should support pagination")


    def test_get_liked_posts_cursor_pages(self):
        """Test pagination with pages() for get_liked_posts."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_liked_posts")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_liked_posts_cursor_items(self):
        """Test pagination with items() for get_liked_posts."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_liked_posts")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_liked_posts_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_liked_posts."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_liked_posts")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_bookmarks_cursor_creation(self):
        """Test that get_bookmarks can be used with Cursor."""
        method = getattr(self.users_client, "get_bookmarks")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_bookmarks should support pagination")


    def test_get_bookmarks_cursor_pages(self):
        """Test pagination with pages() for get_bookmarks."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_bookmarks")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_bookmarks_cursor_items(self):
        """Test pagination with items() for get_bookmarks."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_bookmarks")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_bookmarks_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_bookmarks."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_bookmarks")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_muting_cursor_creation(self):
        """Test that get_muting can be used with Cursor."""
        method = getattr(self.users_client, "get_muting")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_muting should support pagination")


    def test_get_muting_cursor_pages(self):
        """Test pagination with pages() for get_muting."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_muting")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_muting_cursor_items(self):
        """Test pagination with items() for get_muting."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_muting")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_muting_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_muting."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_muting")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_bookmark_folders_cursor_creation(self):
        """Test that get_bookmark_folders can be used with Cursor."""
        method = getattr(self.users_client, "get_bookmark_folders")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_bookmark_folders should support pagination")


    def test_get_bookmark_folders_cursor_pages(self):
        """Test pagination with pages() for get_bookmark_folders."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_bookmark_folders")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_bookmark_folders_cursor_items(self):
        """Test pagination with items() for get_bookmark_folders."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_bookmark_folders")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_bookmark_folders_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_bookmark_folders."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_bookmark_folders")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_following_cursor_creation(self):
        """Test that get_following can be used with Cursor."""
        method = getattr(self.users_client, "get_following")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_following should support pagination")


    def test_get_following_cursor_pages(self):
        """Test pagination with pages() for get_following."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_following")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_following_cursor_items(self):
        """Test pagination with items() for get_following."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_following")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_following_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_following."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_following")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_timeline_cursor_creation(self):
        """Test that get_timeline can be used with Cursor."""
        method = getattr(self.users_client, "get_timeline")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_timeline should support pagination")


    def test_get_timeline_cursor_pages(self):
        """Test pagination with pages() for get_timeline."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_timeline")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_timeline_cursor_items(self):
        """Test pagination with items() for get_timeline."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_timeline")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_timeline_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_timeline."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_timeline")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_reposts_of_me_cursor_creation(self):
        """Test that get_reposts_of_me can be used with Cursor."""
        method = getattr(self.users_client, "get_reposts_of_me")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_reposts_of_me should support pagination")


    def test_get_reposts_of_me_cursor_pages(self):
        """Test pagination with pages() for get_reposts_of_me."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_reposts_of_me")
            test_cursor = cursor(method, max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_reposts_of_me_cursor_items(self):
        """Test pagination with items() for get_reposts_of_me."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_reposts_of_me")
            test_cursor = cursor(method, max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_reposts_of_me_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_reposts_of_me."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_reposts_of_me")
            # Test with max_results parameter
            test_cursor = cursor(method, max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_mentions_cursor_creation(self):
        """Test that get_mentions can be used with Cursor."""
        method = getattr(self.users_client, "get_mentions")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_mentions should support pagination")


    def test_get_mentions_cursor_pages(self):
        """Test pagination with pages() for get_mentions."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_mentions")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_mentions_cursor_items(self):
        """Test pagination with items() for get_mentions."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_mentions")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_mentions_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_mentions."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_mentions")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_owned_lists_cursor_creation(self):
        """Test that get_owned_lists can be used with Cursor."""
        method = getattr(self.users_client, "get_owned_lists")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_owned_lists should support pagination")


    def test_get_owned_lists_cursor_pages(self):
        """Test pagination with pages() for get_owned_lists."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_owned_lists")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_owned_lists_cursor_items(self):
        """Test pagination with items() for get_owned_lists."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_owned_lists")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_owned_lists_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_owned_lists."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_owned_lists")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_posts_cursor_creation(self):
        """Test that get_posts can be used with Cursor."""
        method = getattr(self.users_client, "get_posts")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_posts should support pagination")


    def test_get_posts_cursor_pages(self):
        """Test pagination with pages() for get_posts."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_posts")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_posts_cursor_items(self):
        """Test pagination with items() for get_posts."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_posts")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_posts_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_posts."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_posts")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_followed_lists_cursor_creation(self):
        """Test that get_followed_lists can be used with Cursor."""
        method = getattr(self.users_client, "get_followed_lists")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_followed_lists should support pagination")


    def test_get_followed_lists_cursor_pages(self):
        """Test pagination with pages() for get_followed_lists."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_followed_lists")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_followed_lists_cursor_items(self):
        """Test pagination with items() for get_followed_lists."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_followed_lists")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_followed_lists_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_followed_lists."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_followed_lists")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_get_followers_cursor_creation(self):
        """Test that get_followers can be used with Cursor."""
        method = getattr(self.users_client, "get_followers")
        # Should be able to create cursor without error
        try:
            test_cursor = cursor(method, "test_id", max_results=10)
            assert test_cursor is not None
            assert isinstance(test_cursor, Cursor)
        except PaginationError:
            pytest.fail(f"Method get_followers should support pagination")


    def test_get_followers_cursor_pages(self):
        """Test pagination with pages() for get_followers."""
        with patch.object(self.client, "session") as mock_session:
            # Mock first page response
            first_page_response = Mock()
            first_page_response.status_code = 200
            first_page_response.json.return_value = {
                "data": [{"id": "1", "name": "Item 1"}, {"id": "2", "name": "Item 2"}],
                "meta": {"next_token": "next_page_token", "result_count": 2},
            }
            first_page_response.raise_for_status.return_value = None
            # Mock second page response (no next token = end of pagination)
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [{"id": "3", "name": "Item 3"}],
                "meta": {"result_count": 1},
            }
            second_page_response.raise_for_status.return_value = None
            # Return different responses for consecutive calls
            mock_session.get.side_effect = [first_page_response, second_page_response]
            # Test pagination
            method = getattr(self.users_client, "get_followers")
            test_cursor = cursor(method, "test_id", max_results=2)
            pages = list(test_cursor.pages(2))  # Limit to 2 pages
            assert len(pages) == 2, f"Should get 2 pages, got {len(pages)}"
            # Verify first page
            first_page = pages[0]
            assert hasattr(first_page, "data")
            first_data = getattr(first_page, "data")
            assert len(first_data) == 2, "First page should have 2 items"
            # Verify second page
            second_page = pages[1]
            assert hasattr(second_page, "data")
            second_data = getattr(second_page, "data")
            assert len(second_data) == 1, "Second page should have 1 item"


    def test_get_followers_cursor_items(self):
        """Test pagination with items() for get_followers."""
        with patch.object(self.client, "session") as mock_session:
            # Mock response with paginated data
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "data": [
                    {"id": "1", "name": "Item 1"},
                    {"id": "2", "name": "Item 2"},
                    {"id": "3", "name": "Item 3"},
                ],
                "meta": {
                    "result_count": 3
                    # No next_token = single page
                },
            }
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            # Test item iteration
            method = getattr(self.users_client, "get_followers")
            test_cursor = cursor(method, "test_id", max_results=10)
            items = list(test_cursor.items(5))  # Limit to 5 items
            assert len(items) == 3, f"Should get 3 items, got {len(items)}"
            # Verify items have expected structure
            for item in items:
                assert "id" in item or hasattr(
                    item, "id"
                ), "Items should have 'id' field"


    def test_get_followers_pagination_parameters(self):
        """Test that pagination parameters are handled correctly for get_followers."""
        with patch.object(self.client, "session") as mock_session:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            mock_response.raise_for_status.return_value = None
            mock_session.get.return_value = mock_response
            method = getattr(self.users_client, "get_followers")
            # Test with max_results parameter
            test_cursor = cursor(method, "test_id", max_results=5)
            list(test_cursor.pages(1))  # Trigger one request
            # Verify max_results was passed in request
            call_args = mock_session.get.call_args
            if call_args and "params" in call_args[1]:
                params = call_args[1]["params"]
                assert (
                    "max_results" in params
                ), "max_results should be in request parameters"
            # Test with pagination token (simulate second page request)
            mock_session.reset_mock()
            mock_response_with_token = Mock()
            mock_response_with_token.status_code = 200
            mock_response_with_token.json.return_value = {
                "data": [{"id": "1"}],
                "meta": {"next_token": "next_token_value", "result_count": 1},
            }
            mock_response_with_token.raise_for_status.return_value = None
            second_page_response = Mock()
            second_page_response.status_code = 200
            second_page_response.json.return_value = {
                "data": [],
                "meta": {"result_count": 0},
            }
            second_page_response.raise_for_status.return_value = None
            mock_session.get.side_effect = [
                mock_response_with_token,
                second_page_response,
            ]
            test_cursor = cursor(method, "test_id", max_results=1)
            pages = list(test_cursor.pages(2))
            # Should have made 2 requests
            assert (
                mock_session.get.call_count == 2
            ), "Should make 2 requests for 2 pages"
            # Second request should include pagination token
            second_call_args = mock_session.get.call_args_list[1]
            if (
                second_call_args
                and len(second_call_args) > 1
                and "params" in second_call_args[1]
            ):
                second_params = second_call_args[1]["params"]
                assert (
                    "pagination_token" in second_params
                ), "Second request should include pagination_token"
                assert (
                    second_params["pagination_token"] == "next_token_value"
                ), "Pagination token should be passed correctly"


    def test_pagination_edge_cases(self):
        """Test pagination edge cases."""
        with patch.object(self.client, "session") as mock_session:
            # Test empty response
            empty_response = Mock()
            empty_response.status_code = 200
            empty_response.json.return_value = {"data": [], "meta": {"result_count": 0}}
            empty_response.raise_for_status.return_value = None
            mock_session.get.return_value = empty_response
            # Pick first paginatable method for testing
            method = getattr(self.users_client, "get_list_memberships")
            test_cursor = cursor(method, "test_id", max_results=10)
            # Should handle empty responses gracefully
            pages = list(test_cursor.pages(1))
            assert len(pages) == 1, "Should get one page even if empty"
            items = list(test_cursor.items(10))
            assert len(items) == 0, "Should get no items from empty response"


    def test_non_paginatable_method_raises_error(self):
        """Test that non-paginatable methods raise PaginationError."""
        # Create a mock method that doesn't support pagination
        def non_paginatable_method(id: str) -> dict:
            return {"id": id}
        with pytest.raises(PaginationError):
            cursor(non_paginatable_method)


        def non_paginatable_method(id: str) -> dict:
            return {"id": id}

        with pytest.raises(PaginationError):
            cursor(non_paginatable_method)


    def test_cursor_class_functionality(self):
        """Test basic Cursor class functionality."""
        # Test that Cursor can be imported and instantiated
        from xdk.paginator import Cursor
        assert Cursor is not None
        # Test cursor factory function
        from xdk.paginator import cursor as cursor_factory
        assert cursor_factory is not None
