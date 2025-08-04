"""
Bookmarks models for the X API.

This module provides models for the Bookmarks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for getUsersBookmarksByFolderId


class GetUsersBookmarksByFolderIdResponse(BaseModel):
    """Response model for getUsersBookmarksByFolderId"""

    data: Optional["GetUsersBookmarksByFolderIdResponseData"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersBookmarksByFolderIdResponseData(BaseModel):
    """Nested model for GetUsersBookmarksByFolderIdResponseData"""

    id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersBookmarks


class GetUsersBookmarksResponse(BaseModel):
    """Response model for getUsersBookmarks"""

    data: Optional[List] = None
    errors: Optional[List] = None
    includes: Optional["GetUsersBookmarksResponseIncludes"] = None
    meta: Optional["GetUsersBookmarksResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersBookmarksResponseIncludes(BaseModel):
    """Nested model for GetUsersBookmarksResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersBookmarksResponseMeta(BaseModel):
    """Nested model for GetUsersBookmarksResponseMeta"""

    next_token: Optional[str] = None
    previous_token: Optional[str] = None
    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for createUsersBookmark


class CreateUsersBookmarkRequest(BaseModel):
    """Request model for createUsersBookmark"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateUsersBookmarkResponse(BaseModel):
    """Response model for createUsersBookmark"""

    data: Optional["CreateUsersBookmarkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateUsersBookmarkResponseData(BaseModel):
    """Nested model for CreateUsersBookmarkResponseData"""

    bookmarked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for deleteUsersBookmark


class DeleteUsersBookmarkResponse(BaseModel):
    """Response model for deleteUsersBookmark"""

    data: Optional["DeleteUsersBookmarkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteUsersBookmarkResponseData(BaseModel):
    """Nested model for DeleteUsersBookmarkResponseData"""

    bookmarked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getUsersBookmarkFolders


class GetUsersBookmarkFoldersResponse(BaseModel):
    """Response model for getUsersBookmarkFolders"""

    data: Optional["GetUsersBookmarkFoldersResponseData"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersBookmarkFoldersResponseData(BaseModel):
    """Nested model for GetUsersBookmarkFoldersResponseData"""

    id: Optional[str] = None
    name: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)
