"""
Auto-generated webhooks models for the X API.

This module provides Pydantic models for request and response data structures
for the webhooks endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for create_stream_link


class CreateStreamLinkResponse(BaseModel):
    """Response model for create_stream_link"""

    data: Optional["CreateStreamLinkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateStreamLinkResponseData(BaseModel):
    """Nested model for CreateStreamLinkResponseData"""

    provisioned: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete_stream_link


class DeleteStreamLinkResponse(BaseModel):
    """Response model for delete_stream_link"""

    data: Optional["DeleteStreamLinkResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteStreamLinkResponseData(BaseModel):
    """Nested model for DeleteStreamLinkResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get


class GetResponse(BaseModel):
    """Response model for get"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class GetResponseMeta(BaseModel):
    """Nested model for GetResponseMeta"""

    result_count: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for create


class CreateRequest(BaseModel):
    """Request model for create"""

    url: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateResponse(BaseModel):
    """Response model for create"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    url: Optional[str] = None
    valid: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_stream_links


class GetStreamLinksResponse(BaseModel):
    """Response model for get_stream_links"""

    data: Optional["GetStreamLinksResponseData"] = Field(
        description="The list of active webhook links for a given stream",
        default_factory=dict,
    )
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetStreamLinksResponseData(BaseModel):
    """Nested model for GetStreamLinksResponseData"""

    links: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for validate


class ValidateResponse(BaseModel):
    """Response model for validate"""

    data: Optional["ValidateResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class ValidateResponseData(BaseModel):
    """Nested model for ValidateResponseData"""

    attempted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for delete


class DeleteResponse(BaseModel):
    """Response model for delete"""

    data: Optional["DeleteResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteResponseData(BaseModel):
    """Nested model for DeleteResponseData"""

    deleted: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
