"""
Media client for the X API.

This module provides a client for interacting with the Media endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_media_response, 2_media_analytics_response, 2_media_media_key_response

class MediaClient:
    """Client for Media operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def 2_media(self, 
        
        
        
        media_keys: List,
        
        
        
        
        
        
        
        media_fields: List = None,
        
        
        
        
    ) -> 2_media_response:
        """
        Get Media by media keys
        
        
        Retrieves details of Media files by their media keys.
        
        
        
        
        Args:
            media_keys: A comma separated list of Media Keys. Up to 100 are allowed in a single request.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        
        Returns:
            2_media_response: Response data
        """
        url = self.client.base_url + "/2/media"

        

        
        
        
        
        
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
        
        
        
        if media_keys is not None:
            
            params["media_keys"] = ",".join(str(item) for item in media_keys)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_media_response.model_validate(response_data)
        
    
    def 2_media_analytics(self, 
        
        
        
        media_keys: List,
        
        
        
        end_time: str,
        
        
        
        start_time: str,
        
        
        
        granularity: str,
        
        
        
        
        
        
        
        media_analytics_fields: List = None,
        
        
        
        
    ) -> 2_media_analytics_response:
        """
        Get Media analytics
        
        
        Retrieves analytics data for media.
        
        
        
        
        Args:
            media_keys: A comma separated list of Media Keys. Up to 100 are allowed in a single request.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
        
        
        
        Args:
            granularity: The granularity for the search counts results.
        
        
        
        Args:
            media_analytics_fields: A comma separated list of MediaAnalytics fields to display.
        
        
        
        
        Returns:
            2_media_analytics_response: Response data
        """
        url = self.client.base_url + "/2/media/analytics"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        if media_keys is not None:
            
            params["media_keys"] = ",".join(str(item) for item in media_keys)
            
        
        
        
        
        
        if end_time is not None:
            
            params["end_time"] = end_time
            
        
        
        
        
        
        if start_time is not None:
            
            params["start_time"] = start_time
            
        
        
        
        
        
        if granularity is not None:
            
            params["granularity"] = granularity
            
        
        
        
        
        
        if media_analytics_fields is not None:
            
            params["media_analytics.fields"] = ",".join(str(item) for item in media_analytics_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_media_analytics_response.model_validate(response_data)
        
    
    def 2_media_media_key(self, 
        
        
        
        media_key: str,
        
        
        
        
        
        
        
        media_fields: List = None,
        
        
        
        
    ) -> 2_media_media_key_response:
        """
        Get Media by media key
        
        
        Retrieves details of a specific Media file by its media key.
        
        
        
        
        Args:
            media_key: A single Media Key.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        
        Returns:
            2_media_media_key_response: Response data
        """
        url = self.client.base_url + "/2/media/{media_key}"

        

        
        
        
        
        
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
        
        
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        
        
        url = url.replace("{media_key}", str(media_key))
        
        
        
        
        
        
        
        
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
        
        return 2_media_media_key_response.model_validate(response_data)
        
    