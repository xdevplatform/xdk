"""
Compliance models for the X API.

This module provides models for the Compliance endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for streamPostsCompliance


class StreampostscomplianceResponse(BaseModel):
    """Response model for streamPostsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamUsersCompliance


class StreamuserscomplianceResponse(BaseModel):
    """Response model for streamUsersCompliance"""

    data: Optional[Any] = Field(default=None, description="User compliance data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLabelsCompliance


class StreamlabelscomplianceResponse(BaseModel):
    """Response model for streamLabelsCompliance"""

    data: Optional[Any] = Field(default=None, description="Tweet label data.")
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesCompliance


class StreamlikescomplianceResponse(BaseModel):
    """Response model for streamLikesCompliance"""

    data: Optional[Dict[str, Any]] = Field(default=None)
    errors: Optional[List] = Field(default=None)

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getComplianceJobs


class GetcompliancejobsResponse(BaseModel):
    """Response model for getComplianceJobs"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetcompliancejobsResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetcompliancejobsResponseMeta(BaseModel):
    """Nested model for GetcompliancejobsResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createComplianceJobs


class CreatecompliancejobsRequest(BaseModel):
    """Request model for createComplianceJobs"""

    name: Optional[str] = None
    resumable: Optional[bool] = None
    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatecompliancejobsResponse(BaseModel):
    """Response model for createComplianceJobs"""

    data: Optional["CreatecompliancejobsResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatecompliancejobsResponseData(BaseModel):
    """Nested model for CreatecompliancejobsResponseData"""

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


# Models for getComplianceJobsById


class GetcompliancejobsbyidResponse(BaseModel):
    """Response model for getComplianceJobsById"""

    data: Optional["GetcompliancejobsbyidResponseData"] = Field(default_factory=dict)
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetcompliancejobsbyidResponseData(BaseModel):
    """Nested model for GetcompliancejobsbyidResponseData"""

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
