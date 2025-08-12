"""
communities models for the X API.

This module provides models for the communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_by_id


class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""

    data: Optional["GetByIdResponseData"] = Field(
        description="A X Community is a curated group of Posts.", default_factory=dict
    )
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class GetByIdResponseData(BaseModel):
    """Nested model for GetByIdResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


# Models for search


class SearchResponse(BaseModel):
    """Response model for search"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["SearchResponseMeta"] = None

    model_config = ConfigDict(populate_by_name=True)


class SearchResponseMeta(BaseModel):
    """Nested model for SearchResponseMeta"""

    next_token: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)
