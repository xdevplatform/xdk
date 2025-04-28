"""
Compliance models for the X API.

This module provides models for the Compliance endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getTweetsLabelStream


class get_tweets_label_stream_response(BaseModel):
    """Response model for getTweetsLabelStream"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getLikesComplianceStream


class get_likes_compliance_stream_response(BaseModel):
    """Response model for getLikesComplianceStream"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getUsersComplianceStream


class get_users_compliance_stream_response(BaseModel):
    """Response model for getUsersComplianceStream"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTweetsComplianceStream


class get_tweets_compliance_stream_response(BaseModel):
    """Response model for getTweetsComplianceStream"""

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for listBatchComplianceJobs


class list_batch_compliance_jobs_response(BaseModel):
    """Response model for listBatchComplianceJobs"""

    data: Optional[List] = None

    errors: Optional[List] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for createBatchComplianceJob


class create_batch_compliance_job_request(BaseModel):
    """Request model for createBatchComplianceJob"""

    name: Optional[str] = None

    resumable: Optional[bool] = None

    type: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "my-job",
            }
        }


class create_batch_compliance_job_response(BaseModel):
    """Response model for createBatchComplianceJob"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getBatchComplianceJob


class get_batch_compliance_job_response(BaseModel):
    """Response model for getBatchComplianceJob"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
