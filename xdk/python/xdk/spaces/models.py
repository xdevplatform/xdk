"""
Spaces models for the X API.

This module provides models for the Spaces endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getSpacesById


class GetspacesbyidResponse(BaseModel):
    """Response model for getSpacesById"""

    data: Optional["GetspacesbyidResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None
    includes: Optional["GetspacesbyidResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacesbyidResponseData(BaseModel):
    """Nested model for GetspacesbyidResponseData"""

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


class GetspacesbyidResponseIncludes(BaseModel):
    """Nested model for GetspacesbyidResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesByIds


class GetspacesbyidsResponse(BaseModel):
    """Response model for getSpacesByIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetspacesbyidsResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacesbyidsResponseIncludes(BaseModel):
    """Nested model for GetspacesbyidsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesBuyers


class GetspacesbuyersResponse(BaseModel):
    """Response model for getSpacesBuyers"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetspacesbuyersResponseIncludes"] = None
    meta: Optional["GetspacesbuyersResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacesbuyersResponseIncludes(BaseModel):
    """Nested model for GetspacesbuyersResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacesbuyersResponseMeta(BaseModel):
    """Nested model for GetspacesbuyersResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesByCreatorIds


class GetspacesbycreatoridsResponse(BaseModel):
    """Response model for getSpacesByCreatorIds"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetspacesbycreatoridsResponseIncludes"] = None
    meta: Optional["GetspacesbycreatoridsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacesbycreatoridsResponseIncludes(BaseModel):
    """Nested model for GetspacesbycreatoridsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacesbycreatoridsResponseMeta(BaseModel):
    """Nested model for GetspacesbycreatoridsResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getSpacesPosts


class GetspacespostsResponse(BaseModel):
    """Response model for getSpacesPosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetspacespostsResponseIncludes"] = None
    meta: Optional["GetspacespostsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacespostsResponseIncludes(BaseModel):
    """Nested model for GetspacespostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetspacespostsResponseMeta(BaseModel):
    """Nested model for GetspacespostsResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for searchSpaces


class SearchspacesResponse(BaseModel):
    """Response model for searchSpaces"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchspacesResponseIncludes"] = None
    meta: Optional["SearchspacesResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchspacesResponseIncludes(BaseModel):
    """Nested model for SearchspacesResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchspacesResponseMeta(BaseModel):
    """Nested model for SearchspacesResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
