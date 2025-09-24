"""
Auto-generated direct messages models for the X API.

This module provides Pydantic models for request and response data structures
for the direct messages endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_events_by_participant_id


class GetEventsByParticipantIdResponse(BaseModel):
    """Response model for get_events_by_participant_id"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetEventsByParticipantIdResponseIncludes"] = None
    meta: Optional["GetEventsByParticipantIdResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByParticipantIdResponseIncludes(BaseModel):
    """Nested model for GetEventsByParticipantIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByParticipantIdResponseMeta(BaseModel):
    """Nested model for GetEventsByParticipantIdResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_by_participant_id


class CreateByParticipantIdRequest(BaseModel):
    """Request model for create_by_participant_id"""

    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")
    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")

    model_config = ConfigDict(populate_by_name=True)


class CreateByParticipantIdResponse(BaseModel):
    """Response model for create_by_participant_id"""

    data: Optional["CreateByParticipantIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateByParticipantIdResponseData(BaseModel):
    """Nested model for CreateByParticipantIdResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

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


# Models for delete_events


class DeleteEventsResponse(BaseModel):
    """Response model for delete_events"""

    data: Optional["DeleteEventsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteEventsResponseData(BaseModel):
    """Nested model for DeleteEventsResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_conversation


class CreateConversationRequest(BaseModel):
    """Request model for create_conversation"""

    conversation_type: Optional[str] = None
    message: Any = None
    participant_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateConversationResponse(BaseModel):
    """Response model for create_conversation"""

    data: Optional["CreateConversationResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateConversationResponseData(BaseModel):
    """Nested model for CreateConversationResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_events_by_conversation_id


class GetEventsByConversationIdResponse(BaseModel):
    """Response model for get_events_by_conversation_id"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetEventsByConversationIdResponseIncludes"] = None
    meta: Optional["GetEventsByConversationIdResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByConversationIdResponseIncludes(BaseModel):
    """Nested model for GetEventsByConversationIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetEventsByConversationIdResponseMeta(BaseModel):
    """Nested model for GetEventsByConversationIdResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

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


# Models for create_by_conversation_id


class CreateByConversationIdRequest(BaseModel):
    """Request model for create_by_conversation_id"""

    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")
    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")

    model_config = ConfigDict(populate_by_name=True)


class CreateByConversationIdResponse(BaseModel):
    """Response model for create_by_conversation_id"""

    data: Optional["CreateByConversationIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateByConversationIdResponseData(BaseModel):
    """Nested model for CreateByConversationIdResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)
