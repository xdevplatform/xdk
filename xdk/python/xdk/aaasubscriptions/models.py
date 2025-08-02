"""
AAASubscriptions models for the X API.

This module provides models for the AAASubscriptions endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for createAccountActivitySubscription


class CreateAccountActivitySubscriptionRequest(BaseModel):
    """Request model for createAccountActivitySubscription"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateAccountActivitySubscriptionResponse(BaseModel):
    """Response model for createAccountActivitySubscription"""

    data: Optional["CreateAccountActivitySubscriptionResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateAccountActivitySubscriptionResponseData(BaseModel):
    """Nested model for CreateAccountActivitySubscriptionResponseData"""

    subscribed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
