"""
Likes models for the X API.

This module provides models for the Likes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for streamLikesFirehose








class StreamlikesfirehoseResponse(BaseModel):
    """Response model for streamLikesFirehose"""
    
    data: Optional["StreamlikesfirehoseResponseData"] =None
    errors: Optional[List] =None
    includes: Optional["StreamlikesfirehoseResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class StreamlikesfirehoseResponseData(BaseModel):
    """Nested model for StreamlikesfirehoseResponseData"""
    created_at:Optional[str] =None
    id:Optional[str] =None
    liked_tweet_id:Optional[str] =None
    timestamp_ms:Optional[int] =None
    tweet_author_id:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









class StreamlikesfirehoseResponseIncludes(BaseModel):
    """Nested model for StreamlikesfirehoseResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for streamLikesSample10








class Streamlikessample10Response(BaseModel):
    """Response model for streamLikesSample10"""
    
    data: Optional["Streamlikessample10ResponseData"] =None
    errors: Optional[List] =None
    includes: Optional["Streamlikessample10ResponseIncludes"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class Streamlikessample10ResponseData(BaseModel):
    """Nested model for Streamlikessample10ResponseData"""
    created_at:Optional[str] =None
    id:Optional[str] =None
    liked_tweet_id:Optional[str] =None
    timestamp_ms:Optional[int] =None
    tweet_author_id:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









class Streamlikessample10ResponseIncludes(BaseModel):
    """Nested model for Streamlikessample10ResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True









  