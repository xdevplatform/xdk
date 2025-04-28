"""
Lists client for the X API.

This module provides a client for interacting with the Lists endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import (
    list_remove_member_response,
    list_user_pinned_lists_response,
    list_user_pin_request,
    list_user_pin_response,
    list_add_member_request,
    list_add_member_response,
    list_id_create_request,
    list_id_create_response,
    list_user_owned_lists_response,
    list_id_get_response,
    list_id_update_request,
    list_id_update_response,
    list_id_delete_response,
    get_user_list_memberships_response,
    user_followed_lists_response,
    list_user_follow_request,
    list_user_follow_response,
    list_user_unfollow_response,
    list_user_unpin_response,
)


class ListsClient:
    """Client for Lists operations"""


    def __init__(self, client: Client):
        self.client = client


    def list_remove_member(
        self,
        id: str,
        user_id: str,
    ) -> list_remove_member_response:
        """
        Remove a List member
        Causes a User to be removed from the members of a List.
        Args:
            id: The ID of the List to remove a member.
        Args:
            user_id: The ID of User that will be removed from the List.
        Returns:
            list_remove_member_response: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members/{user_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{user_id}", str(user_id))
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
        return list_remove_member_response.model_validate(response_data)


    def list_user_pinned_lists(
        self,
        id: str,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> list_user_pinned_lists_response:
        """
        Get a User's Pinned Lists
        Get a User's Pinned Lists.
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            list_fields: A comma separated list of List fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Returns:
            list_user_pinned_lists_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if list_fields is not None:
            params["list.fields"] = ",".join(str(item) for item in list_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
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
        return list_user_pinned_lists_response.model_validate(response_data)


    def list_user_pin(
        self,
        id: str,
        body: list_user_pin_request,
    ) -> list_user_pin_response:
        """
        Pin a List
        Causes a User to pin a List.
        Args:
            id: The ID of the authenticated source User that will pin the List.
            body: Request body
        Returns:
            list_user_pin_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists"
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
        return list_user_pin_response.model_validate(response_data)


    def list_add_member(
        self,
        id: str,
        body: Optional[list_add_member_request] = None,
    ) -> list_add_member_response:
        """
        Add a List member
        Causes a User to become a member of a List.
        Args:
            id: The ID of the List for which to add a member.
            body: Request body
        Returns:
            list_add_member_response: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members"
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
        return list_add_member_response.model_validate(response_data)


    def list_id_create(
        self,
        body: Optional[list_id_create_request] = None,
    ) -> list_id_create_response:
        """
        Create List
        Creates a new List.
            body: Request body
        Returns:
            list_id_create_response: Response data
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
        return list_id_create_response.model_validate(response_data)


    def list_user_owned_lists(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> list_user_owned_lists_response:
        """
        Get a User's Owned Lists.
        Get a User's Owned Lists.
        Args:
            id: The ID of the User to lookup.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            list_fields: A comma separated list of List fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Returns:
            list_user_owned_lists_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/owned_lists"
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
        if list_fields is not None:
            params["list.fields"] = ",".join(str(item) for item in list_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
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
        return list_user_owned_lists_response.model_validate(response_data)


    def list_id_get(
        self,
        id: str,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> list_id_get_response:
        """
        List lookup by List ID.
        Returns a List.
        Args:
            id: The ID of the List.
        Args:
            list_fields: A comma separated list of List fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Returns:
            list_id_get_response: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
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
        if list_fields is not None:
            params["list.fields"] = ",".join(str(item) for item in list_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
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
        return list_id_get_response.model_validate(response_data)


    def list_id_update(
        self,
        id: str,
        body: Optional[list_id_update_request] = None,
    ) -> list_id_update_response:
        """
        Update List.
        Update a List that you own.
        Args:
            id: The ID of the List to modify.
            body: Request body
        Returns:
            list_id_update_response: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
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
            response = self.client.oauth2_session.put(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        else:
            response = self.client.session.put(
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
        return list_id_update_response.model_validate(response_data)


    def list_id_delete(
        self,
        id: str,
    ) -> list_id_delete_response:
        """
        Delete List
        Delete a List that you own.
        Args:
            id: The ID of the List to delete.
        Returns:
            list_id_delete_response: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
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
        return list_id_delete_response.model_validate(response_data)


    def get_user_list_memberships(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> get_user_list_memberships_response:
        """
        Get a User's List Memberships
        Get a User's List Memberships.
        Args:
            id: The ID of the User to lookup.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            list_fields: A comma separated list of List fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Returns:
            get_user_list_memberships_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/list_memberships"
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
        if list_fields is not None:
            params["list.fields"] = ",".join(str(item) for item in list_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
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
        return get_user_list_memberships_response.model_validate(response_data)


    def user_followed_lists(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> user_followed_lists_response:
        """
        Get User's Followed Lists
        Returns a User's followed Lists.
        Args:
            id: The ID of the User to lookup.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            list_fields: A comma separated list of List fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            user_fields: A comma separated list of User fields to display.
        Returns:
            user_followed_lists_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"
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
        if list_fields is not None:
            params["list.fields"] = ",".join(str(item) for item in list_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
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
        return user_followed_lists_response.model_validate(response_data)


    def list_user_follow(
        self,
        id: str,
        body: Optional[list_user_follow_request] = None,
    ) -> list_user_follow_response:
        """
        Follow a List
        Causes a User to follow a List.
        Args:
            id: The ID of the authenticated source User that will follow the List.
            body: Request body
        Returns:
            list_user_follow_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"
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
        return list_user_follow_response.model_validate(response_data)


    def list_user_unfollow(
        self,
        id: str,
        list_id: str,
    ) -> list_user_unfollow_response:
        """
        Unfollow a List
        Causes a User to unfollow a List.
        Args:
            id: The ID of the authenticated source User that will unfollow the List.
        Args:
            list_id: The ID of the List to unfollow.
        Returns:
            list_user_unfollow_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists/{list_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{list_id}", str(list_id))
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
        return list_user_unfollow_response.model_validate(response_data)


    def list_user_unpin(
        self,
        id: str,
        list_id: str,
    ) -> list_user_unpin_response:
        """
        Unpin a List
        Causes a User to remove a pinned List.
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            list_id: The ID of the List to unpin.
        Returns:
            list_user_unpin_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists/{list_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{list_id}", str(list_id))
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
        return list_user_unpin_response.model_validate(response_data)
