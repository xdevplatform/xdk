"""
Trends models for the X API.

This module provides models for the Trends endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for getUsersPersonalizedTrends


class GetUsersPersonalizedTrendsResponse(BaseModel):
    """Response model for getUsersPersonalizedTrends"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for getTrendsByWoeid


class GetTrendsByWoeidResponse(BaseModel):
    """Response model for getTrendsByWoeid"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)
