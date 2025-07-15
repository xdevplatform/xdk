"""
Lists models for the X API.

This module provides models for the Lists endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for removeListsMemberByUserId








class 2_lists_id_members_user_id_response(BaseModel):
    """Response model for removeListsMemberByUserId"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createLists

class 2_lists_request(BaseModel):
    """Request model for createLists"""
    
    
    
    
    
    
    description: Optional[str] = None
    
    name: Optional[str] = None
    
    private: Optional[bool] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_lists_response(BaseModel):
    """Response model for createLists"""
    
    
    data: Dict[str, Any] = Field(description="A X List is a curated group of accounts.", default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getListsById








class 2_lists_id_response(BaseModel):
    """Response model for getListsById"""
    
    
    data: Dict[str, Any] = Field(description="A X List is a curated group of accounts.", default_factory=dict)
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for updateLists

class 2_lists_id_request(BaseModel):
    """Request model for updateLists"""
    
    
    
    
    
    
    description: Optional[str] = None
    
    name: Optional[str] = None
    
    private: Optional[bool] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_lists_id_response(BaseModel):
    """Response model for updateLists"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteLists








class 2_lists_id_response(BaseModel):
    """Response model for deleteLists"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersOwnedLists








class 2_users_id_owned_lists_response(BaseModel):
    """Response model for getUsersOwnedLists"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for addListsMember

class 2_lists_id_members_request(BaseModel):
    """Request model for addListsMember"""
    
    
    
    
    
    
    user_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_lists_id_members_response(BaseModel):
    """Response model for addListsMember"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unpinList








class 2_users_id_pinned_lists_list_id_response(BaseModel):
    """Response model for unpinList"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unfollowList








class 2_users_id_followed_lists_list_id_response(BaseModel):
    """Response model for unfollowList"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersFollowedLists








class 2_users_id_followed_lists_response(BaseModel):
    """Response model for getUsersFollowedLists"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for followList

class 2_users_id_followed_lists_request(BaseModel):
    """Request model for followList"""
    
    
    
    
    
    
    list_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_followed_lists_response(BaseModel):
    """Response model for followList"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersListMemberships








class 2_users_id_list_memberships_response(BaseModel):
    """Response model for getUsersListMemberships"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersPinnedLists








class 2_users_id_pinned_lists_response(BaseModel):
    """Response model for getUsersPinnedLists"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for pinList

class 2_users_id_pinned_lists_request(BaseModel):
    """Request model for pinList"""
    
    
    
    
    
    
    list_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_pinned_lists_response(BaseModel):
    """Response model for pinList"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 