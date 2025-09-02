"""
trends models for the X API.

This module provides models for the trends endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_personalized


class GetPersonalizedResponse(BaseModel):
    """Response model for get_personalized"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for get_by_woeid


class GetByWoeidResponse(BaseModel):
    """Response model for get_by_woeid"""

    data: Optional[List] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)
