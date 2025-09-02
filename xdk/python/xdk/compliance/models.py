"""
Auto-generated compliance models for the X API.

This module provides Pydantic models for request and response data structures
for the compliance endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_jobs_by_id


class GetJobsByIdResponse(BaseModel):
    """Response model for get_jobs_by_id"""

    data: Optional["GetJobsByIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetJobsByIdResponseData(BaseModel):
    """Nested model for GetJobsByIdResponseData"""

    created_at: Optional[str] = None
    download_expires_at: Optional[str] = None
    download_url: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    upload_expires_at: Optional[str] = None
    upload_url: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_jobs


class GetJobsResponse(BaseModel):
    """Response model for get_jobs"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetJobsResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetJobsResponseMeta(BaseModel):
    """Nested model for GetJobsResponseMeta"""

    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create_jobs


class CreateJobsRequest(BaseModel):
    """Request model for create_jobs"""

    name: Optional[str] = None
    resumable: Optional[bool] = None
    type: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateJobsResponse(BaseModel):
    """Response model for create_jobs"""

    data: Optional["CreateJobsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateJobsResponseData(BaseModel):
    """Nested model for CreateJobsResponseData"""

    created_at: Optional[str] = None
    download_expires_at: Optional[str] = None
    download_url: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    upload_expires_at: Optional[str] = None
    upload_url: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)
