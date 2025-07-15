"""
Communities models for the X API.

This module provides models for the Communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for communityIdDelete








class 2_communitites_id_name_response(BaseModel):
    """Response model for communityIdDelete"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchCommunities








class 2_communities_search_response(BaseModel):
    """Response model for searchCommunities"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getCommunitiesById








class 2_communities_id_response(BaseModel):
    """Response model for getCommunitiesById"""
    
    
    data: Dict[str, Any] = Field(description="A X Community is a curated group of Posts.", default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for communityUserPin

class 2_users_id_pinned_communities_request(BaseModel):
    """Request model for communityUserPin"""
    
    
    
    
    
    
    community_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_pinned_communities_response(BaseModel):
    """Response model for communityUserPin"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for communityUserUnpin

class 2_users_id_pinned_communities_request(BaseModel):
    """Request model for communityUserUnpin"""
    
    
    
    
    
    
    community_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_pinned_communities_response(BaseModel):
    """Response model for communityUserUnpin"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for communityIdCreate

class 2_communities_request(BaseModel):
    """Request model for communityIdCreate"""
    
    
    
    
    
    
    description: Optional[str] = None
    
    name: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_communities_response(BaseModel):
    """Response model for communityIdCreate"""
    
    
    data: Dict[str, Any] = Field(description="A X Community is a curated group of Posts.", default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 