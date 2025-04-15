"""
Direct_Messages client for the X API.

This module provides a client for interacting with the Direct_Messages endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class Direct_MessagesClient:
    """Client for Direct_Messages operations"""


    def __init__(self, client: Client):
        self.client = client


    def dm_conversation_id_create(self,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Create a new DM Conversation
        Creates a new DM Conversation.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_conversations"
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def dm_conversation_with_user_event_id_create(self,
        participant_id: str,
        body: Any = None,
    ) -> Dict[str, Any]:
        """
        Send a new message to a user
        Creates a new message for a DM Conversation with a participant user by ID
        Args:
            participant_id: The ID of the recipient user that will receive the DM.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_conversations/with/{participant_id}/messages"
        params = {}
        url = url.replace("{participant_id}", str(participant_id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def get_dm_conversations_with_participant_id_dm_events(self,
        participant_id: str,
        max_results: int = None,
        pagination_token: str = None,
        event_types: List = None,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Get DM Events for a DM Conversation
        Returns DM Events for a DM Conversation
        Args:
            participant_id: The ID of the participant user for the One to One DM conversation.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            event_types: The set of event_types to include in the results.
        Args:
            dm_event_fields: A comma separated list of DmEvent fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_conversations/with/{participant_id}/dm_events"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if event_types is not None:
            params["event_types"] = event_types
        if dm_event_fields is not None:
            params["dm_event.fields"] = dm_event_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        url = url.replace("{participant_id}", str(participant_id))
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


    def get_dm_events_by_id(self,
        event_id: str,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Get DM Events by id
        Returns DM Events by event id.
        Args:
            event_id: dm event id.
        Args:
            dm_event_fields: A comma separated list of DmEvent fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_events/{event_id}"
        params = {}
        if dm_event_fields is not None:
            params["dm_event.fields"] = dm_event_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        url = url.replace("{event_id}", str(event_id))
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


    def dm_event_delete(self,
        event_id: str,
    ) -> Dict[str, Any]:
        """
        Delete Dm
        Delete a Dm Event that you own.
        Args:
            event_id: The ID of the direct-message event to delete.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_events/{event_id}"
        params = {}
        url = url.replace("{event_id}", str(event_id))
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


    def dm_conversation_by_id_event_id_create(self,
        dm_conversation_id: str,
        body: Any = None,
    ) -> Dict[str, Any]:
        """
        Send a new message to a DM Conversation
        Creates a new message for a DM Conversation specified by DM Conversation ID
        Args:
            dm_conversation_id: The DM Conversation ID.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_conversations/{dm_conversation_id}/messages"
        params = {}
        url = url.replace("{dm_conversation_id}", str(dm_conversation_id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def get_dm_events(self,
        max_results: int = None,
        pagination_token: str = None,
        event_types: List = None,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Get recent DM Events
        Returns recent DM Events across DM conversations
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            event_types: The set of event_types to include in the results.
        Args:
            dm_event_fields: A comma separated list of DmEvent fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_events"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if event_types is not None:
            params["event_types"] = event_types
        if dm_event_fields is not None:
            params["dm_event.fields"] = dm_event_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
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


    def get_dm_conversations_id_dm_events(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        event_types: List = None,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Get DM Events for a DM Conversation
        Returns DM Events for a DM Conversation
        Args:
            id: The DM Conversation ID.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            event_types: The set of event_types to include in the results.
        Args:
            dm_event_fields: A comma separated list of DmEvent fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/dm_conversations/{id}/dm_events"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if event_types is not None:
            params["event_types"] = event_types
        if dm_event_fields is not None:
            params["dm_event.fields"] = dm_event_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        url = url.replace("{id}", str(id))
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
