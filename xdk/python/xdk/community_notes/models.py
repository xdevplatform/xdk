"""
community notes models for the X API.

This module provides models for the community notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for search_written


class SearchWrittenResponse(BaseModel):
    """Response model for search_written"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["SearchWrittenResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchWrittenResponseMeta(BaseModel):
    """Nested model for SearchWrittenResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create


class CreateRequest(BaseModel):
    """Request model for create"""

    info: Optional["CreateRequestInfo"] = Field(
        description="A X Community Note is a note on a Post.", default_factory=dict
    )
    post_id: Optional[str] = None
    test_mode: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateResponse(BaseModel):
    """Response model for create"""

    data: Optional["CreateResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateRequestInfo(BaseModel):
    """Nested model for CreateRequestInfo"""

    classification: Optional[str] = None
    misleading_tags: Optional[List] = None
    text: Optional[str] = None
    trustworthy_sources: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateResponseData(BaseModel):
    """Nested model for CreateResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete


class DeleteResponse(BaseModel):
    """Response model for delete"""

    data: Optional["DeleteResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteResponseData(BaseModel):
    """Nested model for DeleteResponseData"""

    id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for search_eligible_posts


class SearchEligiblePostsResponse(BaseModel):
    """Response model for search_eligible_posts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchEligiblePostsResponseIncludes"] = None
    meta: Optional["SearchEligiblePostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchEligiblePostsResponseIncludes(BaseModel):
    """Nested model for SearchEligiblePostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchEligiblePostsResponseMeta(BaseModel):
    """Nested model for SearchEligiblePostsResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
