"""
Compliance models for the X API.

This module provides models for the Compliance endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for streamLabelsCompliance


class StreamLabelsComplianceResponse(BaseModel):
    """Response model for streamLabelsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet label data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamPostsCompliance


class StreamPostsComplianceResponse(BaseModel):
    """Response model for streamPostsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamUsersCompliance


class StreamUsersComplianceResponse(BaseModel):
    """Response model for streamUsersCompliance"""

    data: Optional[Any] = Field(default=None, description="User compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getComplianceJobs


class GetComplianceJobsResponse(BaseModel):
    """Response model for getComplianceJobs"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetComplianceJobsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetComplianceJobsResponseMeta(BaseModel):
    """Nested model for GetComplianceJobsResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createComplianceJobs


class CreateComplianceJobsRequest(BaseModel):
    """Request model for createComplianceJobs"""

    name: Optional[str] = None
    resumable: Optional[bool] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateComplianceJobsResponse(BaseModel):
    """Response model for createComplianceJobs"""

    data: Optional["CreateComplianceJobsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateComplianceJobsResponseData(BaseModel):
    """Nested model for CreateComplianceJobsResponseData"""

    created_at: Optional[str] = None
    download_expires_at: Optional[str] = None
    download_url: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    upload_expires_at: Optional[str] = None
    upload_url: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesCompliance


class StreamLikesComplianceResponse(BaseModel):
    """Response model for streamLikesCompliance"""

    data: Optional[Dict[str, Any]] = Field(default=None)
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getComplianceJobsById


class GetComplianceJobsByIdResponse(BaseModel):
    """Response model for getComplianceJobsById"""

    data: Optional["GetComplianceJobsByIdResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetComplianceJobsByIdResponseData(BaseModel):
    """Nested model for GetComplianceJobsByIdResponseData"""

    created_at: Optional[str] = None
    download_expires_at: Optional[str] = None
    download_url: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    upload_expires_at: Optional[str] = None
    upload_url: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
