"""
Direct_Messages models for the X API.

This module provides models for the Direct_Messages endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getDmConversationsIdDmEvents








class 2_dm_conversations_id_dm_events_response(BaseModel):
    """Response model for getDmConversationsIdDmEvents"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getDmEventsById








class 2_dm_events_event_id_response(BaseModel):
    """Response model for getDmEventsById"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteDmEvents








class 2_dm_events_event_id_response(BaseModel):
    """Response model for deleteDmEvents"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getDmEvents








class 2_dm_events_response(BaseModel):
    """Response model for getDmEvents"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getDmEventsByParticipantId








class 2_dm_conversations_with_participant_id_dm_events_response(BaseModel):
    """Response model for getDmEventsByParticipantId"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createDmByConversationId

class 2_dm_conversations_dm_conversation_id_messages_request(BaseModel):
    """Request model for createDmByConversationId"""
    
    
    
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_dm_conversations_dm_conversation_id_messages_response(BaseModel):
    """Response model for createDmByConversationId"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createDmByParticipantId

class 2_dm_conversations_with_participant_id_messages_request(BaseModel):
    """Request model for createDmByParticipantId"""
    
    
    
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_dm_conversations_with_participant_id_messages_response(BaseModel):
    """Response model for createDmByParticipantId"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createDmConversations

class 2_dm_conversations_request(BaseModel):
    """Request model for createDmConversations"""
    
    
    
    
    
    
    conversation_type: Optional[str] = None
    
    message: Any = None
    
    participant_ids: Optional[List] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_dm_conversations_response(BaseModel):
    """Response model for createDmConversations"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 