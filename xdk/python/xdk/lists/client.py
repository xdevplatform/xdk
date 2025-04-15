"""
Lists client for the X API.

This module provides a client for interacting with the Lists endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class ListsClient:
    """Client for Lists operations"""


    def __init__(self, client: Client):
        self.client = client


    def user_followed_lists(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if list_fields is not None:
            params["list.fields"] = list_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
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


    def list_user_follow(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Follow a List
        Causes a User to follow a List.
        Args:
            id: The ID of the authenticated source User that will follow the List.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_id_get(self,
        id: str,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
        params = {}
        if list_fields is not None:
            params["list.fields"] = list_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
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


    def list_id_update(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Update List.
        Update a List that you own.
        Args:
            id: The ID of the List to modify.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.put(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_id_delete(self,
        id: str,
    ) -> Dict[str, Any]:
        """
        Delete List
        Delete a List that you own.
        Args:
            id: The ID of the List to delete.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_user_unfollow(self,
        id: str,
        list_id: str,
    ) -> Dict[str, Any]:
        """
        Unfollow a List
        Causes a User to unfollow a List.
        Args:
            id: The ID of the authenticated source User that will unfollow the List.
        Args:
            list_id: The ID of the List to unfollow.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists/{list_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{list_id}", str(list_id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_id_create(self,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Create List
        Creates a new List.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists"
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def get_user_list_memberships(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/list_memberships"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if list_fields is not None:
            params["list.fields"] = list_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
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


    def list_user_owned_lists(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/owned_lists"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if list_fields is not None:
            params["list.fields"] = list_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
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


    def list_user_pinned_lists(self,
        id: str,
        list_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists"
        params = {}
        if list_fields is not None:
            params["list.fields"] = list_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
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


    def list_user_pin(self,
        id: str,
        body: Dict[str, Any]
              ,
    ) -> Dict[str, Any]:
        """
        Pin a List
        Causes a User to pin a List.
        Args:
            id: The ID of the authenticated source User that will pin the List.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_add_member(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Add a List member
        Causes a User to become a member of a List.
        Args:
            id: The ID of the List for which to add a member.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_remove_member(self,
        id: str,
        user_id: str,
    ) -> Dict[str, Any]:
        """
        Remove a List member
        Causes a User to be removed from the members of a List.
        Args:
            id: The ID of the List to remove a member.
        Args:
            user_id: The ID of User that will be removed from the List.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members/{user_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{user_id}", str(user_id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def list_user_unpin(self,
        id: str,
        list_id: str,
    ) -> Dict[str, Any]:
        """
        Unpin a List
        Causes a User to remove a pinned List.
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            list_id: The ID of the List to unpin.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists/{list_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{list_id}", str(list_id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()
