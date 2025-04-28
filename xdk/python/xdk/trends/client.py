"""
Trends client for the X API.

This module provides a client for interacting with the Trends endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from ..client import Client
from .models import personalized_trends_response, get_trends_response


class TrendsClient:
    """Client for Trends operations"""


    def __init__(self, client: Client):
        self.client = client


    def personalized_trends(
        self,
        personalized_trend_fields: List = None,
    ) -> personalized_trends_response:
        """
        Get personalized Trends
        Returns Personalized trends for the authenticated user
        Args:
            personalized_trend_fields: A comma separated list of PersonalizedTrend fields to display.
        Returns:
            personalized_trends_response: Response data
        """
        url = self.client.base_url + "/2/users/personalized_trends"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if personalized_trend_fields is not None:
            params["personalized_trend.fields"] = personalized_trend_fields
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
        return personalized_trends_response.model_validate(response_data)


    def get_trends(
        self,
        woeid: int,
        max_trends: int = None,
        trend_fields: List = None,
    ) -> get_trends_response:
        """
        Trends
        Returns the Trend associated with the supplied WoeId.
        Args:
            woeid: The WOEID of the place to lookup a trend for.
        Args:
            max_trends: The maximum number of results.
        Args:
            trend_fields: A comma separated list of Trend fields to display.
        Returns:
            get_trends_response: Response data
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
        if trend_fields is not None:
            params["trend.fields"] = trend_fields
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
        return get_trends_response.model_validate(response_data)
