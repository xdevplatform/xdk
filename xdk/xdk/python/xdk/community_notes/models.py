"""
Community_Notes models for the X API.

This module provides models for the Community_Notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for searchForEligiblePosts








class SearchforeligiblepostsResponse(BaseModel):
    """Response model for searchForEligiblePosts"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["SearchforeligiblepostsResponseIncludes"] =None
    meta: Optional["SearchforeligiblepostsResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class SearchforeligiblepostsResponseIncludes(BaseModel):
    """Nested model for SearchforeligiblepostsResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class SearchforeligiblepostsResponseMeta(BaseModel):
    """Nested model for SearchforeligiblepostsResponseMeta"""
    next_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for createNotes

class CreatenotesRequest(BaseModel):
    """Request model for createNotes"""
    
    info: Optional["CreatenotesRequestInfo"] =Field(description="A X Community Note is a note on a Post.",default_factory=dict)
    post_id: Optional[str] =None
    test_mode: Optional[bool] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class CreatenotesResponse(BaseModel):
    """Response model for createNotes"""
    
    data: Optional["CreatenotesResponseData"] =Field(default_factory=dict)
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True













class CreatenotesRequestInfo(BaseModel):
    """Nested model for CreatenotesRequestInfo"""
    classification:Optional[str] =None
    misleading_tags:Optional[List] =None
    text:Optional[str] =None
    trustworthy_sources:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True

























class CreatenotesResponseData(BaseModel):
    """Nested model for CreatenotesResponseData"""
    deleted:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for deleteNotes








class DeletenotesResponse(BaseModel):
    """Response model for deleteNotes"""
    
    data: Optional["DeletenotesResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class DeletenotesResponseData(BaseModel):
    """Nested model for DeletenotesResponseData"""
    id:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for searchNotesWritten








class SearchnoteswrittenResponse(BaseModel):
    """Response model for searchNotesWritten"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    meta: Optional["SearchnoteswrittenResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class SearchnoteswrittenResponseMeta(BaseModel):
    """Nested model for SearchnoteswrittenResponseMeta"""
    next_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









  