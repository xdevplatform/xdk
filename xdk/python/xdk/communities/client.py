"""
Communities client for the X API.

This module provides a client for interacting with the Communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class CommunitiesClient:
    """Client for Communities operations"""


    def __init__(self, client: Client):
        self.client = client


    def community_id_get(self,
        id: str,
        community_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Communities lookup by Community ID.
        Returns a Community.
        Args:
            id: The ID of the Community.
        Args:
            community_fields: A comma separated list of Community fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/communities/{id}"
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
        # Return the response data
        return response.json()


    def communities_search(self,
        query: str,
        max_results: int = None,
        next_token: str = None,
        pagination_token: str = None,
        community_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/communities/search"
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
        response = self.client.session.get(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()
