"""
Auto-generated spaces models for the X API.

This module provides Pydantic models for request and response data structures
for the spaces endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_by_ids


class GetByIdsResponse(BaseModel):
    """Response model for get_by_ids"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetByIdsResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdsResponseIncludes(BaseModel):
    """Nested model for GetByIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_buyers


class GetBuyersResponse(BaseModel):
    """Response model for get_buyers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetBuyersResponseIncludes"] = None
    meta: Optional["GetBuyersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBuyersResponseIncludes(BaseModel):
    """Nested model for GetBuyersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetBuyersResponseMeta(BaseModel):
    """Nested model for GetBuyersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_creator_ids


class GetByCreatorIdsResponse(BaseModel):
    """Response model for get_by_creator_ids"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetByCreatorIdsResponseIncludes"] = None
    meta: Optional["GetByCreatorIdsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByCreatorIdsResponseIncludes(BaseModel):
    """Nested model for GetByCreatorIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByCreatorIdsResponseMeta(BaseModel):
    """Nested model for GetByCreatorIdsResponseMeta"""

    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


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


# Models for get_by_id


class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""

    data: Optional["GetByIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None
    includes: Optional["GetByIdResponseIncludes"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseData(BaseModel):
    """Nested model for GetByIdResponseData"""

    created_at: Optional[str] = None
    creator_id: Optional[str] = None
    ended_at: Optional[str] = None
    host_ids: Optional[List] = None
    id: Optional[str] = None
    invited_user_ids: Optional[List] = None
    is_ticketed: Optional[bool] = None
    lang: Optional[str] = None
    participant_count: Optional[int] = None
    scheduled_start: Optional[str] = None
    speaker_ids: Optional[List] = None
    started_at: Optional[str] = None
    state: Optional[str] = None
    subscriber_count: Optional[int] = None
    title: Optional[str] = None
    topics: Optional[List] = None
    updated_at: Optional[str] = None

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


# Models for search


class SearchResponse(BaseModel):
    """Response model for search"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchResponseIncludes"] = None
    meta: Optional["SearchResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchResponseIncludes(BaseModel):
    """Nested model for SearchResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchResponseMeta(BaseModel):
    """Nested model for SearchResponseMeta"""

    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
