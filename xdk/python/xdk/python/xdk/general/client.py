"""
General client for the X API.

This module provides a client for interacting with the General endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    GetopenapispecResponse,
)


class GeneralClient:
    """Client for General operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_open_api_spec(
        self,
    ) -> GetopenapispecResponse:
        """
        Get OpenAPI Spec.
        Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
        Returns:
            GetopenapispecResponse: Response data
        """
        url = self.client.base_url + "/2/openapi.json"
        params = {}
        headers = {}
        # Make the request
        # This should only happend for the /2/openapi.json route
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
        return GetopenapispecResponse.model_validate(response_data)
