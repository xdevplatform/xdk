"""
Auto-generated general models for the X API.

This module provides Pydantic models for request and response data structures
for the general endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_open_api_spec


class GetOpenApiSpecResponse(BaseModel):
    """Response model for get_open_api_spec"""

    model_config = ConfigDict(populate_by_name=True)
