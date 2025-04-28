"""
Lists models for the X API.

This module provides models for the Lists endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for listUserUnpin


class list_user_unpin_response(BaseModel):
    """Response model for listUserUnpin"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listUserPinnedLists


class list_user_pinned_lists_response(BaseModel):
    """Response model for listUserPinnedLists"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listUserPin


class list_user_pin_request(BaseModel):
    """Request model for listUserPin"""

    list_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "list_id": "1146654567674912769",
            }
        }


class list_user_pin_response(BaseModel):
    """Response model for listUserPin"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for userFollowedLists


class user_followed_lists_response(BaseModel):
    """Response model for userFollowedLists"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listUserFollow


class list_user_follow_request(BaseModel):
    """Request model for listUserFollow"""

    list_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "list_id": "1146654567674912769",
            }
        }


class list_user_follow_response(BaseModel):
    """Response model for listUserFollow"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listRemoveMember


class list_remove_member_response(BaseModel):
    """Response model for listRemoveMember"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listAddMember


class list_add_member_request(BaseModel):
    """Request model for listAddMember"""

    user_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "2244994945",
            }
        }


class list_add_member_response(BaseModel):
    """Response model for listAddMember"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listUserUnfollow


class list_user_unfollow_response(BaseModel):
    """Response model for listUserUnfollow"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listIdGet


class list_id_get_response(BaseModel):
    """Response model for listIdGet"""

    data: Dict[str, Any] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listIdUpdate


class list_id_update_request(BaseModel):
    """Request model for listIdUpdate"""

    description: Optional[str] = None

    name: Optional[str] = None

    private: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


class list_id_update_response(BaseModel):
    """Response model for listIdUpdate"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listIdDelete


class list_id_delete_response(BaseModel):
    """Response model for listIdDelete"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listUserOwnedLists


class list_user_owned_lists_response(BaseModel):
    """Response model for listUserOwnedLists"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listIdCreate


class list_id_create_request(BaseModel):
    """Request model for listIdCreate"""

    description: Optional[str] = None

    name: Optional[str] = None

    private: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


class list_id_create_response(BaseModel):
    """Response model for listIdCreate"""

    data: Dict[str, Any] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getUserListMemberships


class get_user_list_memberships_response(BaseModel):
    """Response model for getUserListMemberships"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
