"""
Usage models for the X API.

This module provides models for the Usage endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getUsage


class GetusageResponse(BaseModel):
    """Response model for getUsage"""

    data: Optional["GetusageResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetusageResponseData(BaseModel):
    """Nested model for GetusageResponseData"""

    cap_reset_day: Optional[int] = None
    daily_client_app_usage: Optional[List] = None
    daily_project_usage: Optional["GetusageResponseDataDailyProjectUsage"] = None
    project_cap: Optional[int] = None
    project_id: Optional[str] = None
    project_usage: Optional[int] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetusageResponseDataDailyProjectUsage(BaseModel):
    """Nested model for GetusageResponseDataDailyProjectUsage"""

    project_id: Optional[int] = None
    usage: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
