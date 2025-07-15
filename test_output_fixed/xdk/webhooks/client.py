"""
Webhooks client for the X API.

This module provides a client for interacting with the Webhooks endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_webhooks_response, 2_webhooks_request, 2_webhooks_response, 2_webhooks_webhook_id_response, 2_webhooks_webhook_id_response

class WebhooksClient:
    """Client for Webhooks operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def 2_webhooks(self, 
        
        
        
        
        
        
        
        webhook_config_fields: List = None,
        
        
        
        
    ) -> 2_webhooks_response:
        """
        Get webhook
        
        
        Get a list of webhook configs associated with a client app.
        
        
        
        
        Args:
            webhook_config_fields: A comma separated list of WebhookConfig fields to display.
        
        
        
        
        Returns:
            2_webhooks_response: Response data
        """
        url = self.client.base_url + "/2/webhooks"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        if webhook_config_fields is not None:
            
            params["webhook_config.fields"] = ",".join(str(item) for item in webhook_config_fields)
            
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_webhooks_response.model_validate(response_data)
        
    
    def 2_webhooks(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_webhooks_request] = None,
        
    ) -> 2_webhooks_response:
        """
        Create webhook
        
        
        Creates a new webhook configuration.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_webhooks_response: Response data
        """
        url = self.client.base_url + "/2/webhooks"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
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
        
        return 2_webhooks_response.model_validate(response_data)
        
    
    def 2_webhooks_webhook_id(self, 
        
        
        
        webhook_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_webhooks_webhook_id_response:
        """
        Validate webhook
        
        
        Triggers a CRC check for a given webhook.
        
        
        
        
        Args:
            webhook_id: The ID of the webhook to check.
        
        
        
        
        Returns:
            2_webhooks_webhook_id_response: Response data
        """
        url = self.client.base_url + "/2/webhooks/{webhook_id}"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
        headers = {}
        
        
        
        
        
        
        
        # Make the request
        
        
        response = self.client.session.put(
            url,
            params=params,
            headers=headers,
            
        )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_webhooks_webhook_id_response.model_validate(response_data)
        
    
    def 2_webhooks_webhook_id(self, 
        
        
        
        webhook_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_webhooks_webhook_id_response:
        """
        Delete webhook
        
        
        Deletes an existing webhook configuration.
        
        
        
        
        Args:
            webhook_id: The ID of the webhook to delete.
        
        
        
        
        Returns:
            2_webhooks_webhook_id_response: Response data
        """
        url = self.client.base_url + "/2/webhooks/{webhook_id}"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
        headers = {}
        
        
        
        
        
        
        
        # Make the request
        
        
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
        
        return 2_webhooks_webhook_id_response.model_validate(response_data)
        
    