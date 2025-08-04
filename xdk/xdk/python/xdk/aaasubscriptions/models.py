"""
AAASubscriptions models for the X API.

This module provides models for the AAASubscriptions endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for createAccountActivitySubscription

class CreateaccountactivitysubscriptionRequest(BaseModel):
    """Request model for createAccountActivitySubscription"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class CreateaccountactivitysubscriptionResponse(BaseModel):
    """Response model for createAccountActivitySubscription"""
    
    data: Optional["CreateaccountactivitysubscriptionResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class CreateaccountactivitysubscriptionResponseData(BaseModel):
    """Nested model for CreateaccountactivitysubscriptionResponseData"""
    subscribed:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True












  