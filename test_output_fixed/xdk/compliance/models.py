"""
Compliance models for the X API.

This module provides models for the Compliance endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for streamUsersCompliance








class 2_users_compliance_stream_response(BaseModel):
    """Response model for streamUsersCompliance"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamPostsCompliance








class 2_tweets_compliance_stream_response(BaseModel):
    """Response model for streamPostsCompliance"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamLabelsCompliance








class 2_tweets_label_stream_response(BaseModel):
    """Response model for streamLabelsCompliance"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getComplianceJobsById








class 2_compliance_jobs_id_response(BaseModel):
    """Response model for getComplianceJobsById"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for streamLikesCompliance








class 2_likes_compliance_stream_response(BaseModel):
    """Response model for streamLikesCompliance"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getComplianceJobs








class 2_compliance_jobs_response(BaseModel):
    """Response model for getComplianceJobs"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createComplianceJobs

class 2_compliance_jobs_request(BaseModel):
    """Request model for createComplianceJobs"""
    
    
    
    
    
    
    name: Optional[str] = None
    
    resumable: Optional[bool] = None
    
    type: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_compliance_jobs_response(BaseModel):
    """Response model for createComplianceJobs"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 