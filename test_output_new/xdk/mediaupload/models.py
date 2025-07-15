"""
MediaUpload models for the X API.

This module provides models for the MediaUpload endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for createMediaSubtitles

class 2_media_subtitles_request(BaseModel):
    """Request model for createMediaSubtitles"""
    
    
    
    
    
    
    id: Optional[str] = None
    
    media_category: Optional[str] = None
    
    subtitles: Optional[Dict[str, Any]] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_media_subtitles_response(BaseModel):
    """Response model for createMediaSubtitles"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for deleteMediaSubtitles

class 2_media_subtitles_request(BaseModel):
    """Request model for deleteMediaSubtitles"""
    
    
    
    
    
    
    id: Optional[str] = None
    
    language_code: Optional[str] = None
    
    media_category: Optional[str] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_media_subtitles_response(BaseModel):
    """Response model for deleteMediaSubtitles"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for getMediaUploadStatus








class 2_media_upload_response(BaseModel):
    """Response model for getMediaUploadStatus"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for mediaUpload

class 2_media_upload_request(BaseModel):
    """Request model for mediaUpload"""
    
    
    
    
    
    
    additional_owners: Optional[List] = None
    
    media: Any = None
    
    media_category: Optional[str] = None
    
    media_type: Optional[str] = None
    
    shared: Optional[bool] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_media_upload_response(BaseModel):
    """Response model for mediaUpload"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for createMediaMetadata

class 2_media_metadata_request(BaseModel):
    """Request model for createMediaMetadata"""
    
    
    
    
    
    
    id: Optional[str] = None
    
    metadata: Optional[Dict[str, Any]] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_media_metadata_response(BaseModel):
    """Response model for createMediaMetadata"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for appendMediaUpload

class 2_media_upload_id_append_request(BaseModel):
    """Request model for appendMediaUpload"""
    
    
    
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_media_upload_id_append_response(BaseModel):
    """Response model for appendMediaUpload"""
    
    
    data: Optional[Dict[str, Any]] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for finalizeMediaUpload








class 2_media_upload_id_finalize_response(BaseModel):
    """Response model for finalizeMediaUpload"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True






# Models for initializeMediaUpload

class 2_media_upload_initialize_request(BaseModel):
    """Request model for initializeMediaUpload"""
    
    
    
    
    
    
    additional_owners: Optional[List] = None
    
    media_category: Optional[str] = None
    
    media_type: Optional[str] = None
    
    shared: Optional[bool] = None
    
    total_bytes: Optional[int] = None
    
    
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True








class 2_media_upload_initialize_response(BaseModel):
    """Response model for initializeMediaUpload"""
    
    
    data: Dict[str, Any] = Field(default_factory=dict)
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 