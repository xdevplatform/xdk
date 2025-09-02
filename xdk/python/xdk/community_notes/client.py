"""
community notes client for the X API.

This module provides a client for interacting with the community notes endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    DeleteResponse,
    SearchEligiblePostsResponse,
    SearchWrittenResponse,
    CreateRequest,
    CreateResponse,
)


class CommunityNotesClient:
    """Client for community notes operations"""


    def __init__(self, client: Client):
        self.client = client


    def delete(
        self,
        id: Any,
    ) -> DeleteResponse:
        """
        Delete a Community Note
        Deletes a community note.
        Args:
            id: The community note id to delete.
        Returns:
            DeleteResponse: Response data
        """
        url = self.client.base_url + "/2/notes/{id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.delete(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return DeleteResponse.model_validate(response_data)


    def search_eligible_posts(
        self,
        test_mode: bool,
        pagination_token: str = None,
        max_results: int = None,
    ) -> SearchEligiblePostsResponse:
        """
        Search for Posts Eligible for Community Notes
        Returns all the posts that are eligible for community notes.
        Args:
            test_mode: If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.
        Args:
            pagination_token: Pagination token to get next set of posts eligible for notes.
        Args:
            max_results: Max results to return.
        Returns:
            SearchEligiblePostsResponse: Response data
        """
        url = self.client.base_url + "/2/notes/search/posts_eligible_for_notes"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if test_mode is not None:
            params["test_mode"] = test_mode
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if max_results is not None:
            params["max_results"] = max_results
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.get(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return SearchEligiblePostsResponse.model_validate(response_data)


    def search_written(
        self,
        test_mode: bool,
        pagination_token: str = None,
        max_results: int = None,
    ) -> SearchWrittenResponse:
        """
        Search for Community Notes Written
        Returns all the community notes written by the user.
        Args:
            test_mode: If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.
        Args:
            pagination_token: Pagination token to get next set of posts eligible for notes.
        Args:
            max_results: Max results to return.
        Returns:
            SearchWrittenResponse: Response data
        """
        url = self.client.base_url + "/2/notes/search/notes_written"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if test_mode is not None:
            params["test_mode"] = test_mode
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if max_results is not None:
            params["max_results"] = max_results
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.get(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return SearchWrittenResponse.model_validate(response_data)


    def create(
        self,
        body: Optional[CreateRequest] = None,
    ) -> CreateResponse:
        """
        Create a Community Note
        Creates a community note endpoint for LLM use case.
            body: Request body
        Returns:
            CreateResponse: Response data
        """
        url = self.client.base_url + "/2/notes"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateResponse.model_validate(response_data)
