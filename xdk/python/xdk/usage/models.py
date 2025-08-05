"""
Usage models for the X API.

This module provides models for the Usage endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for getUsage


class GetUsageResponse(BaseModel):
    """Response model for getUsage"""

    data: Optional["GetUsageResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsageResponseData(BaseModel):
    """Nested model for GetUsageResponseData"""

    cap_reset_day: Optional[int] = None
    daily_client_app_usage: Optional[List] = None
    daily_project_usage: Optional["GetUsageResponseDataDailyProjectUsage"] = None
    project_cap: Optional[int] = None
    project_id: Optional[str] = None
    project_usage: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetUsageResponseDataDailyProjectUsage(BaseModel):
    """Nested model for GetUsageResponseDataDailyProjectUsage"""

    project_id: Optional[int] = None
    usage: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)
