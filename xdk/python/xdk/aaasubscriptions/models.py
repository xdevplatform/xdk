"""
AAASubscriptions models for the X API.

This module provides models for the AAASubscriptions endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for createAccountActivitySubscription


class CreateAccountActivitySubscriptionRequest(BaseModel):
    """Request model for createAccountActivitySubscription"""

    model_config = ConfigDict(populate_by_name=True)


class CreateAccountActivitySubscriptionResponse(BaseModel):
    """Response model for createAccountActivitySubscription"""

    data: Optional["CreateAccountActivitySubscriptionResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateAccountActivitySubscriptionResponseData(BaseModel):
    """Nested model for CreateAccountActivitySubscriptionResponseData"""

    subscribed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
