"""
Community_Notes client for the X API.

This module provides a client for interacting with the Community_Notes endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_notes_request, 2_notes_response, 2_notes_search_notes_written_response, 2_notes_search_posts_eligible_for_notes_response, 2_notes_id_response

class Community_NotesClient:
    """Client for Community_Notes operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def create_note(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_notes_request] = None,
        
    ) -> 2_notes_response:
        """
        Create a Community Note
        
        
        Creates a community note endpoint for LLM use case.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_notes_response: Response data
        """
        url = self.client.base_url + "/2/notes"

        

        
        
        
        
        
        
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
        
        return 2_notes_response.model_validate(response_data)
        
    
    def search_notes_written(self, 
        
        
        
        test_mode: bool,
        
        
        
        
        
        
        
        pagination_token: str = None,
        
        
        
        max_results: int = None,
        
        
        
        note_fields: List = None,
        
        
        
        
    ) -> 2_notes_search_notes_written_response:
        """
        Search for Community Notes Written
        
        
        Returns all the community notes written by the user.
        
        
        
        
        Args:
            test_mode: If true, return the notes the caller wrote for the test. If false, return the notes the caller wrote on the product.
        
        
        
        Args:
            pagination_token: Pagination token to get next set of posts eligible for notes.
        
        
        
        Args:
            max_results: Max results to return.
        
        
        
        Args:
            note_fields: A comma separated list of Note fields to display.
        
        
        
        
        Returns:
            2_notes_search_notes_written_response: Response data
        """
        url = self.client.base_url + "/2/notes/search/notes_written"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        if test_mode is not None:
            
            params["test_mode"] = test_mode
            
        
        
        
        
        
        if pagination_token is not None:
            
            params["pagination_token"] = pagination_token
            
        
        
        
        
        
        if max_results is not None:
            
            params["max_results"] = max_results
            
        
        
        
        
        
        if note_fields is not None:
            
            params["note.fields"] = ",".join(str(item) for item in note_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_notes_search_notes_written_response.model_validate(response_data)
        
    
    def search_posts_eligible_for_notes(self, 
        
        
        
        test_mode: bool,
        
        
        
        
        
        
        
        pagination_token: str = None,
        
        
        
        max_results: int = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> 2_notes_search_posts_eligible_for_notes_response:
        """
        Search for Posts Eligible for Community Notes
        
        
        Returns all the posts that are eligible for community notes.
        
        
        
        
        Args:
            test_mode: If true, return a list of posts that are for the test. If false, return a list of posts that the bots can write proposed notes on the product.
        
        
        
        Args:
            pagination_token: Pagination token to get next set of posts eligible for notes.
        
        
        
        Args:
            max_results: Max results to return.
        
        
        
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
            2_notes_search_posts_eligible_for_notes_response: Response data
        """
        url = self.client.base_url + "/2/notes/search/posts_eligible_for_notes"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        if test_mode is not None:
            
            params["test_mode"] = test_mode
            
        
        
        
        
        
        if pagination_token is not None:
            
            params["pagination_token"] = pagination_token
            
        
        
        
        
        
        if max_results is not None:
            
            params["max_results"] = max_results
            
        
        
        
        
        
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
        
        return 2_notes_search_posts_eligible_for_notes_response.model_validate(response_data)
        
    
    def delete_note(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> 2_notes_id_response:
        """
        Delete a Community Note
        
        
        Deletes a community note.
        
        
        
        
        Args:
            id: The community note id to delete.
        
        
        
        
        Returns:
            2_notes_id_response: Response data
        """
        url = self.client.base_url + "/2/notes/{id}"

        

        
        
        
        
        
        
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
        
        return 2_notes_id_response.model_validate(response_data)
        
    