"""
Direct_Messages models for the X API.

This module provides models for the Direct_Messages endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for dmConversationIdCreate


class dm_conversation_id_create_request(BaseModel):
    """Request model for dmConversationIdCreate"""

    conversation_type: Optional[str] = None

    message: Any = None

    participant_ids: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class dm_conversation_id_create_response(BaseModel):
    """Response model for dmConversationIdCreate"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmEventsById


class get_dm_events_by_id_response(BaseModel):
    """Response model for getDmEventsById"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for dmEventDelete


class dm_event_delete_response(BaseModel):
    """Response model for dmEventDelete"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmConversationsIdDmEvents


class get_dm_conversations_id_dm_events_response(BaseModel):
    """Response model for getDmConversationsIdDmEvents"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmEvents


class get_dm_events_response(BaseModel):
    """Response model for getDmEvents"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for dmConversationByIdEventIdCreate


class dm_conversation_by_id_event_id_create_request(BaseModel):
    """Request model for dmConversationByIdEventIdCreate"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class dm_conversation_by_id_event_id_create_response(BaseModel):
    """Response model for dmConversationByIdEventIdCreate"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getDmConversationsWithParticipantIdDmEvents


class get_dm_conversations_with_participant_id_dm_events_response(BaseModel):
    """Response model for getDmConversationsWithParticipantIdDmEvents"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for dmConversationWithUserEventIdCreate


class dm_conversation_with_user_event_id_create_request(BaseModel):
    """Request model for dmConversationWithUserEventIdCreate"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class dm_conversation_with_user_event_id_create_response(BaseModel):
    """Response model for dmConversationWithUserEventIdCreate"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
