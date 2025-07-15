"""
Users models for the X API.

This module provides models for the Users endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getUsersBlocking








class 2_users_id_blocking_response(BaseModel):
    """Response model for getUsersBlocking"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for usersIdBlock

class 2_users_id_blocking_request(BaseModel):
    """Request model for usersIdBlock"""
    
    
    
    
    
    
    target_user_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_blocking_response(BaseModel):
    """Response model for usersIdBlock"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersFollowers








class 2_users_id_followers_response(BaseModel):
    """Response model for getUsersFollowers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getListsFollowers








class 2_lists_id_followers_response(BaseModel):
    """Response model for getListsFollowers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersByIds








class 2_users_response(BaseModel):
    """Response model for getUsersByIds"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unblockUsersDms








class 2_users_id_dm_unblock_response(BaseModel):
    """Response model for unblockUsersDms"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersByUsernames








class 2_users_by_response(BaseModel):
    """Response model for getUsersByUsernames"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unmuteUser








class 2_users_source_user_id_muting_target_user_id_response(BaseModel):
    """Response model for unmuteUser"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersByUsername








class 2_users_by_username_username_response(BaseModel):
    """Response model for getUsersByUsername"""
    
    
    data: Dict[str, Any] = Field(description="The X User object.", default_factory=dict)
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersMuting








class 2_users_id_muting_response(BaseModel):
    """Response model for getUsersMuting"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for muteUser

class 2_users_id_muting_request(BaseModel):
    """Request model for muteUser"""
    
    
    
    
    
    
    target_user_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_muting_response(BaseModel):
    """Response model for muteUser"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for blockUsersDms








class 2_users_id_dm_block_response(BaseModel):
    """Response model for blockUsersDms"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsLikingUsers








class 2_tweets_id_liking_users_response(BaseModel):
    """Response model for getPostsLikingUsers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getPostsRepostedBy








class 2_tweets_id_retweeted_by_response(BaseModel):
    """Response model for getPostsRepostedBy"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for unfollowUser








class 2_users_source_user_id_following_target_user_id_response(BaseModel):
    """Response model for unfollowUser"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersRepostsOfMe








class 2_users_reposts_of_me_response(BaseModel):
    """Response model for getUsersRepostsOfMe"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for searchUsers








class 2_users_search_response(BaseModel):
    """Response model for searchUsers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getListsMembers








class 2_lists_id_members_response(BaseModel):
    """Response model for getListsMembers"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for usersIdUnblock








class 2_users_source_user_id_blocking_target_user_id_response(BaseModel):
    """Response model for usersIdUnblock"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersFollowing








class 2_users_id_following_response(BaseModel):
    """Response model for getUsersFollowing"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for followUser

class 2_users_id_following_request(BaseModel):
    """Request model for followUser"""
    
    
    
    
    
    
    target_user_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_following_response(BaseModel):
    """Response model for followUser"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersById








class 2_users_id_response(BaseModel):
    """Response model for getUsersById"""
    
    
    data: Dict[str, Any] = Field(description="The X User object.", default_factory=dict)
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getMyUser








class 2_users_me_response(BaseModel):
    """Response model for getMyUser"""
    
    
    data: Dict[str, Any] = Field(description="The X User object.", default_factory=dict)
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 