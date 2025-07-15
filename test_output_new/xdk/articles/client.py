"""
Articles client for the X API.

This module provides a client for interacting with the Articles endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_article_draft_request, 2_article_draft_response

class ArticlesClient:
    """Client for Articles operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def article_draft_create(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_article_draft_request] = None,
        
    ) -> 2_article_draft_response:
        """
        Create draft Article
        
        
        Creates a new Article draft.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_article_draft_response: Response data
        """
        url = self.client.base_url + "/2/article/draft"

        

        
        
        
        
        
        
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
        
        return 2_article_draft_response.model_validate(response_data)
        
    