"""
Community_Notes client for the X API.

This module provides a client for interacting with the Community_Notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class Community_NotesClient:
    """Client for Community_Notes operations"""


    def __init__(self, client: Client):
        self.client = client


    def find_note_by_tweet_id(self,
        post_id: str,
        note_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Community Note lookup by Post ID
        Returns a variety of information about the Community Noted specified by the requested Post ID.
        Args:
            post_id: A single Post ID.
        Args:
            note_fields: A comma separated list of Note fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/notes"
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
        # Return the response data
        return response.json()
