"""
Connection client for the X API.

This module provides a client for interacting with the Connection endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    DeleteAllConnectionsResponse,
)


class ConnectionClient:
    """Client for Connection operations"""


    def __init__(self, client: Client):
        self.client = client


    def delete_all_connections(
        self,
    ) -> DeleteAllConnectionsResponse:
        """
        Terminate all connections
        Terminates all active streaming connections for the authenticated application.
        Returns:
            DeleteAllConnectionsResponse: Response data
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
        return DeleteAllConnectionsResponse.model_validate(response_data)
