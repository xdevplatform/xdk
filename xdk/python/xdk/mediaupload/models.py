"""
MediaUpload models for the X API.

This module provides models for the MediaUpload endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for metadataCreate


class metadata_create_request(BaseModel):
    """Request model for metadataCreate"""

    id: Optional[str] = None

    metadata: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "1146654567674912769",
            }
        }


class metadata_create_response(BaseModel):
    """Response model for metadataCreate"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for createSubtitles


class create_subtitles_request(BaseModel):
    """Request model for createSubtitles"""

    id: Optional[str] = None

    media_category: Optional[str] = None

    subtitles: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "1146654567674912769",
                "media_category": "TweetVideo",
            }
        }


class create_subtitles_response(BaseModel):
    """Response model for createSubtitles"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for deleteSubtitles


class delete_subtitles_request(BaseModel):
    """Request model for deleteSubtitles"""

    id: Optional[str] = None

    language_code: Optional[str] = None

    media_category: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "1146654567674912769",
                "language_code": "EN",
                "media_category": "TweetVideo",
            }
        }


class delete_subtitles_response(BaseModel):
    """Response model for deleteSubtitles"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for uploadMediaStatus


class upload_media_status_response(BaseModel):
    """Response model for uploadMediaStatus"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for uploadMedia


class upload_media_request(BaseModel):
    """Request model for uploadMedia"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


class upload_media_response(BaseModel):
    """Response model for uploadMedia"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
