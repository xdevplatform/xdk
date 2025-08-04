"""
Account_Activity client for the X API.

This module provides a client for interacting with the Account_Activity endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import (
    GetAccountActivitySubscriptionCountResponse,
    ValidateAccountActivitySubscriptionResponse,
    DeleteAccountActivitySubscriptionResponse,
    GetAccountActivitySubscriptionsResponse,
    CreateAccountActivityReplayJobResponse,
)


class Account_ActivityClient:
    """Client for Account_Activity operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_account_activity_subscription_count(
        self,
    ) -> GetAccountActivitySubscriptionCountResponse:
        """
        Get subscription count
        Retrieves a count of currently active Account Activity subscriptions.
        Returns:
            GetAccountActivitySubscriptionCountResponse: Response data
        """
        url = self.client.base_url + "/2/account_activity/subscriptions/count"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
        return GetAccountActivitySubscriptionCountResponse.model_validate(response_data)


    def validate_account_activity_subscription(
        self,
        webhook_id: str,
    ) -> ValidateAccountActivitySubscriptionResponse:
        """
        Validate subscription
        Checks a user’s Account Activity subscription for a given webhook.
        Args:
            webhook_id: The webhook ID to check subscription against.
        Returns:
            ValidateAccountActivitySubscriptionResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"
        )
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
        return ValidateAccountActivitySubscriptionResponse.model_validate(response_data)


    def delete_account_activity_subscription(
        self,
        webhook_id: str,
        user_id: str,
    ) -> DeleteAccountActivitySubscriptionResponse:
        """
        Delete subscription
        Deletes an Account Activity subscription for the given webhook and user ID.
        Args:
            webhook_id: The webhook ID to check subscription against.
        Args:
            user_id: User ID to unsubscribe from.
        Returns:
            DeleteAccountActivitySubscriptionResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all"
        )
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
        return DeleteAccountActivitySubscriptionResponse.model_validate(response_data)


    def get_account_activity_subscriptions(
        self,
        webhook_id: str,
    ) -> GetAccountActivitySubscriptionsResponse:
        """
        Get subscriptions
        Retrieves a list of all active subscriptions for a given webhook.
        Args:
            webhook_id: The webhook ID to pull subscriptions for.
        Returns:
            GetAccountActivitySubscriptionsResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list"
        )
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
        return GetAccountActivitySubscriptionsResponse.model_validate(response_data)


    def create_account_activity_replay_job(
        self,
        webhook_id: str,
        from_date: str,
        to_date: str,
    ) -> CreateAccountActivityReplayJobResponse:
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
            CreateAccountActivityReplayJobResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all"
        )
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
        return CreateAccountActivityReplayJobResponse.model_validate(response_data)
