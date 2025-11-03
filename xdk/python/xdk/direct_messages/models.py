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









# Models for create_by_participant_id

class CreateByParticipantIdRequest(BaseModel):
    """Request model for create_by_participant_id"""
    

    model_config = ConfigDict(populate_by_name=True)








class CreateByParticipantIdResponse(BaseModel):
    """Response model for create_by_participant_id"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for create_conversation

class CreateConversationRequest(BaseModel):
    """Request model for create_conversation"""
    

    model_config = ConfigDict(populate_by_name=True)








class CreateConversationResponse(BaseModel):
    """Response model for create_conversation"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for get_events_by_id








class GetEventsByIdResponse(BaseModel):
    """Response model for get_events_by_id"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for delete_events








class DeleteEventsResponse(BaseModel):
    """Response model for delete_events"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for get_events_by_conversation_id








class GetEventsByConversationIdResponse(BaseModel):
    """Response model for get_events_by_conversation_id"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for create_by_conversation_id

class CreateByConversationIdRequest(BaseModel):
    """Request model for create_by_conversation_id"""
    

    model_config = ConfigDict(populate_by_name=True)








class CreateByConversationIdResponse(BaseModel):
    """Response model for create_by_conversation_id"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for get_events_by_participant_id








class GetEventsByParticipantIdResponse(BaseModel):
    """Response model for get_events_by_participant_id"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for get_events








class GetEventsResponse(BaseModel):
    """Response model for get_events"""
    

    model_config = ConfigDict(populate_by_name=True)



















  