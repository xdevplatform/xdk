"""
Auto-generated usage client for the X API.

This module provides a client for interacting with the usage endpoints of the X API.

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
)


class UsageClient:
    """Client for usage operations"""


    def __init__(self, client: Client):
        self.client = client


    def get(self, days: int = None) -> GetResponse:
        """
        Get usage
        Retrieves usage statistics for Posts over a specified number of days.
        Args:
            days: The number of days for which you need usage for.
            Returns:
            GetResponse: Response data
        """
        url = self.client.base_url + "/2/usage/tweets"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if days is not None:
            params["days"] = days
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
