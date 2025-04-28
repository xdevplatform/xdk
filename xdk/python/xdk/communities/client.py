"""
Communities client for the X API.

This module provides a client for interacting with the Communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from ..client import Client
from .models import communities_search_response, community_id_get_response


class CommunitiesClient:
    """Client for Communities operations"""


    def __init__(self, client: Client):
        self.client = client


    def communities_search(
        self,
        query: str,
        max_results: int = None,
        next_token: str = None,
        pagination_token: str = None,
        community_fields: List = None,
    ) -> communities_search_response:
        """
        Search Communities
        Returns Communities that match search query
        Args:
            query: Query to search communities.
        Args:
            max_results: The maximum number of search results to be returned by a request.
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            community_fields: A comma separated list of Community fields to display.
        Returns:
            communities_search_response: Response data
        """
        url = self.client.base_url + "/2/communities/search"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if query is not None:
            params["query"] = query
        if max_results is not None:
            params["max_results"] = max_results
        if next_token is not None:
            params["next_token"] = next_token
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if community_fields is not None:
            params["community.fields"] = community_fields
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
        return communities_search_response.model_validate(response_data)


    def community_id_get(
        self,
        id: str,
        community_fields: List = None,
    ) -> community_id_get_response:
        """
        Communities lookup by Community ID.
        Returns a Community.
        Args:
            id: The ID of the Community.
        Args:
            community_fields: A comma separated list of Community fields to display.
        Returns:
            community_id_get_response: Response data
        """
        url = self.client.base_url + "/2/communities/{id}"
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
        if community_fields is not None:
            params["community.fields"] = community_fields
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
        return community_id_get_response.model_validate(response_data)
