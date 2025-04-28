"""
Trends models for the X API.

This module provides models for the Trends endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for personalizedTrends


class personalized_trends_response(BaseModel):
    """Response model for personalizedTrends"""

    data: Optional[List] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}


# Models for getTrends


class get_trends_response(BaseModel):
    """Response model for getTrends"""

    data: Optional[List] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
        json_schema_extra = {"example": {}}
