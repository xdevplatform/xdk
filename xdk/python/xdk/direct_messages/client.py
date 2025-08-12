"""
direct messages client for the X API.

This module provides a client for interacting with the direct messages endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    GetDmEventsByParticipantIdResponse,
    CreateDmByParticipantIdRequest,
    CreateDmByParticipantIdResponse,
    CreateDmByConversationIdRequest,
    CreateDmByConversationIdResponse,
    CreateDmConversationsRequest,
    CreateDmConversationsResponse,
    GetEventsResponse,
    GetDmConversationsIdDmEventsResponse,
    GetEventsByIdResponse,
    DeleteDmEventsResponse,
)


class DirectMessagesClient:
    """Client for direct messages operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_dm_events_by_participant_id(
        self,
        participant_id: str,
        max_results: int = None,
        pagination_token: str = None,
        event_types: List = None,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> GetDmEventsByParticipantIdResponse:
        """
        Get DM events for a DM conversation
        Retrieves direct message events for a specific conversation.
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
            GetDmEventsByParticipantIdResponse: Response data
        """
        url = (
            self.client.base_url + "/2/dm_conversations/with/{participant_id}/dm_events"
        )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if event_types is not None:
            params["event_types"] = ",".join(str(item) for item in event_types)
        if dm_event_fields is not None:
            params["dm_event.fields"] = ",".join(str(item) for item in dm_event_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
        url = url.replace("{participant_id}", str(participant_id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
            )
        else:
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
        return GetDmEventsByParticipantIdResponse.model_validate(response_data)


    def create_dm_by_participant_id(
        self,
        participant_id: str,
        body: Optional[CreateDmByParticipantIdRequest] = None,
    ) -> Dict[str, Any]:
        """
        Create DM message by participant ID
        Sends a new direct message to a specific participant by their ID.
        Args:
            participant_id: The ID of the recipient user that will receive the DM.
            body: Request body
        Returns:
            CreateDmByParticipantIdResponse: Response data
        """
        url = (
            self.client.base_url + "/2/dm_conversations/with/{participant_id}/messages"
        )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{participant_id}", str(participant_id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateDmByParticipantIdResponse.model_validate(response_data)


    def create_dm_by_conversation_id(
        self,
        dm_conversation_id: str,
        body: Optional[CreateDmByConversationIdRequest] = None,
    ) -> Dict[str, Any]:
        """
        Create DM message by conversation ID
        Sends a new direct message to a specific conversation by its ID.
        Args:
            dm_conversation_id: The DM Conversation ID.
            body: Request body
        Returns:
            CreateDmByConversationIdResponse: Response data
        """
        url = self.client.base_url + "/2/dm_conversations/{dm_conversation_id}/messages"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{dm_conversation_id}", str(dm_conversation_id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateDmByConversationIdResponse.model_validate(response_data)


    def create_dm_conversations(
        self,
        body: Optional[CreateDmConversationsRequest] = None,
    ) -> Dict[str, Any]:
        """
        Create DM conversation
        Initiates a new direct message conversation with specified participants.
            body: Request body
        Returns:
            CreateDmConversationsResponse: Response data
        """
        url = self.client.base_url + "/2/dm_conversations"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateDmConversationsResponse.model_validate(response_data)


    def get_events(
        self,
        max_results: int = None,
        pagination_token: str = None,
        event_types: List = None,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> GetEventsResponse:
        """
        Get DM events
        Retrieves a list of recent direct message events across all conversations.
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
            GetEventsResponse: Response data
        """
        url = self.client.base_url + "/2/dm_events"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if event_types is not None:
            params["event_types"] = ",".join(str(item) for item in event_types)
        if dm_event_fields is not None:
            params["dm_event.fields"] = ",".join(str(item) for item in dm_event_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
            )
        else:
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
        return GetEventsResponse.model_validate(response_data)


    def get_dm_conversations_id_dm_events(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        event_types: List = None,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> GetDmConversationsIdDmEventsResponse:
        """
        Get DM events for a DM conversation
        Retrieves direct message events for a specific conversation.
        Args:
            id: The DM conversation ID.
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
            GetDmConversationsIdDmEventsResponse: Response data
        """
        url = self.client.base_url + "/2/dm_conversations/{id}/dm_events"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if event_types is not None:
            params["event_types"] = ",".join(str(item) for item in event_types)
        if dm_event_fields is not None:
            params["dm_event.fields"] = ",".join(str(item) for item in dm_event_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
            )
        else:
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
        return GetDmConversationsIdDmEventsResponse.model_validate(response_data)


    def get_events_by_id(
        self,
        event_id: str,
        dm_event_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> GetEventsByIdResponse:
        """
        Get DM event by ID
        Retrieves details of a specific direct message event by its ID.
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
            GetEventsByIdResponse: Response data
        """
        url = self.client.base_url + "/2/dm_events/{event_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if dm_event_fields is not None:
            params["dm_event.fields"] = ",".join(str(item) for item in dm_event_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
        url = url.replace("{event_id}", str(event_id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
            )
        else:
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
        return GetEventsByIdResponse.model_validate(response_data)


    def delete_dm_events(
        self,
        event_id: str,
    ) -> DeleteDmEventsResponse:
        """
        Delete DM event
        Deletes a specific direct message event by its ID, if owned by the authenticated user.
        Args:
            event_id: The ID of the direct-message event to delete.
        Returns:
            DeleteDmEventsResponse: Response data
        """
        url = self.client.base_url + "/2/dm_events/{event_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{event_id}", str(event_id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
            )
        else:
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
        return DeleteDmEventsResponse.model_validate(response_data)
