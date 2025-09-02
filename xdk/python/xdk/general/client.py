"""
Auto-generated general client for the X API.

This module provides a client for interacting with the general endpoints of the X API.

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
    GetOpenApiSpecResponse,
)


class GeneralClient:
    """Client for general operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_open_api_spec(
        self,
    ) -> GetOpenApiSpecResponse:
        """
        Get OpenAPI Spec.
        Retrieves the full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
        Returns:
            GetOpenApiSpecResponse: Response data
        """
        url = self.client.base_url + "/2/openapi.json"
        params = {}
        headers = {}
        # Prepare request data
        json_data = None
        # Make the request
        # This should only happen for the /2/openapi.json route
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
        return GetOpenApiSpecResponse.model_validate(response_data)
