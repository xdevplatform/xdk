"""
Usage client for the X API.

This module provides a client for interacting with the Usage endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    
    
    GetusageResponse,
    
    
)

class UsageClient:
    """Client for Usage operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def get_usage(self, 
        
        
        
        
        
        
        
        days: int = None,
        
        
        
        usage_fields: List = None,
        
        
        
        
    ) -> GetusageResponse:
        """
        Get usage
        
        
        Retrieves usage statistics for Posts over a specified number of days.
        
        
        
        
        Args:
            days: The number of days for which you need usage for.
        
        
        
        Args:
            usage_fields: A comma separated list of Usage fields to display.
        
        
        
        
        Returns:
            GetusageResponse: Response data
        """
        url = self.client.base_url + "/2/usage/tweets"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        if days is not None:
            
            params["days"] = days
            
        
        
        
        
        
        if usage_fields is not None:
            
            params["usage.fields"] = ",".join(str(item) for item in usage_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return GetusageResponse.model_validate(response_data)
        
    