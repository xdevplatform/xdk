"""
General client for the X API.

This module provides a client for interacting with the General endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class GeneralClient:
    """Client for General operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_rule_count(self,
        rules_count_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Rules Count
        Returns the counts of rules from a User's active rule set, to reflect usage by project and application.
        Args:
            rules_count_fields: A comma separated list of RulesCount fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules/counts"
        params = {}
        if rules_count_fields is not None:
            params["rules_count.fields"] = rules_count_fields
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


    def get_open_api_spec(self,
    ) -> Dict[str, Any]:
        """
        Returns the OpenAPI Specification document.
        Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/openapi.json"
        params = {}
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
