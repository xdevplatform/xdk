"""
General models for the X API.

This module provides models for the General endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getOpenApiSpec








class 2_openapi_json_response(BaseModel):
    """Response model for getOpenApiSpec"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getRuleCounts








class 2_tweets_search_stream_rules_counts_response(BaseModel):
    """Response model for getRuleCounts"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 