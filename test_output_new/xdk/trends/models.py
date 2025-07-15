"""
Trends models for the X API.

This module provides models for the Trends endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getTrendsByWoeid








class 2_trends_by_woeid_woeid_response(BaseModel):
    """Response model for getTrendsByWoeid"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersPersonalizedTrends








class 2_users_personalized_trends_response(BaseModel):
    """Response model for getUsersPersonalizedTrends"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 