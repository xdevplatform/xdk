"""
Communities models for the X API.

This module provides models for the Communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for searchCommunities


class SearchCommunitiesResponse(BaseModel):
    """Response model for searchCommunities"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["SearchCommunitiesResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchCommunitiesResponseMeta(BaseModel):
    """Nested model for SearchCommunitiesResponseMeta"""

    next_token: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for getCommunitiesById


class GetCommunitiesByIdResponse(BaseModel):
    """Response model for getCommunitiesById"""

    data: Optional["GetCommunitiesByIdResponseData"] = Field(
        description="A X Community is a curated group of Posts.", default_factory=dict
    )
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetCommunitiesByIdResponseData(BaseModel):
    """Nested model for GetCommunitiesByIdResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
