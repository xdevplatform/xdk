"""
Usage client for the X API.

This module provides a client for interacting with the Usage endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class UsageClient:
    """Client for Usage operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_usage_tweets(self,
        days: int = None,
        usage_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Post Usage
        Returns the Post Usage.
        Args:
            days: The number of days for which you need usage for.
        Args:
            usage_fields: A comma separated list of Usage fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/usage/tweets"
        params = {}
        if days is not None:
            params["days"] = days
        if usage_fields is not None:
            params["usage.fields"] = usage_fields
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
