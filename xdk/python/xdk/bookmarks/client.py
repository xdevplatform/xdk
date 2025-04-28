"""
Bookmarks client for the X API.

This module provides a client for interacting with the Bookmarks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import requests_oauthlib
from ..client import Client
from .models import (
    get_users_id_bookmark_folder_posts_response,
    get_users_id_bookmark_folders_response,
    users_id_bookmarks_delete_response,
    get_users_id_bookmarks_response,
    post_users_id_bookmarks_request,
    post_users_id_bookmarks_response,
)


class BookmarksClient:
    """Client for Bookmarks operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_users_id_bookmark_folder_posts(
        self,
        id: str,
        folder_id: str,
    ) -> get_users_id_bookmark_folder_posts_response:
        """
        Bookmark Folder Posts by User and Folder id
        Returns posts belonging to input bookmarks folder id that have been created by the requesting User
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            folder_id: The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.
        Returns:
            get_users_id_bookmark_folder_posts_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/folders/{folder_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{folder_id}", str(folder_id))
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
        return get_users_id_bookmark_folder_posts_response.model_validate(response_data)


    def get_users_id_bookmark_folders(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
    ) -> get_users_id_bookmark_folders_response:
        """
        Bookmark folders by User
        Returns metadata about Bookmark folders that have been created by the requesting User
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Returns:
            get_users_id_bookmark_folders_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/folders"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        return get_users_id_bookmark_folders_response.model_validate(response_data)


    def users_id_bookmarks_delete(
        self,
        id: str,
        tweet_id: str,
    ) -> users_id_bookmarks_delete_response:
        """
        Remove a bookmarked Post
        Removes a Post from the requesting User's bookmarked Posts.
        Args:
            id: The ID of the authenticated source User whose bookmark is to be removed.
        Args:
            tweet_id: The ID of the Post that the source User is removing from bookmarks.
        Returns:
            users_id_bookmarks_delete_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/{tweet_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{tweet_id}", str(tweet_id))
        headers = {}
        # Make the request
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
        return users_id_bookmarks_delete_response.model_validate(response_data)


    def get_users_id_bookmarks(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> get_users_id_bookmarks_response:
        """
        Bookmarks by User
        Returns Post objects that have been bookmarked by the requesting User
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
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
            get_users_id_bookmarks_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_users_id_bookmarks_response.model_validate(response_data)


    def post_users_id_bookmarks(
        self,
        id: str,
        body: post_users_id_bookmarks_request,
    ) -> post_users_id_bookmarks_response:
        """
        Add Post to Bookmarks
        Adds a Post (ID in the body) to the requesting User's (in the path) bookmarks
        Args:
            id: The ID of the authenticated source User for whom to add bookmarks.
            body: Request body
        Returns:
            post_users_id_bookmarks_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
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
        return post_users_id_bookmarks_response.model_validate(response_data)
