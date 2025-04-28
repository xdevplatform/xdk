"""
Likes models for the X API.

This module provides models for the Likes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for likesFirehoseStream


class likes_firehose_stream_response(BaseModel):
    """Response model for likesFirehoseStream"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for likesSample10Stream


class likes_sample10_stream_response(BaseModel):
    """Response model for likesSample10Stream"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
