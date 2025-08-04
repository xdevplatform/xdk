"""
Users client for the X API.

This module provides a client for interacting with the Users endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    
    
    GetpostslikingusersResponse,
    
    
    
    BlockusersdmsResponse,
    
    
    
    UnfollowuserResponse,
    
    
    
    GetusersbyidsResponse,
    
    
    
    GetusersbyusernamesResponse,
    
    
    
    GetpostsrepostedbyResponse,
    
    
    
    SearchusersResponse,
    
    
    
    GetusersblockingResponse,
    
    
    
    UnmuteuserResponse,
    
    
    
    GetusersbyidResponse,
    
    
    
    GetmyuserResponse,
    
    
    
    GetusersfollowingResponse,
    
    
    
    FollowuserRequest,
    
    FollowuserResponse,
    
    
    
    
    GetlistsfollowersResponse,
    
    
    
    GetlistsmembersResponse,
    
    
    
    GetusersfollowersResponse,
    
    
    
    GetusersrepostsofmeResponse,
    
    
    
    GetusersbyusernameResponse,
    
    
    
    GetusersmutingResponse,
    
    
    
    MuteuserRequest,
    
    MuteuserResponse,
    
    
    
    
    UnblockusersdmsResponse,
    
    
)

class UsersClient:
    """Client for Users operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def get_posts_liking_users(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetpostslikingusersResponse:
        """
        Get Liking Users
        
        
        Retrieves a list of Users who liked a specific Post by its ID.
        
        
        
        
        Args:
            id: A single Post ID.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetpostslikingusersResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/liking_users"

        

        
        
        
        
        
        
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
        
        return GetpostslikingusersResponse.model_validate(response_data)
        
    
    def block_users_dms(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> BlockusersdmsResponse:
        """
        Block DMs
        
        
        Blocks direct messages to or from a specific User by their ID for the authenticated user.
        
        
        
        
        Args:
            id: The ID of the target User that the authenticated user requesting to block dms for.
        
        
        
        
        Returns:
            BlockusersdmsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/dm/block"

        

        
        
        
        
        
        
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
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return BlockusersdmsResponse.model_validate(response_data)
        
    
    def unfollow_user(self, 
        
        
        
        source_user_id: str,
        
        
        
        target_user_id: str,
        
        
        
        
        
        
        
        
    ) -> UnfollowuserResponse:
        """
        Unfollow User
        
        
        Causes the authenticated user to unfollow a specific user by their ID.
        
        
        
        
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unfollow the target User.
        
        
        
        Args:
            target_user_id: The ID of the User that the source User is requesting to unfollow.
        
        
        
        
        Returns:
            UnfollowuserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{source_user_id}/following/{target_user_id}"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        
        
        
        
        url = url.replace("{source_user_id}", str(source_user_id))
        
        
        
        
        
        url = url.replace("{target_user_id}", str(target_user_id))
        
        
        
        
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
        
        return UnfollowuserResponse.model_validate(response_data)
        
    
    def get_users_by_ids(self, 
        
        
        
        ids: List,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersbyidsResponse:
        """
        Get Users by IDs
        
        
        Retrieves details of multiple Users by their IDs.
        
        
        
        
        Args:
            ids: A list of User IDs, comma-separated. You can specify up to 100 IDs.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersbyidsResponse: Response data
        """
        url = self.client.base_url + "/2/users"

        

        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return GetusersbyidsResponse.model_validate(response_data)
        
    
    def get_users_by_usernames(self, 
        
        
        
        usernames: List,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersbyusernamesResponse:
        """
        Get Users by usernames
        
        
        Retrieves details of multiple Users by their usernames.
        
        
        
        
        Args:
            usernames: A list of usernames, comma-separated.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersbyusernamesResponse: Response data
        """
        url = self.client.base_url + "/2/users/by"

        

        
        
        
        
        
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
        
        
        
        if usernames is not None:
            
            params["usernames"] = ",".join(str(item) for item in usernames)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return GetusersbyusernamesResponse.model_validate(response_data)
        
    
    def get_posts_reposted_by(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetpostsrepostedbyResponse:
        """
        Get Reposted by
        
        
        Retrieves a list of Users who reposted a specific Post by its ID.
        
        
        
        
        Args:
            id: A single Post ID.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetpostsrepostedbyResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/retweeted_by"

        

        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
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
        
        return GetpostsrepostedbyResponse.model_validate(response_data)
        
    
    def search_users(self, 
        
        
        
        query: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        next_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> SearchusersResponse:
        """
        Search Users
        
        
        Retrieves a list of Users matching a search query.
        
        
        
        
        Args:
            query: TThe the query string by which to query for users.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            SearchusersResponse: Response data
        """
        url = self.client.base_url + "/2/users/search"

        

        
        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return SearchusersResponse.model_validate(response_data)
        
    
    def get_users_blocking(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersblockingResponse:
        """
        Get blocking
        
        
        Retrieves a list of Users blocked by the specified User ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User for whom to return results.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersblockingResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/blocking"

        

        
        
        
        
        
        
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
        
        return GetusersblockingResponse.model_validate(response_data)
        
    
    def unmute_user(self, 
        
        
        
        source_user_id: str,
        
        
        
        target_user_id: str,
        
        
        
        
        
        
        
        
    ) -> UnmuteuserResponse:
        """
        Unmute User
        
        
        Causes the authenticated user to unmute a specific user by their ID.
        
        
        
        
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unmute the target User.
        
        
        
        Args:
            target_user_id: The ID of the User that the source User is requesting to unmute.
        
        
        
        
        Returns:
            UnmuteuserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{source_user_id}/muting/{target_user_id}"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        
        
        
        
        url = url.replace("{source_user_id}", str(source_user_id))
        
        
        
        
        
        url = url.replace("{target_user_id}", str(target_user_id))
        
        
        
        
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
        
        return UnmuteuserResponse.model_validate(response_data)
        
    
    def get_users_by_id(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersbyidResponse:
        """
        Get User by ID
        
        
        Retrieves details of a specific User by their ID.
        
        
        
        
        Args:
            id: The ID of the User to lookup.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersbyidResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}"

        

        
        
        
        
        
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
        
        
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
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
        
        return GetusersbyidResponse.model_validate(response_data)
        
    
    def get_my_user(self, 
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetmyuserResponse:
        """
        Get my User
        
        
        Retrieves details of the authenticated user.
        
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetmyuserResponse: Response data
        """
        url = self.client.base_url + "/2/users/me"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return GetmyuserResponse.model_validate(response_data)
        
    
    def get_users_following(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersfollowingResponse:
        """
        Get following
        
        
        Retrieves a list of Users followed by a specific User by their ID.
        
        
        
        
        Args:
            id: The ID of the User to lookup.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersfollowingResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/following"

        

        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
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
        
        return GetusersfollowingResponse.model_validate(response_data)
        
    
    def follow_user(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[FollowuserRequest] = None,
        
    ) -> FollowuserResponse:
        """
        Follow User
        
        
        Causes the authenticated user to follow a specific user by their ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that is requesting to follow the target User.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            FollowuserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/following"

        

        
        
        
        
        
        
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
        
        return FollowuserResponse.model_validate(response_data)
        
    
    def get_lists_followers(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetlistsfollowersResponse:
        """
        Get List followers
        
        
        Retrieves a list of Users who follow a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the List.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetlistsfollowersResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/followers"

        

        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
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
        
        return GetlistsfollowersResponse.model_validate(response_data)
        
    
    def get_lists_members(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetlistsmembersResponse:
        """
        Get List members
        
        
        Retrieves a list of Users who are members of a specific List by its ID.
        
        
        
        
        Args:
            id: The ID of the List.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetlistsmembersResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members"

        

        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
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
        
        return GetlistsmembersResponse.model_validate(response_data)
        
    
    def get_users_followers(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersfollowersResponse:
        """
        Get followers
        
        
        Retrieves a list of Users who follow a specific User by their ID.
        
        
        
        
        Args:
            id: The ID of the User to lookup.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersfollowersResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followers"

        

        
        
        
        
        
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
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
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
        
        return GetusersfollowersResponse.model_validate(response_data)
        
    
    def get_users_reposts_of_me(self, 
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> GetusersrepostsofmeResponse:
        """
        Get Reposts of me
        
        
        Retrieves a list of Posts that repost content from the authenticated user.
        
        
        
        
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
            GetusersrepostsofmeResponse: Response data
        """
        url = self.client.base_url + "/2/users/reposts_of_me"

        

        
        
        
        
        
        
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
        
        return GetusersrepostsofmeResponse.model_validate(response_data)
        
    
    def get_users_by_username(self, 
        
        
        
        username: str,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersbyusernameResponse:
        """
        Get User by username
        
        
        Retrieves details of a specific User by their username.
        
        
        
        
        Args:
            username: A username.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersbyusernameResponse: Response data
        """
        url = self.client.base_url + "/2/users/by/username/{username}"

        

        
        
        
        
        
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
        
        
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        url = url.replace("{username}", str(username))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return GetusersbyusernameResponse.model_validate(response_data)
        
    
    def get_users_muting(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> GetusersmutingResponse:
        """
        Get muting
        
        
        Retrieves a list of Users muted by the authenticated user.
        
        
        
        
        Args:
            id: The ID of the authenticated source User for whom to return results.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            GetusersmutingResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/muting"

        

        
        
        
        
        
        
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
        
        return GetusersmutingResponse.model_validate(response_data)
        
    
    def mute_user(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[MuteuserRequest] = None,
        
    ) -> MuteuserResponse:
        """
        Mute User
        
        
        Causes the authenticated user to mute a specific User by their ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that is requesting to mute the target User.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            MuteuserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/muting"

        

        
        
        
        
        
        
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
        
        return MuteuserResponse.model_validate(response_data)
        
    
    def unblock_users_dms(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> UnblockusersdmsResponse:
        """
        Unblock DMs
        
        
        Unblocks direct messages to or from a specific User by their ID for the authenticated user.
        
        
        
        
        Args:
            id: The ID of the target User that the authenticated user requesting to unblock dms for.
        
        
        
        
        Returns:
            UnblockusersdmsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/dm/unblock"

        

        
        
        
        
        
        
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
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return UnblockusersdmsResponse.model_validate(response_data)
        
    