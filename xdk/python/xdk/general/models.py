"""
general models for the X API.

This module provides models for the general endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_open_api_spec


class GetOpenApiSpecResponse(BaseModel):
    """Response model for get_open_api_spec"""

    model_config = ConfigDict(populate_by_name=True)
