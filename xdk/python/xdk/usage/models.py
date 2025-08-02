"""
Usage models for the X API.

This module provides models for the Usage endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getUsage


class GetUsageResponse(BaseModel):
    """Response model for getUsage"""

    data: Optional["GetUsageResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsageResponseData(BaseModel):
    """Nested model for GetUsageResponseData"""

    cap_reset_day: Optional[int] = None
    daily_client_app_usage: Optional[List] = None
    daily_project_usage: Optional["GetUsageResponseDataDaily_project_usage"] = None
    project_cap: Optional[int] = None
    project_id: Optional[str] = None
    project_usage: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetUsageResponseDataDaily_project_usage(BaseModel):
    """Nested model for GetUsageResponseDataDaily_project_usage"""

    project_id: Optional[int] = None
    usage: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
