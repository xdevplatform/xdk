"""
Auto-generated lists models for the X API.

This module provides Pydantic models for request and response data structures
for the lists endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_posts


class GetPostsResponse(BaseModel):
    """Response model for get_posts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetPostsResponseIncludes"] = None
    meta: Optional["GetPostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsResponseIncludes(BaseModel):
    """Nested model for GetPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetPostsResponseMeta(BaseModel):
    """Nested model for GetPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create


class CreateRequest(BaseModel):
    """Request model for create"""

    description: Optional[str] = None
    name: Optional[str] = None
    private: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateResponse(BaseModel):
    """Response model for create"""

    data: Optional["CreateResponseData"] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateResponseData(BaseModel):
    """Nested model for CreateResponseData"""

    id: Optional[str] = None
    name: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for remove_member_by_user_id


class RemoveMemberByUserIdResponse(BaseModel):
    """Response model for remove_member_by_user_id"""

    data: Optional["RemoveMemberByUserIdResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class RemoveMemberByUserIdResponseData(BaseModel):
    """Nested model for RemoveMemberByUserIdResponseData"""

    is_member: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_id


class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""

    data: Optional["GetByIdResponseData"] = Field(
        description="A X List is a curated group of accounts.", default_factory=dict
    )
    errors: Optional[List] = None
    includes: Optional["GetByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseData(BaseModel):
    """Nested model for GetByIdResponseData"""

    created_at: Optional[str] = None
    description: Optional[str] = None
    follower_count: Optional[int] = None
    id: Optional[str] = None
    member_count: Optional[int] = None
    name: Optional[str] = None
    owner_id: Optional[str] = None
    private: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseIncludes(BaseModel):
    """Nested model for GetByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for update


class UpdateRequest(BaseModel):
    """Request model for update"""

    description: Optional[str] = None
    name: Optional[str] = None
    private: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class UpdateResponse(BaseModel):
    """Response model for update"""

    data: Optional["UpdateResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class UpdateResponseData(BaseModel):
    """Nested model for UpdateResponseData"""

    updated: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete


class DeleteResponse(BaseModel):
    """Response model for delete"""

    data: Optional["DeleteResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteResponseData(BaseModel):
    """Nested model for DeleteResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_members


class GetMembersResponse(BaseModel):
    """Response model for get_members"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetMembersResponseIncludes"] = None
    meta: Optional["GetMembersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMembersResponseIncludes(BaseModel):
    """Nested model for GetMembersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetMembersResponseMeta(BaseModel):
    """Nested model for GetMembersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for add_member


class AddMemberRequest(BaseModel):
    """Request model for add_member"""

    user_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class AddMemberResponse(BaseModel):
    """Response model for add_member"""

    data: Optional["AddMemberResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class AddMemberResponseData(BaseModel):
    """Nested model for AddMemberResponseData"""

    is_member: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_followers


class GetFollowersResponse(BaseModel):
    """Response model for get_followers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetFollowersResponseIncludes"] = None
    meta: Optional["GetFollowersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowersResponseIncludes(BaseModel):
    """Nested model for GetFollowersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetFollowersResponseMeta(BaseModel):
    """Nested model for GetFollowersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
