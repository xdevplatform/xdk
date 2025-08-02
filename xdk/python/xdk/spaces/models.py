"""
Spaces models for the X API.

This module provides models for the Spaces endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for searchSpaces


class SearchSpacesResponse(BaseModel):
    """Response model for searchSpaces"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchSpacesResponseIncludes"] = None
    meta: Optional["SearchSpacesResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchSpacesResponseIncludes(BaseModel):
    """Nested model for SearchSpacesResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchSpacesResponseMeta(BaseModel):
    """Nested model for SearchSpacesResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesByCreatorIds


class GetSpacesByCreatorIdsResponse(BaseModel):
    """Response model for getSpacesByCreatorIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesByCreatorIdsResponseIncludes"] = None
    meta: Optional["GetSpacesByCreatorIdsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesByCreatorIdsResponseIncludes(BaseModel):
    """Nested model for GetSpacesByCreatorIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesByCreatorIdsResponseMeta(BaseModel):
    """Nested model for GetSpacesByCreatorIdsResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesPosts


class GetSpacesPostsResponse(BaseModel):
    """Response model for getSpacesPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesPostsResponseIncludes"] = None
    meta: Optional["GetSpacesPostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesPostsResponseIncludes(BaseModel):
    """Nested model for GetSpacesPostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesPostsResponseMeta(BaseModel):
    """Nested model for GetSpacesPostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesBuyers


class GetSpacesBuyersResponse(BaseModel):
    """Response model for getSpacesBuyers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesBuyersResponseIncludes"] = None
    meta: Optional["GetSpacesBuyersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesBuyersResponseIncludes(BaseModel):
    """Nested model for GetSpacesBuyersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesBuyersResponseMeta(BaseModel):
    """Nested model for GetSpacesBuyersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesByIds


class GetSpacesByIdsResponse(BaseModel):
    """Response model for getSpacesByIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetSpacesByIdsResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesByIdsResponseIncludes(BaseModel):
    """Nested model for GetSpacesByIdsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesById


class GetSpacesByIdResponse(BaseModel):
    """Response model for getSpacesById"""

    data: Optional["GetSpacesByIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None
    includes: Optional["GetSpacesByIdResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesByIdResponseData(BaseModel):
    """Nested model for GetSpacesByIdResponseData"""

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

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetSpacesByIdResponseIncludes(BaseModel):
    """Nested model for GetSpacesByIdResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
