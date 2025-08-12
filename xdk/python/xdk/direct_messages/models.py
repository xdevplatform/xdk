"""
direct messages models for the X API.

This module provides models for the direct messages endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_dm_events_by_participant_id


class GetDmEventsByParticipantIdResponse(BaseModel):
    """Response model for get_dm_events_by_participant_id"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetDmEventsByParticipantIdResponseIncludes"] = None
    meta: Optional["GetDmEventsByParticipantIdResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmEventsByParticipantIdResponseIncludes(BaseModel):
    """Nested model for GetDmEventsByParticipantIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmEventsByParticipantIdResponseMeta(BaseModel):
    """Nested model for GetDmEventsByParticipantIdResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_dm_by_participant_id


class CreateDmByParticipantIdRequest(BaseModel):
    """Request model for create_dm_by_participant_id"""

    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")
    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")

    model_config = ConfigDict(populate_by_name=True)


class CreateDmByParticipantIdResponse(BaseModel):
    """Response model for create_dm_by_participant_id"""

    data: Optional["CreateDmByParticipantIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmByParticipantIdResponseData(BaseModel):
    """Nested model for CreateDmByParticipantIdResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_dm_by_conversation_id


class CreateDmByConversationIdRequest(BaseModel):
    """Request model for create_dm_by_conversation_id"""

    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")
    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")

    model_config = ConfigDict(populate_by_name=True)


class CreateDmByConversationIdResponse(BaseModel):
    """Response model for create_dm_by_conversation_id"""

    data: Optional["CreateDmByConversationIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmByConversationIdResponseData(BaseModel):
    """Nested model for CreateDmByConversationIdResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_dm_conversations


class CreateDmConversationsRequest(BaseModel):
    """Request model for create_dm_conversations"""

    conversation_type: Optional[str] = None
    message: Any = None
    participant_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmConversationsResponse(BaseModel):
    """Response model for create_dm_conversations"""

    data: Optional["CreateDmConversationsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmConversationsResponseData(BaseModel):
    """Nested model for CreateDmConversationsResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_events


class GetEventsResponse(BaseModel):
    """Response model for get_events"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetEventsResponseIncludes"] = None
    meta: Optional["GetEventsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsResponseIncludes(BaseModel):
    """Nested model for GetEventsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsResponseMeta(BaseModel):
    """Nested model for GetEventsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_dm_conversations_id_dm_events


class GetDmConversationsIdDmEventsResponse(BaseModel):
    """Response model for get_dm_conversations_id_dm_events"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetDmConversationsIdDmEventsResponseIncludes"] = None
    meta: Optional["GetDmConversationsIdDmEventsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmConversationsIdDmEventsResponseIncludes(BaseModel):
    """Nested model for GetDmConversationsIdDmEventsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmConversationsIdDmEventsResponseMeta(BaseModel):
    """Nested model for GetDmConversationsIdDmEventsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_events_by_id


class GetEventsByIdResponse(BaseModel):
    """Response model for get_events_by_id"""

    data: Optional["GetEventsByIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None
    includes: Optional["GetEventsByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByIdResponseData(BaseModel):
    """Nested model for GetEventsByIdResponseData"""

    attachments: Optional["GetEventsByIdResponseDataAttachments"] = None
    cashtags: Optional[List] = None
    created_at: Optional[str] = None
    dm_conversation_id: Optional[str] = None
    event_type: Optional[str] = None
    hashtags: Optional[List] = None
    id: Optional[str] = None
    mentions: Optional[List] = None
    participant_ids: Optional[List] = None
    referenced_tweets: Optional[List] = None
    sender_id: Optional[str] = None
    text: Optional[str] = None
    urls: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByIdResponseDataAttachments(BaseModel):
    """Nested model for GetEventsByIdResponseDataAttachments"""

    card_ids: Optional[List] = None
    media_keys: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByIdResponseIncludes(BaseModel):
    """Nested model for GetEventsByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete_dm_events


class DeleteDmEventsResponse(BaseModel):
    """Response model for delete_dm_events"""

    data: Optional["DeleteDmEventsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteDmEventsResponseData(BaseModel):
    """Nested model for DeleteDmEventsResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
