"""
bookmarks models for the X API.

This module provides models for the bookmarks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_users_bookmark_folders


class GetUsersBookmarkFoldersResponse(BaseModel):
    """Response model for get_users_bookmark_folders"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetUsersBookmarkFoldersResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersBookmarkFoldersResponseMeta(BaseModel):
    """Nested model for GetUsersBookmarkFoldersResponseMeta"""

    pagination_token: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_users_by_folder_id


class GetUsersByFolderIdResponse(BaseModel):
    """Response model for get_users_by_folder_id"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetUsersByFolderIdResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsersByFolderIdResponseMeta(BaseModel):
    """Nested model for GetUsersByFolderIdResponseMeta"""

    pagination_token: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_users_bookmark


class CreateUsersBookmarkRequest(BaseModel):
    """Request model for create_users_bookmark"""

    tweet_id: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateUsersBookmarkResponse(BaseModel):
    """Response model for create_users_bookmark"""

    data: Optional["CreateUsersBookmarkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateUsersBookmarkResponseData(BaseModel):
    """Nested model for CreateUsersBookmarkResponseData"""

    bookmarked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete_users_bookmark


class DeleteUsersBookmarkResponse(BaseModel):
    """Response model for delete_users_bookmark"""

    data: Optional["DeleteUsersBookmarkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteUsersBookmarkResponseData(BaseModel):
    """Nested model for DeleteUsersBookmarkResponseData"""

    bookmarked: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
