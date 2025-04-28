"""
Spaces client for the X API.

This module provides a client for interacting with the Spaces endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import (
    search_spaces_response,
    find_spaces_by_creator_ids_response,
    space_buyers_response,
    find_space_by_id_response,
    space_tweets_response,
    find_spaces_by_ids_response,
)


class SpacesClient:
    """Client for Spaces operations"""


    def __init__(self, client: Client):
        self.client = client


    def search_spaces(
        self,
        query: str,
        state: str = None,
        max_results: int = None,
        space_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
        topic_fields: List = None,
    ) -> search_spaces_response:
        """
        Search for Spaces
        Returns Spaces that match the provided query.
        Args:
            query: The search query.
        Args:
            state: The state of Spaces to search for.
        Args:
            max_results: The number of results to return.
        Args:
            space_fields: A comma separated list of Space fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            topic_fields: A comma separated list of Topic fields to display.
        Returns:
            search_spaces_response: Response data
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
        if space_fields is not None:
            params["space.fields"] = ",".join(str(item) for item in space_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if topic_fields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topic_fields)
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
        return search_spaces_response.model_validate(response_data)


    def find_spaces_by_creator_ids(
        self,
        user_ids: List,
        space_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
        topic_fields: List = None,
    ) -> find_spaces_by_creator_ids_response:
        """
        Space lookup by their creators
        Returns a variety of information about the Spaces created by the provided User IDs
        Args:
            user_ids: The IDs of Users to search through.
        Args:
            space_fields: A comma separated list of Space fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            topic_fields: A comma separated list of Topic fields to display.
        Returns:
            find_spaces_by_creator_ids_response: Response data
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
        if space_fields is not None:
            params["space.fields"] = ",".join(str(item) for item in space_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if topic_fields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topic_fields)
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
        return find_spaces_by_creator_ids_response.model_validate(response_data)


    def space_buyers(
        self,
        id: str,
        pagination_token: str = None,
        max_results: int = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> space_buyers_response:
        """
        Retrieve the list of Users who purchased a ticket to the given space
        Retrieves the list of Users who purchased a ticket to the given space
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            max_results: The maximum number of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            space_buyers_response: Response data
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
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
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
        return space_buyers_response.model_validate(response_data)


    def find_space_by_id(
        self,
        id: str,
        space_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
        topic_fields: List = None,
    ) -> find_space_by_id_response:
        """
        Space lookup by Space ID
        Returns a variety of information about the Space specified by the requested ID
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            space_fields: A comma separated list of Space fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            topic_fields: A comma separated list of Topic fields to display.
        Returns:
            find_space_by_id_response: Response data
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
        if space_fields is not None:
            params["space.fields"] = ",".join(str(item) for item in space_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if topic_fields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topic_fields)
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
        return find_space_by_id_response.model_validate(response_data)


    def space_tweets(
        self,
        id: str,
        max_results: int = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> space_tweets_response:
        """
        Retrieve Posts from a Space.
        Retrieves Posts shared in the specified Space.
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            max_results: The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            place_fields: A comma separated list of Place fields to display.
        Returns:
            space_tweets_response: Response data
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
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
        if poll_fields is not None:
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if place_fields is not None:
            params["place.fields"] = ",".join(str(item) for item in place_fields)
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
        return space_tweets_response.model_validate(response_data)


    def find_spaces_by_ids(
        self,
        ids: List,
        space_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
        topic_fields: List = None,
    ) -> find_spaces_by_ids_response:
        """
        Space lookup up Space IDs
        Returns a variety of information about the Spaces specified by the requested IDs
        Args:
            ids: The list of Space IDs to return.
        Args:
            space_fields: A comma separated list of Space fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            topic_fields: A comma separated list of Topic fields to display.
        Returns:
            find_spaces_by_ids_response: Response data
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
        if space_fields is not None:
            params["space.fields"] = ",".join(str(item) for item in space_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if topic_fields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topic_fields)
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
        return find_spaces_by_ids_response.model_validate(response_data)
