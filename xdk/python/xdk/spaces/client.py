"""
spaces client for the X API.

This module provides a client for interacting with the spaces endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    GetPostsResponse,
    GetBuyersResponse,
    GetByIdsResponse,
    GetByIdResponse,
    SearchResponse,
    GetByCreatorIdsResponse,
)


class SpacesClient:
    """Client for spaces operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_posts(
        self,
        id: str,
        max_results: int = None,
    ) -> GetPostsResponse:
        """
        Get Space Posts
        Retrieves a list of Posts shared in a specific Space by its ID.
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            max_results: The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
        Returns:
            GetPostsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/tweets"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
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
        return GetPostsResponse.model_validate(response_data)


    def get_buyers(
        self,
        id: str,
        pagination_token: Any = None,
        max_results: int = None,
    ) -> GetBuyersResponse:
        """
        Get Space ticket buyers
        Retrieves a list of Users who purchased tickets to a specific Space by its ID.
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            max_results: The maximum number of results.
        Returns:
            GetBuyersResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/buyers"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if max_results is not None:
            params["max_results"] = max_results
        url = url.replace("{id}", str(id))
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
        return GetBuyersResponse.model_validate(response_data)


    def get_by_ids(
        self,
        ids: List,
    ) -> GetByIdsResponse:
        """
        Get Spaces by IDs
        Retrieves details of multiple Spaces by their IDs.
        Args:
            ids: The list of Space IDs to return.
        Returns:
            GetByIdsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if ids is not None:
            params["ids"] = ",".join(str(item) for item in ids)
        headers = {}
        # Make the request
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
        return GetByIdsResponse.model_validate(response_data)


    def get_by_id(
        self,
        id: str,
    ) -> GetByIdResponse:
        """
        Get space by ID
        Retrieves details of a specific space by its ID.
        Args:
            id: The ID of the Space to be retrieved.
        Returns:
            GetByIdResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
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
        return GetByIdResponse.model_validate(response_data)


    def search(
        self,
        query: str,
        state: str = None,
        max_results: int = None,
    ) -> SearchResponse:
        """
        Search Spaces
        Retrieves a list of Spaces matching the specified search query.
        Args:
            query: The search query.
        Args:
            state: The state of Spaces to search for.
        Args:
            max_results: The number of results to return.
        Returns:
            SearchResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/search"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if query is not None:
            params["query"] = query
        if state is not None:
            params["state"] = state
        if max_results is not None:
            params["max_results"] = max_results
        headers = {}
        # Make the request
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
        return SearchResponse.model_validate(response_data)


    def get_by_creator_ids(
        self,
        user_ids: List,
    ) -> GetByCreatorIdsResponse:
        """
        Get Spaces by creator IDs
        Retrieves details of Spaces created by specified User IDs.
        Args:
            user_ids: The IDs of Users to search through.
        Returns:
            GetByCreatorIdsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/by/creator_ids"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if user_ids is not None:
            params["user_ids"] = ",".join(str(item) for item in user_ids)
        headers = {}
        # Make the request
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
        return GetByCreatorIdsResponse.model_validate(response_data)
