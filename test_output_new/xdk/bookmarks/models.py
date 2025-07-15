"""
Bookmarks models for the X API.

This module provides models for the Bookmarks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for getUsersBookmarks








class 2_users_id_bookmarks_response(BaseModel):
    """Response model for getUsersBookmarks"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    includes: Optional[Dict[str, Any]] = None
    
    meta: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createUsersBookmark

class 2_users_id_bookmarks_request(BaseModel):
    """Request model for createUsersBookmark"""
    
    
    
    
    
    
    tweet_id: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_users_id_bookmarks_response(BaseModel):
    """Response model for createUsersBookmark"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersBookmarksByFolderId








class 2_users_id_bookmarks_folders_folder_id_response(BaseModel):
    """Response model for getUsersBookmarksByFolderId"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteUsersBookmark








class 2_users_id_bookmarks_tweet_id_response(BaseModel):
    """Response model for deleteUsersBookmark"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getUsersBookmarkFolders








class 2_users_id_bookmarks_folders_response(BaseModel):
    """Response model for getUsersBookmarkFolders"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 