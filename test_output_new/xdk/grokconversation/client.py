"""
GrokConversation client for the X API.

This module provides a client for interacting with the GrokConversation endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_get_grok_conversation_events_response

class GrokConversationClient:
    """Client for GrokConversation operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def get_grok_conversation_events_a_p_i(self, 
        
        
        
        
        
        
        
        grok_conversation_fields: List = None,
        
        
        
        
    ) -> 2_get_grok_conversation_events_response:
        """
        Get Grok conversation events
        
        
        Get Grok conversation events
        
        
        
        
        Args:
            grok_conversation_fields: A comma separated list of GrokConversation fields to display.
        
        
        
        
        Returns:
            2_get_grok_conversation_events_response: Response data
        """
        url = self.client.base_url + "/2/get_grok_conversation_events"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        if grok_conversation_fields is not None:
            
            params["grok_conversation.fields"] = ",".join(str(item) for item in grok_conversation_fields)
            
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_get_grok_conversation_events_response.model_validate(response_data)
        
    