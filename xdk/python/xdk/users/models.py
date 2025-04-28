"""
Users models for the X API.

This module provides models for the Users endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for usersIdBlocking


class users_id_blocking_response(BaseModel):
    """Response model for usersIdBlocking"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findMyUser


class find_my_user_response(BaseModel):
    """Response model for findMyUser"""

    data: Dict[str, Any] = Field(description="The X User object.", default_factory=dict)

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "created_at": "2013-12-14T04:35:55Z",
                    "id": "2244994945",
                    "name": "X Dev",
                    "protected": false,
                    "username": "TwitterDev",
                },
            }
        }


# Models for listOfRepostOfUser


class list_of_repost_of_user_response(BaseModel):
    """Response model for listOfRepostOfUser"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdDMUnBlock


class users_id_d_m_un_block_response(BaseModel):
    """Response model for usersIdDMUnBlock"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdDMBlock


class users_id_d_m_block_response(BaseModel):
    """Response model for usersIdDMBlock"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findUsersByUsername


class find_users_by_username_response(BaseModel):
    """Response model for findUsersByUsername"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listGetMembers


class list_get_members_response(BaseModel):
    """Response model for listGetMembers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findUserById


class find_user_by_id_response(BaseModel):
    """Response model for findUserById"""

    data: Dict[str, Any] = Field(description="The X User object.", default_factory=dict)

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "created_at": "2013-12-14T04:35:55Z",
                    "id": "2244994945",
                    "name": "X Dev",
                    "protected": false,
                    "username": "TwitterDev",
                },
            }
        }


# Models for listGetFollowers


class list_get_followers_response(BaseModel):
    """Response model for listGetFollowers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for tweetsIdLikingUsers


class tweets_id_liking_users_response(BaseModel):
    """Response model for tweetsIdLikingUsers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdMuting


class users_id_muting_response(BaseModel):
    """Response model for usersIdMuting"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdMute


class users_id_mute_request(BaseModel):
    """Request model for usersIdMute"""

    target_user_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "target_user_id": "2244994945",
            }
        }


class users_id_mute_response(BaseModel):
    """Response model for usersIdMute"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findUsersById


class find_users_by_id_response(BaseModel):
    """Response model for findUsersById"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for searchUserByQuery


class search_user_by_query_response(BaseModel):
    """Response model for searchUserByQuery"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for tweetsIdRetweetingUsers


class tweets_id_retweeting_users_response(BaseModel):
    """Response model for tweetsIdRetweetingUsers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdFollowing


class users_id_following_response(BaseModel):
    """Response model for usersIdFollowing"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdFollow


class users_id_follow_request(BaseModel):
    """Request model for usersIdFollow"""

    target_user_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "target_user_id": "2244994945",
            }
        }


class users_id_follow_response(BaseModel):
    """Response model for usersIdFollow"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdUnfollow


class users_id_unfollow_response(BaseModel):
    """Response model for usersIdUnfollow"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for findUserByUsername


class find_user_by_username_response(BaseModel):
    """Response model for findUserByUsername"""

    data: Dict[str, Any] = Field(description="The X User object.", default_factory=dict)

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data": {
                    "created_at": "2013-12-14T04:35:55Z",
                    "id": "2244994945",
                    "name": "X Dev",
                    "protected": false,
                    "username": "TwitterDev",
                },
            }
        }


# Models for usersIdFollowers


class users_id_followers_response(BaseModel):
    """Response model for usersIdFollowers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for usersIdUnmute


class users_id_unmute_response(BaseModel):
    """Response model for usersIdUnmute"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
