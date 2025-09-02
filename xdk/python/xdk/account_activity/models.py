"""
Auto-generated account activity models for the X API.

This module provides Pydantic models for request and response data structures
for the account activity endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for create_replay_job


class CreateReplayJobResponse(BaseModel):
    """Response model for create_replay_job"""

    created_at: Optional[str] = None
    job_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_subscription_count


class GetSubscriptionCountResponse(BaseModel):
    """Response model for get_subscription_count"""

    data: Optional["GetSubscriptionCountResponseData"] = Field(
        description="The count of active subscriptions across all webhooks",
        default_factory=dict,
    )
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetSubscriptionCountResponseData(BaseModel):
    """Nested model for GetSubscriptionCountResponseData"""

    account_name: Optional[str] = None
    provisioned_count: Optional[str] = None
    subscriptions_count_all: Optional[str] = None
    subscriptions_count_direct_messages: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for validate_subscription


class ValidateSubscriptionResponse(BaseModel):
    """Response model for validate_subscription"""

    data: Optional["ValidateSubscriptionResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class ValidateSubscriptionResponseData(BaseModel):
    """Nested model for ValidateSubscriptionResponseData"""

    subscribed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_subscription


class CreateSubscriptionRequest(BaseModel):
    """Request model for create_subscription"""

    model_config = ConfigDict(populate_by_name=True)


class CreateSubscriptionResponse(BaseModel):
    """Response model for create_subscription"""

    data: Optional["CreateSubscriptionResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateSubscriptionResponseData(BaseModel):
    """Nested model for CreateSubscriptionResponseData"""

    subscribed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete_subscription


class DeleteSubscriptionResponse(BaseModel):
    """Response model for delete_subscription"""

    data: Optional["DeleteSubscriptionResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteSubscriptionResponseData(BaseModel):
    """Nested model for DeleteSubscriptionResponseData"""

    subscribed: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_subscriptions


class GetSubscriptionsResponse(BaseModel):
    """Response model for get_subscriptions"""

    data: Optional["GetSubscriptionsResponseData"] = Field(
        description="The list of active subscriptions for a specified webhook",
        default_factory=dict,
    )
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetSubscriptionsResponseData(BaseModel):
    """Nested model for GetSubscriptionsResponseData"""

    application_id: Optional[str] = None
    subscriptions: Optional[List] = None
    webhook_id: Optional[str] = None
    webhook_url: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)
