"""
Lists models for the X API.

This module provides models for the Lists endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getUsersFollowedLists


class GetusersfollowedlistsResponse(BaseModel):
    """Response model for getUsersFollowedLists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetusersfollowedlistsResponseIncludes"] = None
    meta: Optional["GetusersfollowedlistsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetusersfollowedlistsResponseIncludes(BaseModel):
    """Nested model for GetusersfollowedlistsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetusersfollowedlistsResponseMeta(BaseModel):
    """Nested model for GetusersfollowedlistsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for followList


class FollowlistRequest(BaseModel):
    """Request model for followList"""

    list_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FollowlistResponse(BaseModel):
    """Response model for followList"""

    data: Optional["FollowlistResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class FollowlistResponseData(BaseModel):
    """Nested model for FollowlistResponseData"""

    following: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersListMemberships


class GetuserslistmembershipsResponse(BaseModel):
    """Response model for getUsersListMemberships"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetuserslistmembershipsResponseIncludes"] = None
    meta: Optional["GetuserslistmembershipsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetuserslistmembershipsResponseIncludes(BaseModel):
    """Nested model for GetuserslistmembershipsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetuserslistmembershipsResponseMeta(BaseModel):
    """Nested model for GetuserslistmembershipsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersPinnedLists


class GetuserspinnedlistsResponse(BaseModel):
    """Response model for getUsersPinnedLists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetuserspinnedlistsResponseIncludes"] = None
    meta: Optional["GetuserspinnedlistsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetuserspinnedlistsResponseIncludes(BaseModel):
    """Nested model for GetuserspinnedlistsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetuserspinnedlistsResponseMeta(BaseModel):
    """Nested model for GetuserspinnedlistsResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for pinList


class PinlistRequest(BaseModel):
    """Request model for pinList"""

    list_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class PinlistResponse(BaseModel):
    """Response model for pinList"""

    data: Optional["PinlistResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class PinlistResponseData(BaseModel):
    """Nested model for PinlistResponseData"""

    pinned: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersOwnedLists


class GetusersownedlistsResponse(BaseModel):
    """Response model for getUsersOwnedLists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetusersownedlistsResponseIncludes"] = None
    meta: Optional["GetusersownedlistsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetusersownedlistsResponseIncludes(BaseModel):
    """Nested model for GetusersownedlistsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetusersownedlistsResponseMeta(BaseModel):
    """Nested model for GetusersownedlistsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createLists


class CreatelistsRequest(BaseModel):
    """Request model for createLists"""

    description: Optional[str] = None
    name: Optional[str] = None
    private: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatelistsResponse(BaseModel):
    """Response model for createLists"""

    data: Optional["CreatelistsResponseData"] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatelistsResponseData(BaseModel):
    """Nested model for CreatelistsResponseData"""

    id: Optional[str] = None
    name: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for addListsMember


class AddlistsmemberRequest(BaseModel):
    """Request model for addListsMember"""

    user_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class AddlistsmemberResponse(BaseModel):
    """Response model for addListsMember"""

    data: Optional["AddlistsmemberResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class AddlistsmemberResponseData(BaseModel):
    """Nested model for AddlistsmemberResponseData"""

    is_member: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getListsById


class GetlistsbyidResponse(BaseModel):
    """Response model for getListsById"""

    data: Optional["GetlistsbyidResponseData"] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetlistsbyidResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetlistsbyidResponseData(BaseModel):
    """Nested model for GetlistsbyidResponseData"""

    created_at: Optional[str] = None
    description: Optional[str] = None
    follower_count: Optional[int] = None
    id: Optional[str] = None
    member_count: Optional[int] = None
    name: Optional[str] = None
    owner_id: Optional[str] = None
    private: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetlistsbyidResponseIncludes(BaseModel):
    """Nested model for GetlistsbyidResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for updateLists


class UpdatelistsRequest(BaseModel):
    """Request model for updateLists"""

    description: Optional[str] = None
    name: Optional[str] = None
    private: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UpdatelistsResponse(BaseModel):
    """Response model for updateLists"""

    data: Optional["UpdatelistsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UpdatelistsResponseData(BaseModel):
    """Nested model for UpdatelistsResponseData"""

    updated: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteLists


class DeletelistsResponse(BaseModel):
    """Response model for deleteLists"""

    data: Optional["DeletelistsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeletelistsResponseData(BaseModel):
    """Nested model for DeletelistsResponseData"""

    deleted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unfollowList


class UnfollowlistResponse(BaseModel):
    """Response model for unfollowList"""

    data: Optional["UnfollowlistResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnfollowlistResponseData(BaseModel):
    """Nested model for UnfollowlistResponseData"""

    following: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for removeListsMemberByUserId


class RemovelistsmemberbyuseridResponse(BaseModel):
    """Response model for removeListsMemberByUserId"""

    data: Optional["RemovelistsmemberbyuseridResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class RemovelistsmemberbyuseridResponseData(BaseModel):
    """Nested model for RemovelistsmemberbyuseridResponseData"""

    is_member: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for unpinList


class UnpinlistResponse(BaseModel):
    """Response model for unpinList"""

    data: Optional["UnpinlistResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class UnpinlistResponseData(BaseModel):
    """Nested model for UnpinlistResponseData"""

    pinned: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
