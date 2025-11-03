
"""
Auto-generated spaces client for the X API.

This module provides a client for interacting with the spaces endpoints of the X API.

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
    
    
    GetByIdResponse,
    
    
    
    GetByCreatorIdsResponse,
    
    
    
    SearchResponse,
    
    
    
    GetPostsResponse,
    
    
    
    GetByIdsResponse,
    
    
    
    GetBuyersResponse,
    
    
)

class SpacesClient:
    """Client for spaces operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def get_by_id(self, id: str, spacefields: List = None, expansions: List = None, userfields: List = None, topicfields: List = None) -> GetByIdResponse:
        """
        Get space by ID
        
        Retrieves details of a specific space by its ID.
        
        Args:
            id: The ID of the Space to be retrieved.
            spacefields: A comma separated list of Space fields to display.
            expansions: A comma separated list of fields to expand.
            userfields: A comma separated list of User fields to display.
            topicfields: A comma separated list of Topic fields to display.
            Returns:
            GetByIdResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}"
        url = url.replace("{id}", str(id))
        

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
        if spacefields is not None:
            params["space.fields"] = ",".join(str(item) for item in spacefields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if topicfields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topicfields)
            
        
        
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
        
        

    
    def get_by_creator_ids(self, user_ids: List, spacefields: List = None, expansions: List = None, userfields: List = None, topicfields: List = None) -> GetByCreatorIdsResponse:
        """
        Get Spaces by creator IDs
        
        Retrieves details of Spaces created by specified User IDs.
        
        Args:
            user_ids: The IDs of Users to search through.
            spacefields: A comma separated list of Space fields to display.
            expansions: A comma separated list of fields to expand.
            userfields: A comma separated list of User fields to display.
            topicfields: A comma separated list of Topic fields to display.
            Returns:
            GetByCreatorIdsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/by/creator_ids"
        

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
        if user_ids is not None:
            params["user_ids"] = ",".join(str(item) for item in user_ids)
            
        if spacefields is not None:
            params["space.fields"] = ",".join(str(item) for item in spacefields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if topicfields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topicfields)
            
        
        
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
        
        return GetByCreatorIdsResponse.model_validate(response_data)
        
        

    
    def search(self, query: str, state: str = None, max_results: int = None, spacefields: List = None, expansions: List = None, userfields: List = None, topicfields: List = None) -> SearchResponse:
        """
        Search Spaces
        
        Retrieves a list of Spaces matching the specified search query.
        
        Args:
            query: The search query.
            state: The state of Spaces to search for.
            max_results: The number of results to return.
            spacefields: A comma separated list of Space fields to display.
            expansions: A comma separated list of fields to expand.
            userfields: A comma separated list of User fields to display.
            topicfields: A comma separated list of Topic fields to display.
            Returns:
            SearchResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/search"
        

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
        if query is not None:
            params["query"] = query
            
        if state is not None:
            params["state"] = state
            
        if max_results is not None:
            params["max_results"] = max_results
            
        if spacefields is not None:
            params["space.fields"] = ",".join(str(item) for item in spacefields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if topicfields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topicfields)
            
        
        
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
        
        return SearchResponse.model_validate(response_data)
        
        

    
    def get_posts(self, id: str, max_results: int = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> GetPostsResponse:
        """
        Get Space Posts
        
        Retrieves a list of Posts shared in a specific Space by its ID.
        
        Args:
            id: The ID of the Space to be retrieved.
            max_results: The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            GetPostsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/tweets"
        url = url.replace("{id}", str(id))
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
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
        
        

    
    def get_by_ids(self, ids: List, spacefields: List = None, expansions: List = None, userfields: List = None, topicfields: List = None) -> GetByIdsResponse:
        """
        Get Spaces by IDs
        
        Retrieves details of multiple Spaces by their IDs.
        
        Args:
            ids: The list of Space IDs to return.
            spacefields: A comma separated list of Space fields to display.
            expansions: A comma separated list of fields to expand.
            userfields: A comma separated list of User fields to display.
            topicfields: A comma separated list of Topic fields to display.
            Returns:
            GetByIdsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces"
        

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
        if ids is not None:
            params["ids"] = ",".join(str(item) for item in ids)
            
        if spacefields is not None:
            params["space.fields"] = ",".join(str(item) for item in spacefields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if topicfields is not None:
            params["topic.fields"] = ",".join(str(item) for item in topicfields)
            
        
        
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
        
        return GetByIdsResponse.model_validate(response_data)
        
        

    
    def get_buyers(self, id: str, pagination_token: Any = None, max_results: int = None, userfields: List = None, expansions: List = None, tweetfields: List = None) -> GetBuyersResponse:
        """
        Get Space ticket buyers
        
        Retrieves a list of Users who purchased tickets to a specific Space by its ID.
        
        Args:
            id: The ID of the Space to be retrieved.
            pagination_token: This parameter is used to get a specified 'page' of results.
            max_results: The maximum number of results.
            userfields: A comma separated list of User fields to display.
            expansions: A comma separated list of fields to expand.
            tweetfields: A comma separated list of Tweet fields to display.
            Returns:
            GetBuyersResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/buyers"
        url = url.replace("{id}", str(id))
        

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
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        
        
        headers = {}
        
        
        # Prepare request data
        json_data = None
        
        
        
        










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
        
        return GetBuyersResponse.model_validate(response_data)
        
        

    