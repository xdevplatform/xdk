"""
General client for the X API.

This module provides a client for interacting with the General endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_openapi_json_response, 2_tweets_search_stream_rules_counts_response

class GeneralClient:
    """Client for General operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def 2_openapi_json(self, 
        
        
        
        
        
        
        
        
    ) -> 2_openapi_json_response:
        """
        Returns the OpenAPI Specification document.
        
        
        Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
        
        
        
        
        
        Returns:
            2_openapi_json_response: Response data
        """
        url = self.client.base_url + "/2/openapi.json"

        

        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        # Make the request
        
        # This should only happend for the /2/openapi.json route
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
        
        return 2_openapi_json_response.model_validate(response_data)
        
    
    def 2_tweets_search_stream_rules_counts(self, 
        
        
        
        
        
        
        
        rules_count_fields: List = None,
        
        
        
        
    ) -> 2_tweets_search_stream_rules_counts_response:
        """
        Get stream rule counts
        
        
        Retrieves the count of rules in the active rule set for the filtered stream.
        
        
        
        
        Args:
            rules_count_fields: A comma separated list of RulesCount fields to display.
        
        
        
        
        Returns:
            2_tweets_search_stream_rules_counts_response: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules/counts"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        if rules_count_fields is not None:
            
            params["rules_count.fields"] = ",".join(str(item) for item in rules_count_fields)
            
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_tweets_search_stream_rules_counts_response.model_validate(response_data)
        
    