"""
Community_Notes models for the X API.

This module provides models for the Community_Notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for createNotes


class CreateNotesRequest(BaseModel):
    """Request model for createNotes"""

    info: Optional["CreateNotesRequestInfo"] = Field(
        description="A X Community Note is a note on a Post.", default_factory=dict
    )
    post_id: Optional[str] = None
    test_mode: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateNotesResponse(BaseModel):
    """Response model for createNotes"""

    data: Optional["CreateNotesResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateNotesRequestInfo(BaseModel):
    """Nested model for CreateNotesRequestInfo"""

    classification: Optional[str] = None
    misleading_tags: Optional[List] = None
    text: Optional[str] = None
    trustworthy_sources: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateNotesResponseData(BaseModel):
    """Nested model for CreateNotesResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for deleteNotes


class DeleteNotesResponse(BaseModel):
    """Response model for deleteNotes"""

    data: Optional["DeleteNotesResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteNotesResponseData(BaseModel):
    """Nested model for DeleteNotesResponseData"""

    id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for searchNotesWritten


class SearchNotesWrittenResponse(BaseModel):
    """Response model for searchNotesWritten"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["SearchNotesWrittenResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchNotesWrittenResponseMeta(BaseModel):
    """Nested model for SearchNotesWrittenResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for searchForEligiblePosts


class SearchForEligiblePostsResponse(BaseModel):
    """Response model for searchForEligiblePosts"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["SearchForEligiblePostsResponseIncludes"] = None
    meta: Optional["SearchForEligiblePostsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchForEligiblePostsResponseIncludes(BaseModel):
    """Nested model for SearchForEligiblePostsResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchForEligiblePostsResponseMeta(BaseModel):
    """Nested model for SearchForEligiblePostsResponseMeta"""

    next_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)
