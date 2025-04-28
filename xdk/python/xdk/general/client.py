"""
General client for the X API.

This module provides a client for interacting with the General endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import get_open_api_spec_response, get_rule_count_response


class GeneralClient:
    """Client for General operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_open_api_spec(
        self,
    ) -> get_open_api_spec_response:
        """
        Returns the OpenAPI Specification document.
        Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
        Returns:
            get_open_api_spec_response: Response data
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
        return get_open_api_spec_response.model_validate(response_data)


    def get_rule_count(
        self,
        rules_count_fields: List = None,
    ) -> get_rule_count_response:
        """
        Rules Count
        Returns the counts of rules from a User's active rule set, to reflect usage by project and application.
        Args:
            rules_count_fields: A comma separated list of RulesCount fields to display.
        Returns:
            get_rule_count_response: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules/counts"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if rules_count_fields is not None:
            params["rules_count.fields"] = ",".join(
                str(item) for item in rules_count_fields
            )
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
        return get_rule_count_response.model_validate(response_data)
