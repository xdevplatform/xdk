"""
General models for the X API.

This module provides models for the General endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for getOpenApiSpec


class GetOpenApiSpecResponse(BaseModel):
    """Response model for getOpenApiSpec"""

    model_config = ConfigDict(populate_by_name=True)
