"""
Community_Notes client for the X API.

This module provides a client for interacting with the Community_Notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from ..client import Client
from .models import find_note_by_tweet_id_response


class Community_NotesClient:
    """Client for Community_Notes operations"""


    def __init__(self, client: Client):
        self.client = client


    def find_note_by_tweet_id(
        self,
        post_id: str,
        note_fields: List = None,
    ) -> find_note_by_tweet_id_response:
        """
        Community Note lookup by Post ID
        Returns a variety of information about the Community Noted specified by the requested Post ID.
        Args:
            post_id: A single Post ID.
        Args:
            note_fields: A comma separated list of Note fields to display.
        Returns:
            find_note_by_tweet_id_response: Response data
        """
        url = self.client.base_url + "/2/notes"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if post_id is not None:
            params["postId"] = post_id
        if note_fields is not None:
            params["note.fields"] = note_fields
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
        return find_note_by_tweet_id_response.model_validate(response_data)
