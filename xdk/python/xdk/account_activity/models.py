"""
Account_Activity models for the X API.

This module provides models for the Account_Activity endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getAccountActivitySubscriptionCount


class GetAccountActivitySubscriptionCountResponse(BaseModel):
    """Response model for getAccountActivitySubscriptionCount"""

    data: Optional["GetAccountActivitySubscriptionCountResponseData"] = Field(
        description="The count of active subscriptions across all webhooks",
        default_factory=dict,
    )
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetAccountActivitySubscriptionCountResponseData(BaseModel):
    """Nested model for GetAccountActivitySubscriptionCountResponseData"""

    account_name: Optional[str] = None
    provisioned_count: Optional[str] = None
    subscriptions_count_all: Optional[str] = None
    subscriptions_count_direct_messages: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for validateAccountActivitySubscription


class ValidateAccountActivitySubscriptionResponse(BaseModel):
    """Response model for validateAccountActivitySubscription"""

    data: Optional["ValidateAccountActivitySubscriptionResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class ValidateAccountActivitySubscriptionResponseData(BaseModel):
    """Nested model for ValidateAccountActivitySubscriptionResponseData"""

    subscribed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteAccountActivitySubscription


class DeleteAccountActivitySubscriptionResponse(BaseModel):
    """Response model for deleteAccountActivitySubscription"""

    data: Optional["DeleteAccountActivitySubscriptionResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeleteAccountActivitySubscriptionResponseData(BaseModel):
    """Nested model for DeleteAccountActivitySubscriptionResponseData"""

    subscribed: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getAccountActivitySubscriptions


class GetAccountActivitySubscriptionsResponse(BaseModel):
    """Response model for getAccountActivitySubscriptions"""

    data: Optional["GetAccountActivitySubscriptionsResponseData"] = Field(
        description="The list of active subscriptions for a specified webhook",
        default_factory=dict,
    )
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetAccountActivitySubscriptionsResponseData(BaseModel):
    """Nested model for GetAccountActivitySubscriptionsResponseData"""

    application_id: Optional[str] = None
    subscriptions: Optional[List] = None
    webhook_id: Optional[str] = None
    webhook_url: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createAccountActivityReplayJob


class CreateAccountActivityReplayJobResponse(BaseModel):
    """Response model for createAccountActivityReplayJob"""

    created_at: Optional[str] = None
    job_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
