"""
Communities client for the X API.

This module provides a client for interacting with the Communities endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_communitites_id_name_response, 2_communities_search_response, 2_communities_id_response, 2_users_id_pinned_communities_request, 2_users_id_pinned_communities_response, 2_users_id_pinned_communities_request, 2_users_id_pinned_communities_response, 2_communities_request, 2_communities_response

class CommunitiesClient:
    """Client for Communities operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def community_id_delete(self, 
        
        
        
        id: str,
        
        
        
        name: str,
        
        
        
        
        
        
        
        
    ) -> 2_communitites_id_name_response:
        """
        Delete Community
        
        
        Delete a Community that you own.
        
        
        
        
        Args:
            id: The ID of the Community to delete.
        
        
        
        Args:
            name: The name of the Community to delete.
        
        
        
        
        Returns:
            2_communitites_id_name_response: Response data
        """
        url = self.client.base_url + "/2/communitites/{id}/{name}"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        
        
        
        
        url = url.replace("{id}", str(id))
        
        
        
        
        
        url = url.replace("{name}", str(name))
        
        
        
        
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
        
        return 2_communitites_id_name_response.model_validate(response_data)
        
    
    def search_communities(self, 
        
        
        
        query: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        next_token: str = None,
        
        
        
        pagination_token: str = None,
        
        
        
        community_fields: List = None,
        
        
        
        
    ) -> 2_communities_search_response:
        """
        Search Communities
        
        
        Retrieves a list of Communities matching the specified search query.
        
        
        
        
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
            2_communities_search_response: Response data
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
            
            params["community.fields"] = ",".join(str(item) for item in community_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_communities_search_response.model_validate(response_data)
        
    
    def get_communities_by_id(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        community_fields: List = None,
        
        
        
        
    ) -> 2_communities_id_response:
        """
        Get Community by ID
        
        
        Retrieves details of a specific Community by its ID.
        
        
        
        
        Args:
            id: The ID of the Community.
        
        
        
        Args:
            community_fields: A comma separated list of Community fields to display.
        
        
        
        
        Returns:
            2_communities_id_response: Response data
        """
        url = self.client.base_url + "/2/communities/{id}"

        

        
        
        
        
        
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
        
        
        
        
        
        
        
        if community_fields is not None:
            
            params["community.fields"] = ",".join(str(item) for item in community_fields)
            
        
        
        
        
        
        
        
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
        
        return 2_communities_id_response.model_validate(response_data)
        
    
    def community_user_pin(self, 
        
        
        
        id: str,
        
        
        
        
        body: 2_users_id_pinned_communities_request,
        
        
        
        
        
    ) -> 2_users_id_pinned_communities_response:
        """
        Pin a Community
        
        
        Causes a User to pin a community.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that will pin the Community.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_users_id_pinned_communities_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_communities"

        

        
        
        
        
        
        
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
        
        return 2_users_id_pinned_communities_response.model_validate(response_data)
        
    
    def community_user_unpin(self, 
        
        
        
        id: str,
        
        
        
        
        body: 2_users_id_pinned_communities_request,
        
        
        
        
        
    ) -> 2_users_id_pinned_communities_response:
        """
        Unpin a Community
        
        
        Causes a User to unpin a community.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that will unpin the Community.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_users_id_pinned_communities_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_communities"

        

        
        
        
        
        
        
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
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.delete(
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
        
        return 2_users_id_pinned_communities_response.model_validate(response_data)
        
    
    def community_id_create(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_communities_request] = None,
        
    ) -> 2_communities_response:
        """
        Create Community
        
        
        Creates a new Community.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_communities_response: Response data
        """
        url = self.client.base_url + "/2/communities"

        

        
        
        
        
        
        
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
        
        return 2_communities_response.model_validate(response_data)
        
    