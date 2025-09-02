"""
Auto-generated usage models for the X API.

This module provides Pydantic models for request and response data structures
for the usage endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get


class GetResponse(BaseModel):
    """Response model for get"""

    data: Optional["GetResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetResponseData(BaseModel):
    """Nested model for GetResponseData"""

    cap_reset_day: Optional[int] = None
    daily_client_app_usage: Optional[List] = None
    daily_project_usage: Optional["GetResponseDataDailyProjectUsage"] = None
    project_cap: Optional[int] = None
    project_id: Optional[str] = None
    project_usage: Optional[int] = None

    model_config = ConfigDict(populate_by_name=True)


class GetResponseDataDailyProjectUsage(BaseModel):
    """Nested model for GetResponseDataDailyProjectUsage"""

    project_id: Optional[int] = None
    usage: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)
