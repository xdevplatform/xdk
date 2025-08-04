"""
Account_Activity models for the X API.

This module provides models for the Account_Activity endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for getAccountActivitySubscriptionCount








class GetaccountactivitysubscriptioncountResponse(BaseModel):
    """Response model for getAccountActivitySubscriptionCount"""
    
    data: Optional["GetaccountactivitysubscriptioncountResponseData"] =Field(description="The count of active subscriptions across all webhooks",default_factory=dict)
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetaccountactivitysubscriptioncountResponseData(BaseModel):
    """Nested model for GetaccountactivitysubscriptioncountResponseData"""
    account_name:Optional[str] =None
    provisioned_count:Optional[str] =None
    subscriptions_count_all:Optional[str] =None
    subscriptions_count_direct_messages:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for deleteAccountActivitySubscription








class DeleteaccountactivitysubscriptionResponse(BaseModel):
    """Response model for deleteAccountActivitySubscription"""
    
    data: Optional["DeleteaccountactivitysubscriptionResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class DeleteaccountactivitysubscriptionResponseData(BaseModel):
    """Nested model for DeleteaccountactivitysubscriptionResponseData"""
    subscribed:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for validateAccountActivitySubscription








class ValidateaccountactivitysubscriptionResponse(BaseModel):
    """Response model for validateAccountActivitySubscription"""
    
    data: Optional["ValidateaccountactivitysubscriptionResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class ValidateaccountactivitysubscriptionResponseData(BaseModel):
    """Nested model for ValidateaccountactivitysubscriptionResponseData"""
    subscribed:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for createAccountActivityReplayJob








class CreateaccountactivityreplayjobResponse(BaseModel):
    """Response model for createAccountActivityReplayJob"""
    
    created_at: Optional[str] =None
    job_id: Optional[str] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True





























# Models for getAccountActivitySubscriptions








class GetaccountactivitysubscriptionsResponse(BaseModel):
    """Response model for getAccountActivitySubscriptions"""
    
    data: Optional["GetaccountactivitysubscriptionsResponseData"] =Field(description="The list of active subscriptions for a specified webhook",default_factory=dict)
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetaccountactivitysubscriptionsResponseData(BaseModel):
    """Nested model for GetaccountactivitysubscriptionsResponseData"""
    application_id:Optional[str] =None
    subscriptions:Optional[List] =None
    webhook_id:Optional[str] =None
    webhook_url:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True












  