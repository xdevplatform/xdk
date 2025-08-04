"""
Bookmarks models for the X API.

This module provides models for the Bookmarks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for getUsersBookmarkFolders








class GetusersbookmarkfoldersResponse(BaseModel):
    """Response model for getUsersBookmarkFolders"""
    
    data: Optional["GetusersbookmarkfoldersResponseData"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetusersbookmarkfoldersResponseData(BaseModel):
    """Nested model for GetusersbookmarkfoldersResponseData"""
    id:Optional[str] =None
    name:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersBookmarksByFolderId








class GetusersbookmarksbyfolderidResponse(BaseModel):
    """Response model for getUsersBookmarksByFolderId"""
    
    data: Optional["GetusersbookmarksbyfolderidResponseData"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class GetusersbookmarksbyfolderidResponseData(BaseModel):
    """Nested model for GetusersbookmarksbyfolderidResponseData"""
    id:Optional[str] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for getUsersBookmarks








class GetusersbookmarksResponse(BaseModel):
    """Response model for getUsersBookmarks"""
    
    data: Optional[List] =None
    errors: Optional[List] =None
    includes: Optional["GetusersbookmarksResponseIncludes"] =None
    meta: Optional["GetusersbookmarksResponseMeta"] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True
























class GetusersbookmarksResponseIncludes(BaseModel):
    """Nested model for GetusersbookmarksResponseIncludes"""
    media:Optional[List] =None
    places:Optional[List] =None
    polls:Optional[List] =None
    topics:Optional[List] =None
    tweets:Optional[List] =None
    users:Optional[List] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






class GetusersbookmarksResponseMeta(BaseModel):
    """Nested model for GetusersbookmarksResponseMeta"""
    next_token:Optional[str] =None
    previous_token:Optional[str] =None
    result_count:Optional[int] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True











# Models for createUsersBookmark

class CreateusersbookmarkRequest(BaseModel):
    """Request model for createUsersBookmark"""
    
    tweet_id: Optional[str] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class CreateusersbookmarkResponse(BaseModel):
    """Response model for createUsersBookmark"""
    
    data: Optional["CreateusersbookmarkResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True





























class CreateusersbookmarkResponseData(BaseModel):
    """Nested model for CreateusersbookmarkResponseData"""
    bookmarked:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True














# Models for deleteUsersBookmark








class DeleteusersbookmarkResponse(BaseModel):
    """Response model for deleteUsersBookmark"""
    
    data: Optional["DeleteusersbookmarkResponseData"] =None
    errors: Optional[List] =None
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True


















class DeleteusersbookmarkResponseData(BaseModel):
    """Nested model for DeleteusersbookmarkResponseData"""
    bookmarked:Optional[bool] =None

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True












  