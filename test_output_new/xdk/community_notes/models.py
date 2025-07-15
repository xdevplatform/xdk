"""
Community_Notes models for the X API.

This module provides models for the Community_Notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for createNote

class 2_notes_request(BaseModel):
    """Request model for createNote"""
    
    
    
    
    
    
    info: Dict[str, Any] = Field(description="A X Community Note is a note on a Post.", default_factory=dict)
    
    post_id: Optional[str] = None
    
    test_mode: Optional[bool] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_notes_response(BaseModel):
    """Response model for createNote"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchNotesWritten








class 2_notes_search_notes_written_response(BaseModel):
    """Response model for searchNotesWritten"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchPostsEligibleForNotes








class 2_notes_search_posts_eligible_for_notes_response(BaseModel):
    """Response model for searchPostsEligibleForNotes"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteNote








class 2_notes_id_response(BaseModel):
    """Response model for deleteNote"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 