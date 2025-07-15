"""
Webhooks models for the X API.

This module provides models for the Webhooks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getWebhooks








class 2_webhooks_response(BaseModel):
    """Response model for getWebhooks"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createWebhooks

class 2_webhooks_request(BaseModel):
    """Request model for createWebhooks"""
    
    
    
    
    
    
    url: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_webhooks_response(BaseModel):
    """Response model for createWebhooks"""
    
    
    created_at: Optional[str] = None
    
    id: Optional[str] = None
    
    url: Optional[str] = None
    
    valid: Optional[bool] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for validateWebhooks








class 2_webhooks_webhook_id_response(BaseModel):
    """Response model for validateWebhooks"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteWebhooks








class 2_webhooks_webhook_id_response(BaseModel):
    """Response model for deleteWebhooks"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 