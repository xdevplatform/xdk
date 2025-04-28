"""
Connection client for the X API.

This module provides a client for interacting with the Connection endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from ..client import Client
from .models import kill_all_app_connections_response


class ConnectionClient:
    """Client for Connection operations"""


    def __init__(self, client: Client):
        self.client = client


    def kill_all_app_connections(
        self,
    ) -> kill_all_app_connections_response:
        """
        Force kills all streaming connections of the authenticated application.
        Force kills all streaming connections of the authenticated application.
        Returns:
            kill_all_app_connections_response: Response data
        """
        url = self.client.base_url + "/2/connections/all"
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
        return kill_all_app_connections_response.model_validate(response_data)
