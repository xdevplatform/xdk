"""
webhooks models for the X API.

This module provides models for the webhooks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


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
