"""
Auto-generated media models for the X API.

This module provides Pydantic models for request and response data structures
for the media endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime









# Models for get_upload_status








class GetUploadStatusResponse(BaseModel):
    """Response model for get_upload_status"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for upload

class UploadRequest(BaseModel):
    """Request model for upload"""
    

    model_config = ConfigDict(populate_by_name=True)








class UploadResponse(BaseModel):
    """Response model for upload"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for create_subtitles

class CreateSubtitlesRequest(BaseModel):
    """Request model for create_subtitles"""
    

    model_config = ConfigDict(populate_by_name=True)








class CreateSubtitlesResponse(BaseModel):
    """Response model for create_subtitles"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for delete_subtitles

class DeleteSubtitlesRequest(BaseModel):
    """Request model for delete_subtitles"""
    

    model_config = ConfigDict(populate_by_name=True)








class DeleteSubtitlesResponse(BaseModel):
    """Response model for delete_subtitles"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for initialize_upload

class InitializeUploadRequest(BaseModel):
    """Request model for initialize_upload"""
    

    model_config = ConfigDict(populate_by_name=True)








class InitializeUploadResponse(BaseModel):
    """Response model for initialize_upload"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for finalize_upload








class FinalizeUploadResponse(BaseModel):
    """Response model for finalize_upload"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for get_by_key








class GetByKeyResponse(BaseModel):
    """Response model for get_by_key"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for append_upload

class AppendUploadRequest(BaseModel):
    """Request model for append_upload"""
    

    model_config = ConfigDict(populate_by_name=True)








class AppendUploadResponse(BaseModel):
    """Response model for append_upload"""
    

    model_config = ConfigDict(populate_by_name=True)



























# Models for get_analytics








class GetAnalyticsResponse(BaseModel):
    """Response model for get_analytics"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for get_by_keys








class GetByKeysResponse(BaseModel):
    """Response model for get_by_keys"""
    

    model_config = ConfigDict(populate_by_name=True)





















# Models for create_metadata

class CreateMetadataRequest(BaseModel):
    """Request model for create_metadata"""
    

    model_config = ConfigDict(populate_by_name=True)








class CreateMetadataResponse(BaseModel):
    """Response model for create_metadata"""
    

    model_config = ConfigDict(populate_by_name=True)

























  