"""
Bookmarks models for the X API.

This module provides models for the Bookmarks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getUsersIdBookmarks


class get_users_id_bookmarks_response(BaseModel):
    """Response model for getUsersIdBookmarks"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for postUsersIdBookmarks


class post_users_id_bookmarks_request(BaseModel):
    """Request model for postUsersIdBookmarks"""

    tweet_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class post_users_id_bookmarks_response(BaseModel):
    """Response model for postUsersIdBookmarks"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersIdBookmarkFolders


class get_users_id_bookmark_folders_response(BaseModel):
    """Response model for getUsersIdBookmarkFolders"""

    data: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for usersIdBookmarksDelete


class users_id_bookmarks_delete_response(BaseModel):
    """Response model for usersIdBookmarksDelete"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getUsersIdBookmarkFolderPosts


class get_users_id_bookmark_folder_posts_response(BaseModel):
    """Response model for getUsersIdBookmarkFolderPosts"""

    data: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
