"""
AAASubscriptions client for the X API.

This module provides a client for interacting with the AAASubscriptions endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_account_activity_replay_webhooks_webhook_id_subscriptions_all_response, 2_account_activity_webhooks_webhook_id_subscriptions_all_list_response, 2_account_activity_webhooks_webhook_id_subscriptions_all_response, 2_account_activity_webhooks_webhook_id_subscriptions_all_request, 2_account_activity_webhooks_webhook_id_subscriptions_all_response, 2_account_activity_webhooks_webhook_id_subscriptions_user_id_all_response, 2_account_activity_subscriptions_count_response

class AAASubscriptionsClient:
    """Client for AAASubscriptions operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def 2_account_activity_replay_webhooks_webhook_id_subscriptions_all(self, 
        
        
        
        webhook_id: str,
        
        
        
        from_date: str,
        
        
        
        to_date: str,
        
        
        
        
        
        
        
        
    ) -> 2_account_activity_replay_webhooks_webhook_id_subscriptions_all_response:
        """
        Create replay job
        
        
        Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.
        
        
        
        
        Args:
            webhook_id: The unique identifier for the webhook configuration.
        
        
        
        Args:
            from_date: The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format.
        
        
        
        Args:
            to_date: The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format.
        
        
        
        
        Returns:
            2_account_activity_replay_webhooks_webhook_id_subscriptions_all_response: Response data
        """
        url = self.client.base_url + "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        if from_date is not None:
            
            params["from_date"] = from_date
            
        
        
        
        
        
        if to_date is not None:
            
            params["to_date"] = to_date
            
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
        
        
        
        
        
        
        
        
        headers = {}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Make the request
        
        
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
        
        return 2_account_activity_replay_webhooks_webhook_id_subscriptions_all_response.model_validate(response_data)
        
    
    def 2_account_activity_webhooks_webhook_id_subscriptions_all_list(self, 
        
        
        
        webhook_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_account_activity_webhooks_webhook_id_subscriptions_all_list_response:
        """
        Get subscriptions
        
        
        Retrieves a list of all active subscriptions for a given webhook.
        
        
        
        
        Args:
            webhook_id: The webhook ID to pull subscriptions for.
        
        
        
        
        Returns:
            2_account_activity_webhooks_webhook_id_subscriptions_all_list_response: Response data
        """
        url = self.client.base_url + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
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
        
        return 2_account_activity_webhooks_webhook_id_subscriptions_all_list_response.model_validate(response_data)
        
    
    def 2_account_activity_webhooks_webhook_id_subscriptions_all(self, 
        
        
        
        webhook_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_account_activity_webhooks_webhook_id_subscriptions_all_response:
        """
        Validate subscription
        
        
        Checks a user’s Account Activity subscription for a given webhook.
        
        
        
        
        Args:
            webhook_id: The webhook ID to check subscription against.
        
        
        
        
        Returns:
            2_account_activity_webhooks_webhook_id_subscriptions_all_response: Response data
        """
        url = self.client.base_url + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
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
        
        return 2_account_activity_webhooks_webhook_id_subscriptions_all_response.model_validate(response_data)
        
    
    def 2_account_activity_webhooks_webhook_id_subscriptions_all(self, 
        
        
        
        webhook_id: str,
        
        
        
        
        
        
        
        
        body: Optional[2_account_activity_webhooks_webhook_id_subscriptions_all_request] = None,
        
    ) -> 2_account_activity_webhooks_webhook_id_subscriptions_all_response:
        """
        Create subscription
        
        
        Creates an Account Activity subscription for the user and the given webhook.
        
        
        
        
        Args:
            webhook_id: The webhook ID to check subscription against.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_account_activity_webhooks_webhook_id_subscriptions_all_response: Response data
        """
        url = self.client.base_url + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
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
        
        return 2_account_activity_webhooks_webhook_id_subscriptions_all_response.model_validate(response_data)
        
    
    def 2_account_activity_webhooks_webhook_id_subscriptions_user_id_all(self, 
        
        
        
        webhook_id: str,
        
        
        
        user_id: str,
        
        
        
        
        
        
        
        
    ) -> 2_account_activity_webhooks_webhook_id_subscriptions_user_id_all_response:
        """
        Delete subscription
        
        
        Deletes an Account Activity subscription for the given webhook and user ID.
        
        
        
        
        Args:
            webhook_id: The webhook ID to check subscription against.
        
        
        
        Args:
            user_id: User ID to unsubscribe from.
        
        
        
        
        Returns:
            2_account_activity_webhooks_webhook_id_subscriptions_user_id_all_response: Response data
        """
        url = self.client.base_url + "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        
        
        
        
        url = url.replace("{webhook_id}", str(webhook_id))
        
        
        
        
        
        url = url.replace("{user_id}", str(user_id))
        
        
        
        
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
        
        return 2_account_activity_webhooks_webhook_id_subscriptions_user_id_all_response.model_validate(response_data)
        
    
    def 2_account_activity_subscriptions_count(self, 
        
        
        
        
        
        
        
        
    ) -> 2_account_activity_subscriptions_count_response:
        """
        Get subscription count
        
        
        Retrieves a count of currently active Account Activity subscriptions.
        
        
        
        
        
        Returns:
            2_account_activity_subscriptions_count_response: Response data
        """
        url = self.client.base_url + "/2/account_activity/subscriptions/count"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        
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
        
        return 2_account_activity_subscriptions_count_response.model_validate(response_data)
        
    