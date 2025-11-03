"""
Auto-generated account activity client for the X API.

This module provides a client for interacting with the account activity endpoints of the X API.

All methods, parameters, and response models are generated from the OpenAPI specification.

Generated automatically - do not edit manually.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time


if TYPE_CHECKING:
    from ..client import Client
from .models import (
    ValidateSubscriptionResponse,
    CreateSubscriptionRequest,
    CreateSubscriptionResponse,
    CreateReplayJobResponse,
    GetSubscriptionCountResponse,
    DeleteSubscriptionResponse,
    GetSubscriptionsResponse,
)


class AccountActivityClient:
    """Client for account activity operations"""


    def __init__(self, client: Client):
        self.client = client


    def validate_subscription(self, webhook_id: Any) -> ValidateSubscriptionResponse:
        """
        Validate subscription
        Checks a user’s Account Activity subscription for a given webhook.
        Args:
            webhook_id: The webhook ID to check subscription against.
            Returns:
            ValidateSubscriptionResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"
        )
        url = url.replace("{webhook_id}", str(webhook_id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        # Prepare request data
        json_data = None
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
        return ValidateSubscriptionResponse.model_validate(response_data)


    def create_subscription(
        self, webhook_id: Any, body: Optional[CreateSubscriptionRequest] = None
    ) -> CreateSubscriptionResponse:
        """
        Create subscription
        Creates an Account Activity subscription for the user and the given webhook.
        Args:
            webhook_id: The webhook ID to check subscription against.
            body: Request body
        Returns:
            CreateSubscriptionResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all"
        )
        url = url.replace("{webhook_id}", str(webhook_id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateSubscriptionResponse.model_validate(response_data)


    def create_replay_job(
        self, webhook_id: Any, from_date: str, to_date: str
    ) -> CreateReplayJobResponse:
        """
        Create replay job
        Creates a replay job to retrieve activities from up to the past 5 days for all subscriptions associated with a given webhook.
        Args:
            webhook_id: The unique identifier for the webhook configuration.
            from_date: The oldest (starting) UTC timestamp (inclusive) from which events will be provided, in `yyyymmddhhmm` format.
            to_date: The latest (ending) UTC timestamp (exclusive) up to which events will be provided, in `yyyymmddhhmm` format.
            Returns:
            CreateReplayJobResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/replay/webhooks/{webhook_id}/subscriptions/all"
        )
        url = url.replace("{webhook_id}", str(webhook_id))
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
        headers = {}
        # Prepare request data
        json_data = None
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
        return CreateReplayJobResponse.model_validate(response_data)


    def get_subscription_count(
        self,
    ) -> GetSubscriptionCountResponse:
        """
        Get subscription count
        Retrieves a count of currently active Account Activity subscriptions.
        Returns:
            GetSubscriptionCountResponse: Response data
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
        # Prepare request data
        json_data = None
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
        return GetSubscriptionCountResponse.model_validate(response_data)


    def delete_subscription(
        self, webhook_id: Any, user_id: Any
    ) -> DeleteSubscriptionResponse:
        """
        Delete subscription
        Deletes an Account Activity subscription for the given webhook and user ID.
        Args:
            webhook_id: The webhook ID to check subscription against.
            user_id: User ID to unsubscribe from.
            Returns:
            DeleteSubscriptionResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/{user_id}/all"
        )
        url = url.replace("{webhook_id}", str(webhook_id))
        url = url.replace("{user_id}", str(user_id))
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
        # Prepare request data
        json_data = None
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
        return DeleteSubscriptionResponse.model_validate(response_data)


    def get_subscriptions(self, webhook_id: Any) -> GetSubscriptionsResponse:
        """
        Get subscriptions
        Retrieves a list of all active subscriptions for a given webhook.
        Args:
            webhook_id: The webhook ID to pull subscriptions for.
            Returns:
            GetSubscriptionsResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/account_activity/webhooks/{webhook_id}/subscriptions/all/list"
        )
        url = url.replace("{webhook_id}", str(webhook_id))
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
        # Prepare request data
        json_data = None
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
        return GetSubscriptionsResponse.model_validate(response_data)
