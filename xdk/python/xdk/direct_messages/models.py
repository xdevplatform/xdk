"""
Direct_Messages models for the X API.

This module provides models for the Direct_Messages endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for getDmConversationsIdDmEvents


class GetDmConversationsIdDmEventsResponse(BaseModel):
    """Response model for getDmConversationsIdDmEvents"""

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


# Models for getDmEventsByParticipantId


class GetDmEventsByParticipantIdResponse(BaseModel):
    """Response model for getDmEventsByParticipantId"""

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


# Models for getDmEvents


class GetDmEventsResponse(BaseModel):
    """Response model for getDmEvents"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetDmEventsResponseIncludes"] = None
    meta: Optional["GetDmEventsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmEventsResponseIncludes(BaseModel):
    """Nested model for GetDmEventsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmEventsResponseMeta(BaseModel):
    """Nested model for GetDmEventsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getDmEventsById


class GetDmEventsByIdResponse(BaseModel):
    """Response model for getDmEventsById"""

    data: Optional["GetDmEventsByIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None
    includes: Optional["GetDmEventsByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmEventsByIdResponseData(BaseModel):
    """Nested model for GetDmEventsByIdResponseData"""

    attachments: Optional["GetDmEventsByIdResponseDataAttachments"] = None
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


class GetDmEventsByIdResponseDataAttachments(BaseModel):
    """Nested model for GetDmEventsByIdResponseDataAttachments"""

    card_ids: Optional[List] = None
    media_keys: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetDmEventsByIdResponseIncludes(BaseModel):
    """Nested model for GetDmEventsByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for deleteDmEvents


class DeleteDmEventsResponse(BaseModel):
    """Response model for deleteDmEvents"""

    data: Optional["DeleteDmEventsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteDmEventsResponseData(BaseModel):
    """Nested model for DeleteDmEventsResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for createDmByParticipantId


class CreateDmByParticipantIdRequest(BaseModel):
    """Request model for createDmByParticipantId"""

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
    """Response model for createDmByParticipantId"""

    data: Optional["CreateDmByParticipantIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmByParticipantIdResponseData(BaseModel):
    """Nested model for CreateDmByParticipantIdResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for createDmByConversationId


class CreateDmByConversationIdRequest(BaseModel):
    """Request model for createDmByConversationId"""

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
    """Response model for createDmByConversationId"""

    data: Optional["CreateDmByConversationIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmByConversationIdResponseData(BaseModel):
    """Nested model for CreateDmByConversationIdResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for createDmConversations


class CreateDmConversationsRequest(BaseModel):
    """Request model for createDmConversations"""

    conversation_type: Optional[str] = None
    message: Any = None
    participant_ids: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmConversationsResponse(BaseModel):
    """Response model for createDmConversations"""

    data: Optional["CreateDmConversationsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateDmConversationsResponseData(BaseModel):
    """Nested model for CreateDmConversationsResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)
