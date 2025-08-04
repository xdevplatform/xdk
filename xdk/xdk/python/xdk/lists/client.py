"""
Lists client for the X API.

This module provides a client for interacting with the Lists endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    
    
    CreatelistsRequest,
    
    CreatelistsResponse,
    
    
    
    
    GetlistsbyidResponse,
    
    
    
    UpdatelistsRequest,
    
    UpdatelistsResponse,
    
    
    
    
    DeletelistsResponse,
    
    
    
    UnfollowlistResponse,
    
    
    
    GetusersfollowedlistsResponse,
    
    
    
    FollowlistRequest,
    
    FollowlistResponse,
    
    
    
    
    UnpinlistResponse,
    
    
    
    AddlistsmemberRequest,
    
    AddlistsmemberResponse,
    
    
    
    
    GetuserslistmembershipsResponse,
    
    
    
    GetuserspinnedlistsResponse,
    
    
    
    PinlistRequest,
    
    PinlistResponse,
    
    
    
    
    RemovelistsmemberbyuseridResponse,
    
    
    
    GetusersownedlistsResponse,
    
    
)

class ListsClient:
    """Client for Lists operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def create_lists(self, 
        
        
        
        
        
        
        
        
        body: Optional[CreatelistsRequest] = None,
        
    ) -> CreatelistsResponse:
        """
        Create List
        
        
        Creates a new List for the authenticated user.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            CreatelistsResponse: Response data
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
        
        return CreatelistsResponse.model_validate(response_data)
        
    
    def get_lists_by_id(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        list_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        
    ) -> GetlistsbyidResponse:
        """
        Get List by ID
        
        
        Retrieves details of a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the List.
        
        
        
        Args:
            list_fields: A comma separated list of List fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        
        Returns:
            GetlistsbyidResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
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
        
        return GetlistsbyidResponse.model_validate(response_data)
        
    
    def update_lists(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[UpdatelistsRequest] = None,
        
    ) -> UpdatelistsResponse:
        """
        Update List
        
        
        Updates the details of a specific List owned by the authenticated user by its ID.
        
        
        
        
        Args:
            id: The ID of the List to modify.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            UpdatelistsResponse: Response data
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
        
        return UpdatelistsResponse.model_validate(response_data)
        
    
    def delete_lists(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> DeletelistsResponse:
        """
        Delete List
        
        
        Deletes a specific List owned by the authenticated user by its ID.
        
        
        
        
        Args:
            id: The ID of the List to delete.
        
        
        
        
        Returns:
            DeletelistsResponse: Response data
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
        
        return DeletelistsResponse.model_validate(response_data)
        
    
    def unfollow_list(self, 
        
        
        
        id: str,
        
        
        
        list_id: str,
        
        
        
        
        
        
        
        
    ) -> UnfollowlistResponse:
        """
        Unfollow List
        
        
        Causes the authenticated user to unfollow a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that will unfollow the List.
        
        
        
        Args:
            list_id: The ID of the List to unfollow.
        
        
        
        
        Returns:
            UnfollowlistResponse: Response data
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
        
        return UnfollowlistResponse.model_validate(response_data)
        
    
    def get_users_followed_lists(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        list_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        
    ) -> GetusersfollowedlistsResponse:
        """
        Get followed Lists
        
        
        Retrieves a list of Lists followed by a specific User by their ID.
        
        
        
        
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
            GetusersfollowedlistsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
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
        
        return GetusersfollowedlistsResponse.model_validate(response_data)
        
    
    def follow_list(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[FollowlistRequest] = None,
        
    ) -> FollowlistResponse:
        """
        Follow List
        
        
        Causes the authenticated user to follow a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that will follow the List.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            FollowlistResponse: Response data
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
        
        return FollowlistResponse.model_validate(response_data)
        
    
    def unpin_list(self, 
        
        
        
        id: str,
        
        
        
        list_id: str,
        
        
        
        
        
        
        
        
    ) -> UnpinlistResponse:
        """
        Unpin List
        
        
        Causes the authenticated user to unpin a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User for whom to return results.
        
        
        
        Args:
            list_id: The ID of the List to unpin.
        
        
        
        
        Returns:
            UnpinlistResponse: Response data
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
        
        return UnpinlistResponse.model_validate(response_data)
        
    
    def add_lists_member(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[AddlistsmemberRequest] = None,
        
    ) -> AddlistsmemberResponse:
        """
        Add List member
        
        
        Adds a User to a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the List for which to add a member.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            AddlistsmemberResponse: Response data
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
        
        return AddlistsmemberResponse.model_validate(response_data)
        
    
    def get_users_list_memberships(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        list_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        
    ) -> GetuserslistmembershipsResponse:
        """
        Get List memberships
        
        
        Retrieves a list of Lists that a specific User is a member of by their ID.
        
        
        
        
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
            GetuserslistmembershipsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/list_memberships"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
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
        
        return GetuserslistmembershipsResponse.model_validate(response_data)
        
    
    def get_users_pinned_lists(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        list_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        
    ) -> GetuserspinnedlistsResponse:
        """
        Get pinned Lists
        
        
        Retrieves a list of Lists pinned by the authenticated user.
        
        
        
        
        Args:
            id: The ID of the authenticated source User for whom to return results.
        
        
        
        Args:
            list_fields: A comma separated list of List fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        
        Returns:
            GetuserspinnedlistsResponse: Response data
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
        
        return GetuserspinnedlistsResponse.model_validate(response_data)
        
    
    def pin_list(self, 
        
        
        
        id: str,
        
        
        
        
        body: PinlistRequest,
        
        
        
        
        
    ) -> PinlistResponse:
        """
        Pin List
        
        
        Causes the authenticated user to pin a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that will pin the List.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            PinlistResponse: Response data
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
        
        return PinlistResponse.model_validate(response_data)
        
    
    def remove_lists_member_by_user_id(self, 
        
        
        
        id: str,
        
        
        
        user_id: str,
        
        
        
        
        
        
        
        
    ) -> RemovelistsmemberbyuseridResponse:
        """
        Remove List member
        
        
        Removes a User from a specific List by its ID and the User’s ID.
        
        
        
        
        Args:
            id: The ID of the List to remove a member.
        
        
        
        Args:
            user_id: The ID of User that will be removed from the List.
        
        
        
        
        Returns:
            RemovelistsmemberbyuseridResponse: Response data
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
        
        return RemovelistsmemberbyuseridResponse.model_validate(response_data)
        
    
    def get_users_owned_lists(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        list_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        
    ) -> GetusersownedlistsResponse:
        """
        Get owned Lists
        
        
        Retrieves a list of Lists owned by a specific User by their ID.
        
        
        
        
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
            GetusersownedlistsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/owned_lists"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
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
        
        return GetusersownedlistsResponse.model_validate(response_data)
        
    