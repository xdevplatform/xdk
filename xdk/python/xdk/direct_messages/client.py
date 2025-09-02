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
    GetEventsResponse,
    CreateByParticipantIdRequest,
    CreateByParticipantIdResponse,
    GetEventsByParticipantIdResponse,
    GetEventsByConversationIdResponse,
    GetEventsByIdResponse,
    DeleteEventsResponse,
    CreateByConversationIdRequest,
    CreateByConversationIdResponse,
    CreateConversationRequest,
    CreateConversationResponse,
)


class DirectMessagesClient:
    """Client for direct messages operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_events(
        self,
        max_results: int = None,
        pagination_token: Any = None,
        event_types: List = None,
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


    def create_by_participant_id(
        self,
        participant_id: Any,
        body: Optional[CreateByParticipantIdRequest] = None,
    ) -> Dict[str, Any]:
        """
        Create DM message by participant ID
        Sends a new direct message to a specific participant by their ID.
        Args:
            participant_id: The ID of the recipient user that will receive the DM.
            body: Request body
        Returns:
            CreateByParticipantIdResponse: Response data
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
        return CreateByParticipantIdResponse.model_validate(response_data)


    def get_events_by_participant_id(
        self,
        participant_id: Any,
        max_results: int = None,
        pagination_token: Any = None,
        event_types: List = None,
    ) -> GetEventsByParticipantIdResponse:
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
        Returns:
            GetEventsByParticipantIdResponse: Response data
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
        return GetEventsByParticipantIdResponse.model_validate(response_data)


    def get_events_by_conversation_id(
        self,
        id: Any,
        max_results: int = None,
        pagination_token: Any = None,
        event_types: List = None,
    ) -> GetEventsByConversationIdResponse:
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
        Returns:
            GetEventsByConversationIdResponse: Response data
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
        return GetEventsByConversationIdResponse.model_validate(response_data)


    def get_events_by_id(
        self,
        event_id: Any,
    ) -> GetEventsByIdResponse:
        """
        Get DM event by ID
        Retrieves details of a specific direct message event by its ID.
        Args:
            event_id: dm event id.
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


    def delete_events(
        self,
        event_id: Any,
    ) -> DeleteEventsResponse:
        """
        Delete DM event
        Deletes a specific direct message event by its ID, if owned by the authenticated user.
        Args:
            event_id: The ID of the direct-message event to delete.
        Returns:
            DeleteEventsResponse: Response data
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
        return DeleteEventsResponse.model_validate(response_data)


    def create_by_conversation_id(
        self,
        dm_conversation_id: str,
        body: Optional[CreateByConversationIdRequest] = None,
    ) -> Dict[str, Any]:
        """
        Create DM message by conversation ID
        Sends a new direct message to a specific conversation by its ID.
        Args:
            dm_conversation_id: The DM Conversation ID.
            body: Request body
        Returns:
            CreateByConversationIdResponse: Response data
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
        return CreateByConversationIdResponse.model_validate(response_data)


    def create_conversation(
        self,
        body: Optional[CreateConversationRequest] = None,
    ) -> Dict[str, Any]:
        """
        Create DM conversation
        Initiates a new direct message conversation with specified participants.
            body: Request body
        Returns:
            CreateConversationResponse: Response data
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
        return CreateConversationResponse.model_validate(response_data)
