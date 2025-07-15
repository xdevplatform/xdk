"""
Media models for the X API.

This module provides models for the Media endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getMediaAnalytics








class 2_media_analytics_response(BaseModel):
    """Response model for getMediaAnalytics"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getMediaByMediaKey








class 2_media_media_key_response(BaseModel):
    """Response model for getMediaByMediaKey"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getMediaByMediaKeys








class 2_media_response(BaseModel):
    """Response model for getMediaByMediaKeys"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 