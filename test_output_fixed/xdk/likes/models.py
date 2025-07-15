"""
Likes models for the X API.

This module provides models for the Likes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for streamLikesFirehose








class 2_likes_firehose_stream_response(BaseModel):
    """Response model for streamLikesFirehose"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamLikesSample10








class 2_likes_sample10_stream_response(BaseModel):
    """Response model for streamLikesSample10"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 