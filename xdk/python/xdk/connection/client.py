"""
Connection client for the X API.

This module provides a client for interacting with the Connection endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class ConnectionClient:
    """Client for Connection operations"""


    def __init__(self, client: Client):
        self.client = client


    def kill_all_app_connections(self,
    ) -> Dict[str, Any]:
        """
        Force kills all streaming connections of the authenticated application.
        Force kills all streaming connections of the authenticated application.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/connections/all"
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
        # Return the response data
        return response.json()
