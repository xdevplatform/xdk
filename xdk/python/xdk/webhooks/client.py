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
    CreateStreamLinkResponse,
    DeleteStreamLinkResponse,
    GetStreamLinksResponse,
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


    def create_stream_link(
        self,
        webhook_id: Any,
        tweetfields: str = None,
        expansions: str = None,
        mediafields: str = None,
        pollfields: str = None,
        userfields: str = None,
        placefields: str = None,
    ) -> CreateStreamLinkResponse:
        """
        Create stream link
        Creates a link to deliver FilteredStream events to the given webhook.
        Args:
            webhook_id: The webhook ID to link to your FilteredStream ruleset.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            CreateStreamLinkResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/webhooks/{webhook_id}"
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
        if tweetfields is not None:
            params["tweet.fields"] = tweetfields
        if expansions is not None:
            params["expansions"] = expansions
        if mediafields is not None:
            params["media.fields"] = mediafields
        if pollfields is not None:
            params["poll.fields"] = pollfields
        if userfields is not None:
            params["user.fields"] = userfields
        if placefields is not None:
            params["place.fields"] = placefields
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
        return CreateStreamLinkResponse.model_validate(response_data)


    def delete_stream_link(self, webhook_id: Any) -> DeleteStreamLinkResponse:
        """
        Delete stream link
        Deletes a link from FilteredStream events to the given webhook.
        Args:
            webhook_id: The webhook ID to link to your FilteredStream ruleset.
            Returns:
            DeleteStreamLinkResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/webhooks/{webhook_id}"
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
        return DeleteStreamLinkResponse.model_validate(response_data)


    def get_stream_links(
        self,
    ) -> GetStreamLinksResponse:
        """
        Get stream links
        Get a list of webhook links associated with a filtered stream ruleset.
        Returns:
            GetStreamLinksResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/webhooks"
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
        return GetStreamLinksResponse.model_validate(response_data)


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
