"""
Auto-generated activity models for the X API.

This module provides Pydantic models for request and response data structures
for the activity endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime









# Models for stream








class StreamResponse(BaseModel):
    """Response model for stream"""
    
    data: Optional["StreamResponseData"] =None
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)


















class StreamResponseData(BaseModel):
    """Nested model for StreamResponseData"""
    event_type:Optional[str] =None
    event_uuid:Optional[str] =None
    filter: Optional["StreamResponseDataFilter"] = None
    payload: Optional["StreamResponseDataPayload"] = None
    tag:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class StreamResponseDataFilter(BaseModel):
    """Nested model for StreamResponseDataFilter"""
    user_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class StreamResponseDataPayload(BaseModel):
    """Nested model for StreamResponseDataPayload"""
    after:Optional[str] =None
    before:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)














# Models for get_subscriptions








class GetSubscriptionsResponse(BaseModel):
    """Response model for get_subscriptions"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    meta: Optional["GetSubscriptionsResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
























class GetSubscriptionsResponseMeta(BaseModel):
    """Nested model for GetSubscriptionsResponseMeta"""
    total_subscriptions:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for create_subscription

class CreateSubscriptionRequest(BaseModel):
    """Request model for create_subscription"""
    
    event_type: Optional[str] =None
    filter: Optional["CreateSubscriptionRequestFilter"] =None
    tag: Optional[str] =None
    webhook_id: Optional[str] =None
    

    model_config = ConfigDict(populate_by_name=True)








class CreateSubscriptionResponse(BaseModel):
    """Response model for create_subscription"""
    
    data: Optional["CreateSubscriptionResponseData"] =None
    errors: Optional[List] =None
    meta: Optional["CreateSubscriptionResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)
















class CreateSubscriptionRequestFilter(BaseModel):
    """Nested model for CreateSubscriptionRequestFilter"""
    user_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)

























class CreateSubscriptionResponseData(BaseModel):
    """Nested model for CreateSubscriptionResponseData"""
    subscription: Optional["CreateSubscriptionResponseDataSubscription"] = None
    total_subscriptions_for_instance_id:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)


class CreateSubscriptionResponseDataSubscription(BaseModel):
    """Nested model for CreateSubscriptionResponseDataSubscription"""
    created_at:Optional[str] =None
    event_type:Optional[str] =None
    filter: Optional["CreateSubscriptionResponseDataSubscriptionFilter"] = None
    subscription_id:Optional[str] =None
    tag:Optional[str] =None
    updated_at:Optional[str] =None
    webhook_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class CreateSubscriptionResponseDataSubscriptionFilter(BaseModel):
    """Nested model for CreateSubscriptionResponseDataSubscriptionFilter"""
    user_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)









class CreateSubscriptionResponseMeta(BaseModel):
    """Nested model for CreateSubscriptionResponseMeta"""
    total_subscriptions:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for update_subscription

class UpdateSubscriptionRequest(BaseModel):
    """Request model for update_subscription"""
    
    tag: Optional[str] =None
    webhook_id: Optional[str] =None
    

    model_config = ConfigDict(populate_by_name=True)








class UpdateSubscriptionResponse(BaseModel):
    """Response model for update_subscription"""
    
    data: Optional["UpdateSubscriptionResponseData"] =None
    

    model_config = ConfigDict(populate_by_name=True)
































class UpdateSubscriptionResponseData(BaseModel):
    """Nested model for UpdateSubscriptionResponseData"""
    subscription: Optional["UpdateSubscriptionResponseDataSubscription"] = None
    total_subscriptions:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)


class UpdateSubscriptionResponseDataSubscription(BaseModel):
    """Nested model for UpdateSubscriptionResponseDataSubscription"""
    created_at:Optional[str] =None
    event_type:Optional[str] =None
    filter: Optional["UpdateSubscriptionResponseDataSubscriptionFilter"] = None
    subscription_id:Optional[str] =None
    tag:Optional[str] =None
    updated_at:Optional[str] =None
    webhook_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)


class UpdateSubscriptionResponseDataSubscriptionFilter(BaseModel):
    """Nested model for UpdateSubscriptionResponseDataSubscriptionFilter"""
    user_id:Optional[str] =None

    model_config = ConfigDict(populate_by_name=True)











# Models for delete_subscription








class DeleteSubscriptionResponse(BaseModel):
    """Response model for delete_subscription"""
    
    data: Optional["DeleteSubscriptionResponseData"] =None
    errors: Optional[List] =None
    meta: Optional["DeleteSubscriptionResponseMeta"] =None
    

    model_config = ConfigDict(populate_by_name=True)


















class DeleteSubscriptionResponseData(BaseModel):
    """Nested model for DeleteSubscriptionResponseData"""
    deleted:Optional[bool] =None

    model_config = ConfigDict(populate_by_name=True)









class DeleteSubscriptionResponseMeta(BaseModel):
    """Nested model for DeleteSubscriptionResponseMeta"""
    total_subscriptions:Optional[int] =None

    model_config = ConfigDict(populate_by_name=True)









  