"""
Users client for the X API.

This module provides a client for interacting with the Users endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_users_me_response, 2_users_id_blocking_response, 2_users_id_blocking_request, 2_users_id_blocking_response, 2_users_by_response, 2_tweets_id_liking_users_response, 2_lists_id_members_response, 2_users_id_followers_response, 2_users_id_dm_block_response, 2_tweets_id_retweeted_by_response, 2_users_source_user_id_following_target_user_id_response, 2_users_search_response, 2_users_id_response, 2_users_id_following_response, 2_users_id_following_request, 2_users_id_following_response, 2_users_id_muting_response, 2_users_id_muting_request, 2_users_id_muting_response, 2_users_source_user_id_muting_target_user_id_response, 2_users_reposts_of_me_response, 2_users_by_username_username_response, 2_users_response, 2_users_id_dm_unblock_response, 2_lists_id_followers_response, 2_users_source_user_id_blocking_target_user_id_response

class UsersClient:
    """Client for Users operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def 2_users_me(self, 
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_me_response:
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
            2_users_me_response: Response data
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
        
        return 2_users_me_response.model_validate(response_data)
        
    
    def 2_users_id_blocking(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_id_blocking_response:
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
            2_users_id_blocking_response: Response data
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
        
        return 2_users_id_blocking_response.model_validate(response_data)
        
    
    def 2_users_id_blocking(self, 
        
        
        
        id: str,
        
        
        
        
        body: 2_users_id_blocking_request,
        
        
        
        
        
    ) -> 2_users_id_blocking_response:
        """
        Block User by User ID
        
        
        Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request
        
        
        
        
        Args:
            id: The ID of the authenticated source User that is requesting to block the target User.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_users_id_blocking_response: Response data
        """
        url = self.client.base_url + "/2/users/{id}/blocking"

        

        
        
        
        
        
        
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
        
        return 2_users_id_blocking_response.model_validate(response_data)
        
    
    def 2_users_by(self, 
        
        
        
        usernames: List,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_by_response:
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
            2_users_by_response: Response data
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
        
        return 2_users_by_response.model_validate(response_data)
        
    
    def 2_tweets_id_liking_users(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_tweets_id_liking_users_response:
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
            2_tweets_id_liking_users_response: Response data
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
        
        return 2_tweets_id_liking_users_response.model_validate(response_data)
        
    
    def 2_lists_id_members(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_lists_id_members_response:
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
            2_lists_id_members_response: Response data
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
        
        return 2_lists_id_members_response.model_validate(response_data)
        
    
    def 2_users_id_followers(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_id_followers_response:
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
            2_users_id_followers_response: Response data
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
        
        return 2_users_id_followers_response.model_validate(response_data)
        
    
    def 2_users_id_dm_block(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> 2_users_id_dm_block_response:
        """
        Block DMs
        
        
        Blocks direct messages to or from a specific User by their ID for the authenticated user.
        
        
        
        
        Args:
            id: The ID of the target User that the authenticated user requesting to block dms for.
        
        
        
        
        Returns:
            2_users_id_dm_block_response: Response data
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
        
        return 2_users_id_dm_block_response.model_validate(response_data)
        
    
    def 2_tweets_id_retweeted_by(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_tweets_id_retweeted_by_response:
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
            2_tweets_id_retweeted_by_response: Response data
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
        
        return 2_tweets_id_retweeted_by_response.model_validate(response_data)
        
    
    def 2_users_source_user_id_following_target_user_id(self, 
        
        
        
        source_user_id: str,
        
        
        
        target_user_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_users_source_user_id_following_target_user_id_response:
        """
        Unfollow User
        
        
        Causes the authenticated user to unfollow a specific user by their ID.
        
        
        
        
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unfollow the target User.
        
        
        
        Args:
            target_user_id: The ID of the User that the source User is requesting to unfollow.
        
        
        
        
        Returns:
            2_users_source_user_id_following_target_user_id_response: Response data
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
        
        return 2_users_source_user_id_following_target_user_id_response.model_validate(response_data)
        
    
    def 2_users_search(self, 
        
        
        
        query: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        next_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_search_response:
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
            2_users_search_response: Response data
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
        
        return 2_users_search_response.model_validate(response_data)
        
    
    def 2_users_id(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_id_response:
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
            2_users_id_response: Response data
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
        
        return 2_users_id_response.model_validate(response_data)
        
    
    def 2_users_id_following(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_id_following_response:
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
            2_users_id_following_response: Response data
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
        
        return 2_users_id_following_response.model_validate(response_data)
        
    
    def 2_users_id_following(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[2_users_id_following_request] = None,
        
    ) -> 2_users_id_following_response:
        """
        Follow User
        
        
        Causes the authenticated user to follow a specific user by their ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that is requesting to follow the target User.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_users_id_following_response: Response data
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
        
        return 2_users_id_following_response.model_validate(response_data)
        
    
    def 2_users_id_muting(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_id_muting_response:
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
            2_users_id_muting_response: Response data
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
        
        return 2_users_id_muting_response.model_validate(response_data)
        
    
    def 2_users_id_muting(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[2_users_id_muting_request] = None,
        
    ) -> 2_users_id_muting_response:
        """
        Mute User
        
        
        Causes the authenticated user to mute a specific User by their ID.
        
        
        
        
        Args:
            id: The ID of the authenticated source User that is requesting to mute the target User.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_users_id_muting_response: Response data
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
        
        return 2_users_id_muting_response.model_validate(response_data)
        
    
    def 2_users_source_user_id_muting_target_user_id(self, 
        
        
        
        source_user_id: str,
        
        
        
        target_user_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_users_source_user_id_muting_target_user_id_response:
        """
        Unmute User
        
        
        Causes the authenticated user to unmute a specific user by their ID.
        
        
        
        
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unmute the target User.
        
        
        
        Args:
            target_user_id: The ID of the User that the source User is requesting to unmute.
        
        
        
        
        Returns:
            2_users_source_user_id_muting_target_user_id_response: Response data
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
        
        return 2_users_source_user_id_muting_target_user_id_response.model_validate(response_data)
        
    
    def 2_users_reposts_of_me(self, 
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> 2_users_reposts_of_me_response:
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
            2_users_reposts_of_me_response: Response data
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
        
        return 2_users_reposts_of_me_response.model_validate(response_data)
        
    
    def 2_users_by_username_username(self, 
        
        
        
        username: str,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_by_username_username_response:
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
            2_users_by_username_username_response: Response data
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
        
        return 2_users_by_username_username_response.model_validate(response_data)
        
    
    def 2_users(self, 
        
        
        
        ids: List,
        
        
        
        
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_users_response:
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
            2_users_response: Response data
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
        
        return 2_users_response.model_validate(response_data)
        
    
    def 2_users_id_dm_unblock(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> 2_users_id_dm_unblock_response:
        """
        Unblock DMs
        
        
        Unblocks direct messages to or from a specific User by their ID for the authenticated user.
        
        
        
        
        Args:
            id: The ID of the target User that the authenticated user requesting to unblock dms for.
        
        
        
        
        Returns:
            2_users_id_dm_unblock_response: Response data
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
        
        return 2_users_id_dm_unblock_response.model_validate(response_data)
        
    
    def 2_lists_id_followers(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        user_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> 2_lists_id_followers_response:
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
            2_lists_id_followers_response: Response data
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
        
        return 2_lists_id_followers_response.model_validate(response_data)
        
    
    def 2_users_source_user_id_blocking_target_user_id(self, 
        
        
        
        source_user_id: str,
        
        
        
        target_user_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_users_source_user_id_blocking_target_user_id_response:
        """
        Unblock User by User ID
        
        
        Causes the source User to unblock the target User. The source User must match the User context authorizing the request
        
        
        
        
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unblock the target User.
        
        
        
        Args:
            target_user_id: The ID of the User that the source User is requesting to unblock.
        
        
        
        
        Returns:
            2_users_source_user_id_blocking_target_user_id_response: Response data
        """
        url = self.client.base_url + "/2/users/{source_user_id}/blocking/{target_user_id}"

        

        
        
        
        
        
        
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
        
        return 2_users_source_user_id_blocking_target_user_id_response.model_validate(response_data)
        
    