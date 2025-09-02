"""
Auto-generated lists client for the X API.

This module provides a client for interacting with the lists endpoints of the X API.

All methods, parameters, and response models are generated from the OpenAPI specification.

Generated automatically - do not edit manually.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time


if TYPE_CHECKING:
    from ..client import Client
from .models import (
    CreateRequest,
    CreateResponse,
    GetByIdResponse,
    UpdateRequest,
    UpdateResponse,
    DeleteResponse,
    GetMembersResponse,
    AddMemberRequest,
    AddMemberResponse,
    GetFollowersResponse,
    GetPostsResponse,
    RemoveMemberByUserIdResponse,
)


class ListsClient:
    """Client for lists operations"""


    def __init__(self, client: Client):
        self.client = client


    def create(self, body: Optional[CreateRequest] = None) -> CreateResponse:
        """
        Create List
        Creates a new List for the authenticated user.
        body: Request body
        Returns:
            CreateResponse: Response data
        """
        url = self.client.base_url + "/2/lists"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateResponse.model_validate(response_data)


    def get_by_id(self, id: Any) -> GetByIdResponse:
        """
        Get List by ID
        Retrieves details of a specific List by its ID.
        Args:
            id: The ID of the List.
            Returns:
            GetByIdResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
        url = url.replace("{id}", str(id))
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
        headers = {}
        # Prepare request data
        json_data = None
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


    def update(self, id: Any, body: Optional[UpdateRequest] = None) -> UpdateResponse:
        """
        Update List
        Updates the details of a specific List owned by the authenticated user by its ID.
        Args:
            id: The ID of the List to modify.
            body: Request body
        Returns:
            UpdateResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
        url = url.replace("{id}", str(id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.put(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.put(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return UpdateResponse.model_validate(response_data)


    def delete(self, id: Any) -> DeleteResponse:
        """
        Delete List
        Deletes a specific List owned by the authenticated user by its ID.
        Args:
            id: The ID of the List to delete.
            Returns:
            DeleteResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
        url = url.replace("{id}", str(id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        # Prepare request data
        json_data = None
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


    def get_members(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetMembersResponse:
        """
        Get List members
        Retrieves a list of Users who are members of a specific List by its ID.
        Args:
            id: The ID of the List.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetMembersResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members"
        url = url.replace("{id}", str(id))
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
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        headers = {}
        # Prepare request data
        json_data = None
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
        return GetMembersResponse.model_validate(response_data)


    def add_member(
        self, id: Any, body: Optional[AddMemberRequest] = None
    ) -> AddMemberResponse:
        """
        Add List member
        Adds a User to a specific List by its ID.
        Args:
            id: The ID of the List for which to add a member.
            body: Request body
        Returns:
            AddMemberResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members"
        url = url.replace("{id}", str(id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return AddMemberResponse.model_validate(response_data)


    def get_followers(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetFollowersResponse:
        """
        Get List followers
        Retrieves a list of Users who follow a specific List by its ID.
        Args:
            id: The ID of the List.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetFollowersResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/followers"
        url = url.replace("{id}", str(id))
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
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        headers = {}
        # Prepare request data
        json_data = None
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
        return GetFollowersResponse.model_validate(response_data)


    def get_posts(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetPostsResponse:
        """
        Get List Posts
        Retrieves a list of Posts associated with a specific List by its ID.
        Args:
            id: The ID of the List.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            Returns:
            GetPostsResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/tweets"
        url = url.replace("{id}", str(id))
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
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        headers = {}
        # Prepare request data
        json_data = None
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


    def remove_member_by_user_id(
        self, id: Any, user_id: Any
    ) -> RemoveMemberByUserIdResponse:
        """
        Remove List member
        Removes a User from a specific List by its ID and the User’s ID.
        Args:
            id: The ID of the List to remove a member.
            user_id: The ID of User that will be removed from the List.
            Returns:
            RemoveMemberByUserIdResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members/{user_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{user_id}", str(user_id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        # Prepare request data
        json_data = None
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
        return RemoveMemberByUserIdResponse.model_validate(response_data)
