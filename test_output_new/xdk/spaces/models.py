"""
Spaces models for the X API.

This module provides models for the Spaces endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getSpacesPosts








class 2_spaces_id_tweets_response(BaseModel):
    """Response model for getSpacesPosts"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getSpacesBuyers








class 2_spaces_id_buyers_response(BaseModel):
    """Response model for getSpacesBuyers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getSpacesById








class 2_spaces_id_response(BaseModel):
    """Response model for getSpacesById"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getSpacesByIds








class 2_spaces_response(BaseModel):
    """Response model for getSpacesByIds"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchSpaces








class 2_spaces_search_response(BaseModel):
    """Response model for searchSpaces"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getSpacesByCreatorIds








class 2_spaces_by_creator_ids_response(BaseModel):
    """Response model for getSpacesByCreatorIds"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 