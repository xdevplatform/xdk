"""
Direct_Messages models for the X API.

This module provides models for the Direct_Messages endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getDmConversationsIdDmEvents


class GetdmconversationsiddmeventsResponse(BaseModel):
    """Response model for getDmConversationsIdDmEvents"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetdmconversationsiddmeventsResponseIncludes"] = None
    meta: Optional["GetdmconversationsiddmeventsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmconversationsiddmeventsResponseIncludes(BaseModel):
    """Nested model for GetdmconversationsiddmeventsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmconversationsiddmeventsResponseMeta(BaseModel):
    """Nested model for GetdmconversationsiddmeventsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmEvents


class GetdmeventsResponse(BaseModel):
    """Response model for getDmEvents"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetdmeventsResponseIncludes"] = None
    meta: Optional["GetdmeventsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsResponseIncludes(BaseModel):
    """Nested model for GetdmeventsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsResponseMeta(BaseModel):
    """Nested model for GetdmeventsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmEventsByParticipantId


class GetdmeventsbyparticipantidResponse(BaseModel):
    """Response model for getDmEventsByParticipantId"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetdmeventsbyparticipantidResponseIncludes"] = None
    meta: Optional["GetdmeventsbyparticipantidResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsbyparticipantidResponseIncludes(BaseModel):
    """Nested model for GetdmeventsbyparticipantidResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsbyparticipantidResponseMeta(BaseModel):
    """Nested model for GetdmeventsbyparticipantidResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createDmConversations


class CreatedmconversationsRequest(BaseModel):
    """Request model for createDmConversations"""

    conversation_type: Optional[str] = None
    message: Any = None
    participant_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatedmconversationsResponse(BaseModel):
    """Response model for createDmConversations"""

    data: Optional["CreatedmconversationsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatedmconversationsResponseData(BaseModel):
    """Nested model for CreatedmconversationsResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createDmByParticipantId


class CreatedmbyparticipantidRequest(BaseModel):
    """Request model for createDmByParticipantId"""

    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")
    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatedmbyparticipantidResponse(BaseModel):
    """Response model for createDmByParticipantId"""

    data: Optional["CreatedmbyparticipantidResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatedmbyparticipantidResponseData(BaseModel):
    """Nested model for CreatedmbyparticipantidResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createDmByConversationId


class CreatedmbyconversationidRequest(BaseModel):
    """Request model for createDmByConversationId"""

    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")
    attachments: Optional[List] = Field(
        default=None, description="Attachments to a DM Event."
    )
    text: Optional[str] = Field(default=None, description="Text of the message.")

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatedmbyconversationidResponse(BaseModel):
    """Response model for createDmByConversationId"""

    data: Optional["CreatedmbyconversationidResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatedmbyconversationidResponseData(BaseModel):
    """Nested model for CreatedmbyconversationidResponseData"""

    dm_conversation_id: Optional[str] = None
    dm_event_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmEventsById


class GetdmeventsbyidResponse(BaseModel):
    """Response model for getDmEventsById"""

    data: Optional["GetdmeventsbyidResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None
    includes: Optional["GetdmeventsbyidResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsbyidResponseData(BaseModel):
    """Nested model for GetdmeventsbyidResponseData"""

    attachments: Optional["GetdmeventsbyidResponseDataAttachments"] = None
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

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsbyidResponseDataAttachments(BaseModel):
    """Nested model for GetdmeventsbyidResponseDataAttachments"""

    card_ids: Optional[List] = None
    media_keys: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetdmeventsbyidResponseIncludes(BaseModel):
    """Nested model for GetdmeventsbyidResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteDmEvents


class DeletedmeventsResponse(BaseModel):
    """Response model for deleteDmEvents"""

    data: Optional["DeletedmeventsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeletedmeventsResponseData(BaseModel):
    """Nested model for DeletedmeventsResponseData"""

    deleted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
