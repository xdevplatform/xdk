"""
Articles models for the X API.

This module provides models for the Articles endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for articleDraftCreate

class 2_article_draft_request(BaseModel):
    """Request model for articleDraftCreate"""
    
    
    
    
    
    
    card_uri: Optional[str] = None
    
    community_id: Optional[str] = None
    
    direct_message_deep_link: Optional[str] = None
    
    for_super_followers_only: Optional[bool] = None
    
    geo: Optional[Dict[str, Any]] = None
    
    media: Dict[str, Any] = Field(description="Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.", default_factory=dict)
    
    nullcast: Optional[bool] = None
    
    poll: Dict[str, Any] = Field(description="Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.", default_factory=dict)
    
    quote_tweet_id: Optional[str] = None
    
    reply: Dict[str, Any] = Field(description="Tweet information of the Tweet being replied to.", default_factory=dict)
    
    reply_settings: Optional[str] = None
    
    text: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_article_draft_response(BaseModel):
    """Response model for articleDraftCreate"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 