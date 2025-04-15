"""
Trends client for the X API.

This module provides a client for interacting with the Trends endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class TrendsClient:
    """Client for Trends operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_trends(self,
        woeid: int,
        max_trends: int = None,
        trend_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/trends/by/woeid/{woeid}"
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
        # Return the response data
        return response.json()


    def personalized_trends(self,
        personalized_trend_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Get personalized Trends
        Returns Personalized trends for the authenticated user
        Args:
            personalized_trend_fields: A comma separated list of PersonalizedTrend fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/personalized_trends"
        params = {}
        if personalized_trend_fields is not None:
            params["personalized_trend.fields"] = personalized_trend_fields
        headers = {}
        # Make the request
        response = self.client.session.get(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()
