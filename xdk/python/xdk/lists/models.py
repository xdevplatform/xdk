"""
Lists models for the X API.

This module provides models for the Lists endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for getUsersListMemberships


class GetUsersListMembershipsResponse(BaseModel):
    """Response model for getUsersListMemberships"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersListMembershipsResponseIncludes"] = None
    meta: Optional["GetUsersListMembershipsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersListMembershipsResponseIncludes(BaseModel):
    """Nested model for GetUsersListMembershipsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersListMembershipsResponseMeta(BaseModel):
    """Nested model for GetUsersListMembershipsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersFollowedLists


class GetUsersFollowedListsResponse(BaseModel):
    """Response model for getUsersFollowedLists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersFollowedListsResponseIncludes"] = None
    meta: Optional["GetUsersFollowedListsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersFollowedListsResponseIncludes(BaseModel):
    """Nested model for GetUsersFollowedListsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersFollowedListsResponseMeta(BaseModel):
    """Nested model for GetUsersFollowedListsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for followList


class FollowListRequest(BaseModel):
    """Request model for followList"""

    list_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class FollowListResponse(BaseModel):
    """Response model for followList"""

    data: Optional["FollowListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class FollowListResponseData(BaseModel):
    """Nested model for FollowListResponseData"""

    following: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getListsById


class GetListsByIdResponse(BaseModel):
    """Response model for getListsById"""

    data: Optional["GetListsByIdResponseData"] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetListsByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetListsByIdResponseData(BaseModel):
    """Nested model for GetListsByIdResponseData"""

    created_at: Optional[str] = None
    description: Optional[str] = None
    follower_count: Optional[int] = None
    id: Optional[str] = None
    member_count: Optional[int] = None
    name: Optional[str] = None
    owner_id: Optional[str] = None
    private: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class GetListsByIdResponseIncludes(BaseModel):
    """Nested model for GetListsByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for updateLists


class UpdateListsRequest(BaseModel):
    """Request model for updateLists"""

    description: Optional[str] = None
    name: Optional[str] = None
    private: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class UpdateListsResponse(BaseModel):
    """Response model for updateLists"""

    data: Optional["UpdateListsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UpdateListsResponseData(BaseModel):
    """Nested model for UpdateListsResponseData"""

    updated: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for deleteLists


class DeleteListsResponse(BaseModel):
    """Response model for deleteLists"""

    data: Optional["DeleteListsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteListsResponseData(BaseModel):
    """Nested model for DeleteListsResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersPinnedLists


class GetUsersPinnedListsResponse(BaseModel):
    """Response model for getUsersPinnedLists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersPinnedListsResponseIncludes"] = None
    meta: Optional["GetUsersPinnedListsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersPinnedListsResponseIncludes(BaseModel):
    """Nested model for GetUsersPinnedListsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersPinnedListsResponseMeta(BaseModel):
    """Nested model for GetUsersPinnedListsResponseMeta"""

    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for pinList


class PinListRequest(BaseModel):
    """Request model for pinList"""

    list_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class PinListResponse(BaseModel):
    """Response model for pinList"""

    data: Optional["PinListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class PinListResponseData(BaseModel):
    """Nested model for PinListResponseData"""

    pinned: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unpinList


class UnpinListResponse(BaseModel):
    """Response model for unpinList"""

    data: Optional["UnpinListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnpinListResponseData(BaseModel):
    """Nested model for UnpinListResponseData"""

    pinned: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for removeListsMemberByUserId


class RemoveListsMemberByUserIdResponse(BaseModel):
    """Response model for removeListsMemberByUserId"""

    data: Optional["RemoveListsMemberByUserIdResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class RemoveListsMemberByUserIdResponseData(BaseModel):
    """Nested model for RemoveListsMemberByUserIdResponseData"""

    is_member: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersOwnedLists


class GetUsersOwnedListsResponse(BaseModel):
    """Response model for getUsersOwnedLists"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersOwnedListsResponseIncludes"] = None
    meta: Optional["GetUsersOwnedListsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersOwnedListsResponseIncludes(BaseModel):
    """Nested model for GetUsersOwnedListsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersOwnedListsResponseMeta(BaseModel):
    """Nested model for GetUsersOwnedListsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for createLists


class CreateListsRequest(BaseModel):
    """Request model for createLists"""

    description: Optional[str] = None
    name: Optional[str] = None
    private: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateListsResponse(BaseModel):
    """Response model for createLists"""

    data: Optional["CreateListsResponseData"] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateListsResponseData(BaseModel):
    """Nested model for CreateListsResponseData"""

    id: Optional[str] = None
    name: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for addListsMember


class AddListsMemberRequest(BaseModel):
    """Request model for addListsMember"""

    user_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class AddListsMemberResponse(BaseModel):
    """Response model for addListsMember"""

    data: Optional["AddListsMemberResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class AddListsMemberResponseData(BaseModel):
    """Nested model for AddListsMemberResponseData"""

    is_member: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for unfollowList


class UnfollowListResponse(BaseModel):
    """Response model for unfollowList"""

    data: Optional["UnfollowListResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UnfollowListResponseData(BaseModel):
    """Nested model for UnfollowListResponseData"""

    following: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
