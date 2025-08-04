"""
Cursor-based pagination utilities for the X API SDK.

This module provides a Cursor for elegant pagination support.
"""

from typing import (
    Iterator,
    Any,
    Optional,
    Callable,
    TypeVar,
    Generic,
    overload,
    Protocol,
    runtime_checkable,
)
import inspect

# Type variable for response type
ResponseType = TypeVar("ResponseType")


@runtime_checkable
class PaginatableMethod(Protocol[ResponseType]):
    """
    Protocol for methods that support pagination.

    A method is considered paginatable if it accepts pagination_token
    and/or max_results parameters.
    """


    def __call__(
        self,
        *args,
        pagination_token: Optional[str] = None,
        max_results: Optional[int] = None,
        **kwargs,
    ) -> ResponseType: ...


class PaginationError(TypeError):
    """Raised when a non-paginatable method is passed to Cursor."""

    pass


def _validate_paginatable_method(method: Callable) -> None:
    """
    Validate that a method supports pagination parameters.
    Raises PaginationError if the method doesn't support pagination.
    """
    sig = inspect.signature(method)
    params = sig.parameters
    # Check if method has pagination_token, next_token, or max_results parameters
    has_pagination_token = "pagination_token" in params
    has_next_token = "next_token" in params
    has_max_results = "max_results" in params
    if not (has_pagination_token or has_next_token or has_max_results):
        raise PaginationError(
            f"Method '{method.__name__}' does not support pagination. "
            f"Paginatable methods must accept 'pagination_token', 'next_token', and/or 'max_results' parameters. "
            f"Available parameters: {list(params.keys())}"
        )


class Cursor(Generic[ResponseType]):
    """
    A cursor for handling pagination in API calls.

    This class wraps any API method and provides elegant pagination
    through .items() and .pages() methods. The cursor preserves the
    return type of the wrapped method for proper type hints.

    Example usage:
        # For methods requiring arguments
        cursor = Cursor(client.users.get_users_blocking, "user_id", max_results=100)
        for user in cursor.items(250):  # user is properly typed
            print(user.name)

        # For methods with query parameters
        cursor = Cursor(client.tweets.search_posts_recent, "python", max_results=50)
        for page in cursor.pages(5):  # page is SearchResponse type
            print(f"Got {len(page.data)} tweets")
    """


    def __init__(
        self, method: PaginatableMethod[ResponseType], *args: Any, **kwargs: Any
    ):
        """
        Initialize the cursor.
        Args:
            method: The API method to call for each page (must support pagination)
            *args: Positional arguments to pass to the API method
            **kwargs: Keyword arguments to pass to the API method (excluding pagination params)
        Raises:
            PaginationError: If the method doesn't support pagination parameters
        """
        # Validate method supports pagination at runtime
        _validate_paginatable_method(method)
        self.method = method
        self.args = args
        self.params = kwargs.copy()


    def items(self, limit: Optional[int] = None) -> Iterator[Any]:
        """
        Iterate over individual items from paginated responses.
        Args:
            limit: Maximum number of items to return (None for unlimited)
        Yields:
            Individual items from the API responses
        """
        return _ItemIterator(self, limit)


    def pages(self, limit: Optional[int] = None) -> Iterator[ResponseType]:
        """
        Iterate over pages of responses.
        Args:
            limit: Maximum number of pages to return (None for unlimited)
        Yields:
            Page responses from the API (same type as the wrapped method returns)
        """
        return _PageIterator(self, limit)


# Factory function for better type inference


@overload


def cursor(
    method: PaginatableMethod[ResponseType], *args: Any, **kwargs: Any
) -> Cursor[ResponseType]: ...


def cursor(
    method: PaginatableMethod[ResponseType], *args: Any, **kwargs: Any
) -> Cursor[ResponseType]:
    """
    Create a cursor with proper type inference and validation.
    This factory function helps with type inference so you get proper
    type hints for the response type, and validates that the method
    supports pagination at both static analysis and runtime.
    Args:
        method: The API method to wrap (must support pagination)
        *args: Positional arguments to pass to the method
        **kwargs: Keyword arguments to pass to the method
    Returns:
        A properly typed Cursor instance
    Raises:
        PaginationError: If the method doesn't support pagination parameters
    Example:
        # Type is inferred as Cursor[GetUsersResponse]
        users_cursor = cursor(client.users.get_users_blocking, "user_id", max_results=100)
        # page is typed as GetUsersResponse
        for page in users_cursor.pages(5):
            print(len(page.data))
        # For search methods
        search_cursor = cursor(client.tweets.search_posts_recent, "python", max_results=50)
        for tweet in search_cursor.items(100):
            print(tweet.text)
    """
    return Cursor(method, *args, **kwargs)


class _PageIterator(Generic[ResponseType], Iterator[ResponseType]):
    """Internal iterator for pages."""


    def __init__(self, cursor: Cursor[ResponseType], limit: Optional[int]):
        self.cursor = cursor
        self.limit = limit
        self.count = 0
        self.exhausted = False
        self._next_token: Optional[str] = None


    def __iter__(self) -> Iterator[ResponseType]:
        return self


    def __next__(self) -> ResponseType:
        if self.exhausted or (self.limit is not None and self.count >= self.limit):
            raise StopIteration
        # Prepare params for this request
        params = self.cursor.params.copy()
        if self._next_token:
            # Try different pagination parameter names
            if self._supports_pagination_token():
                params["pagination_token"] = self._next_token
            elif self._supports_next_token():
                params["next_token"] = self._next_token
        # Make the API call with both positional and keyword arguments
        response = self.cursor.method(*self.cursor.args, **params)
        # Extract next token
        self._next_token = self._extract_next_token(response)
        # Check if we're done
        if not self._next_token:
            self.exhausted = True
        self.count += 1
        return response


    def _supports_pagination_token(self) -> bool:
        """Check if the method supports pagination_token parameter."""
        sig = inspect.signature(self.cursor.method)
        return "pagination_token" in sig.parameters


    def _supports_next_token(self) -> bool:
        """Check if the method supports next_token parameter."""
        sig = inspect.signature(self.cursor.method)
        return "next_token" in sig.parameters


    def _extract_next_token(self, response: ResponseType) -> Optional[str]:
        """Extract the next_token from the response."""
        # Try common patterns for next_token
        if hasattr(response, "meta") and response.meta:
            if hasattr(response.meta, "next_token"):
                return response.meta.next_token
        return None


class _ItemIterator(Iterator[Any]):
    """Internal iterator for individual items."""


    def __init__(self, cursor: Cursor, limit: Optional[int]):
        self.page_iterator = _PageIterator(cursor, None)  # No page limit for items
        self.limit = limit
        self.count = 0
        self._current_items = []
        self._current_index = 0


    def __iter__(self) -> Iterator[Any]:
        return self


    def __next__(self) -> Any:
        if self.limit is not None and self.count >= self.limit:
            raise StopIteration
        # If we've exhausted current items, get next page
        while self._current_index >= len(self._current_items):
            try:
                page = next(self.page_iterator)
                # Try common patterns for data arrays
                items = self._extract_items(page)
                self._current_items = items or []
                self._current_index = 0
                # If the page has no items, continue to next page
                if not self._current_items:
                    continue
            except StopIteration:
                raise StopIteration
        # Return current item and advance
        item = self._current_items[self._current_index]
        self._current_index += 1
        self.count += 1
        return item


    def _extract_items(self, response: Any) -> Optional[list]:
        """Extract items from response, trying common field names."""
        # Try common field names for data arrays
        for field_name in ["data", "results", "items"]:
            if hasattr(response, field_name):
                items = getattr(response, field_name)
                if isinstance(items, list):
                    return items
        return None
