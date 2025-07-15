"""
AAASubscriptions models for the X API.

This module provides models for the AAASubscriptions endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for validateAccountActivitySubscription








class 2_account_activity_webhooks_webhook_id_subscriptions_all_response(BaseModel):
    """Response model for validateAccountActivitySubscription"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createAccountActivitySubscription

class 2_account_activity_webhooks_webhook_id_subscriptions_all_request(BaseModel):
    """Request model for createAccountActivitySubscription"""
    
    
    
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_account_activity_webhooks_webhook_id_subscriptions_all_response(BaseModel):
    """Response model for createAccountActivitySubscription"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getAccountActivitySubscriptionCount








class 2_account_activity_subscriptions_count_response(BaseModel):
    """Response model for getAccountActivitySubscriptionCount"""
    
    
    data: Dict[str, Any] = Field(description="The count of active subscriptions across all webhooks", default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getAccountActivitySubscriptions








class 2_account_activity_webhooks_webhook_id_subscriptions_all_list_response(BaseModel):
    """Response model for getAccountActivitySubscriptions"""
    
    
    data: Dict[str, Any] = Field(description="The list of active subscriptions for a specified webhook", default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createAccountActivityReplayJob








class 2_account_activity_replay_webhooks_webhook_id_subscriptions_all_response(BaseModel):
    """Response model for createAccountActivityReplayJob"""
    
    
    created_at: Optional[str] = None
    
    job_id: Optional[str] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteAccountActivitySubscription








class 2_account_activity_webhooks_webhook_id_subscriptions_user_id_all_response(BaseModel):
    """Response model for deleteAccountActivitySubscription"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 