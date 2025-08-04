"""
Webhooks models for the X API.

This module provides models for the Webhooks endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getWebhooks


class GetwebhooksResponse(BaseModel):
    """Response model for getWebhooks"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["GetwebhooksResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetwebhooksResponseMeta(BaseModel):
    """Nested model for GetwebhooksResponseMeta"""

    result_count: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for createWebhooks


class CreatewebhooksRequest(BaseModel):
    """Request model for createWebhooks"""

    url: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class CreatewebhooksResponse(BaseModel):
    """Response model for createWebhooks"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    url: Optional[str] = None
    valid: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for validateWebhooks


class ValidatewebhooksResponse(BaseModel):
    """Response model for validateWebhooks"""

    data: Optional["ValidatewebhooksResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class ValidatewebhooksResponseData(BaseModel):
    """Nested model for ValidatewebhooksResponseData"""

    attempted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for deleteWebhooks


class DeletewebhooksResponse(BaseModel):
    """Response model for deleteWebhooks"""

    data: Optional["DeletewebhooksResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeletewebhooksResponseData(BaseModel):
    """Nested model for DeletewebhooksResponseData"""

    deleted: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
