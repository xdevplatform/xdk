"""
trends client for the X API.

This module provides a client for interacting with the trends endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    GetPersonalizedResponse,
    GetByWoeidResponse,
)


class TrendsClient:
    """Client for trends operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_personalized(
        self,
    ) -> GetPersonalizedResponse:
        """
        Get personalized Trends
        Retrieves personalized trending topics for the authenticated user.
        Returns:
            GetPersonalizedResponse: Response data
        """
        url = self.client.base_url + "/2/users/personalized_trends"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
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
        return GetPersonalizedResponse.model_validate(response_data)


    def get_by_woeid(
        self,
        woeid: int,
        max_trends: int = None,
    ) -> GetByWoeidResponse:
        """
        Get Trends by WOEID
        Retrieves trending topics for a specific location identified by its WOEID.
        Args:
            woeid: The WOEID of the place to lookup a trend for.
        Args:
            max_trends: The maximum number of results.
        Returns:
            GetByWoeidResponse: Response data
        """
        url = self.client.base_url + "/2/trends/by/woeid/{woeid}"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if max_trends is not None:
            params["max_trends"] = max_trends
        url = url.replace("{woeid}", str(woeid))
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
        return GetByWoeidResponse.model_validate(response_data)
