"""
AAASubscriptions client for the X API.

This module provides a client for interacting with the AAASubscriptions endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    CreateaccountactivitysubscriptionRequest,
    CreateaccountactivitysubscriptionResponse,
)


class AaasubscriptionsClient:
    """Client for AAASubscriptions operations"""

    def __init__(self, client: Client):
        self.client = client

    def create_account_activity_subscription(
        self,
        webhook_id: str,
        body: Optional[CreateaccountactivitysubscriptionRequest] = None,
    ) -> CreateaccountactivitysubscriptionResponse:
        """
        Create subscription


        Creates an Account Activity subscription for the user and the given webhook.




        Args:
            webhook_id: The webhook ID to check subscription against.







            body: Request body




        Returns:
            CreateaccountactivitysubscriptionResponse: Response data
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

        return CreateaccountactivitysubscriptionResponse.model_validate(response_data)
