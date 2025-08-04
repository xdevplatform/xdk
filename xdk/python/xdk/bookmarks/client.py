"""
Bookmarks client for the X API.

This module provides a client for interacting with the Bookmarks endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import (
    GetUsersBookmarkFoldersResponse,
    GetUsersBookmarksResponse,
    CreateUsersBookmarkRequest,
    CreateUsersBookmarkResponse,
    DeleteUsersBookmarkResponse,
    GetUsersBookmarksByFolderIdResponse,
)


class BookmarksClient:
    """Client for Bookmarks operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_users_bookmark_folders(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
    ) -> GetUsersBookmarkFoldersResponse:
        """
        Get Bookmark folders
        Retrieves a list of Bookmark folders created by the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Returns:
            GetUsersBookmarkFoldersResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/folders"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        return GetUsersBookmarkFoldersResponse.model_validate(response_data)


    def get_users_bookmarks(
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
    ) -> GetUsersBookmarksResponse:
        """
        Get Bookmarks
        Retrieves a list of Posts bookmarked by the authenticated user.
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
            GetUsersBookmarksResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        return GetUsersBookmarksResponse.model_validate(response_data)


    def create_users_bookmark(
        self,
        id: str,
        body: CreateUsersBookmarkRequest,
    ) -> CreateUsersBookmarkResponse:
        """
        Create Bookmark
        Adds a post to the authenticated user’s bookmarks.
        Args:
            id: The ID of the authenticated source User for whom to add bookmarks.
            body: Request body
        Returns:
            CreateUsersBookmarkResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
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
        return CreateUsersBookmarkResponse.model_validate(response_data)


    def delete_users_bookmark(
        self,
        id: str,
        tweet_id: str,
    ) -> DeleteUsersBookmarkResponse:
        """
        Delete Bookmark
        Removes a Post from the authenticated user’s Bookmarks by its ID.
        Args:
            id: The ID of the authenticated source User whose bookmark is to be removed.
        Args:
            tweet_id: The ID of the Post that the source User is removing from bookmarks.
        Returns:
            DeleteUsersBookmarkResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/{tweet_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{tweet_id}", str(tweet_id))
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
        return DeleteUsersBookmarkResponse.model_validate(response_data)


    def get_users_bookmarks_by_folder_id(
        self,
        id: str,
        folder_id: str,
    ) -> GetUsersBookmarksByFolderIdResponse:
        """
        Get Bookmarks by folder ID
        Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            folder_id: The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.
        Returns:
            GetUsersBookmarksByFolderIdResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/folders/{folder_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{folder_id}", str(folder_id))
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
        return GetUsersBookmarksByFolderIdResponse.model_validate(response_data)
