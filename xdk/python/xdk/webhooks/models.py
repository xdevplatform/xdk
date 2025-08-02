"""
Webhooks models for the X API.

This module provides models for the Webhooks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getWebhooks


class GetWebhooksResponse(BaseModel):
    """Response model for getWebhooks"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetWebhooksResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetWebhooksResponseMeta(BaseModel):
    """Nested model for GetWebhooksResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createWebhooks


class CreateWebhooksRequest(BaseModel):
    """Request model for createWebhooks"""

    url: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreateWebhooksResponse(BaseModel):
    """Response model for createWebhooks"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    url: Optional[str] = None
    valid: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for validateWebhooks


class ValidateWebhooksResponse(BaseModel):
    """Response model for validateWebhooks"""

    data: Optional["ValidateWebhooksResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class ValidateWebhooksResponseData(BaseModel):
    """Nested model for ValidateWebhooksResponseData"""

    attempted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteWebhooks


class DeleteWebhooksResponse(BaseModel):
    """Response model for deleteWebhooks"""

    data: Optional["DeleteWebhooksResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeleteWebhooksResponseData(BaseModel):
    """Nested model for DeleteWebhooksResponseData"""

    deleted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
