"""
Auto-generated webhooks client for the X API.

This module provides a client for interacting with the webhooks endpoints of the X API.

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
    GetResponse,
    CreateRequest,
    CreateResponse,
    ValidateResponse,
    DeleteResponse,
)


class WebhooksClient:
    """Client for webhooks operations"""


    def __init__(self, client: Client):
        self.client = client


    def get(
        self,
    ) -> GetResponse:
        """
        Get webhook
        Get a list of webhook configs associated with a client app.
        Returns:
            GetResponse: Response data
        """
        url = self.client.base_url + "/2/webhooks"
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
        return GetResponse.model_validate(response_data)


    def create(self, body: Optional[CreateRequest] = None) -> CreateResponse:
        """
        Create webhook
        Creates a new webhook configuration.
        body: Request body
        Returns:
            CreateResponse: Response data
        """
        url = self.client.base_url + "/2/webhooks"
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
        return CreateResponse.model_validate(response_data)


    def validate(self, webhook_id: Any) -> ValidateResponse:
        """
        Validate webhook
        Triggers a CRC check for a given webhook.
        Args:
            webhook_id: The ID of the webhook to check.
            Returns:
            ValidateResponse: Response data
        """
        url = self.client.base_url + "/2/webhooks/{webhook_id}"
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
        return ValidateResponse.model_validate(response_data)


    def delete(self, webhook_id: Any) -> DeleteResponse:
        """
        Delete webhook
        Deletes an existing webhook configuration.
        Args:
            webhook_id: The ID of the webhook to delete.
            Returns:
            DeleteResponse: Response data
        """
        url = self.client.base_url + "/2/webhooks/{webhook_id}"
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
        return DeleteResponse.model_validate(response_data)
