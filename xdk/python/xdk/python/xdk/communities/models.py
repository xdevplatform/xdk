"""
Communities models for the X API.

This module provides models for the Communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getCommunitiesById


class GetcommunitiesbyidResponse(BaseModel):
    """Response model for getCommunitiesById"""

    data: Optional["GetcommunitiesbyidResponseData"] = Field(
        description="A X Community is a curated group of Posts.", default_factory=dict
    )
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class GetcommunitiesbyidResponseData(BaseModel):
    """Nested model for GetcommunitiesbyidResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for searchCommunities


class SearchcommunitiesResponse(BaseModel):
    """Response model for searchCommunities"""

    data: Optional[List] = None
    errors: Optional[List] = None
    meta: Optional["SearchcommunitiesResponseMeta"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class SearchcommunitiesResponseMeta(BaseModel):
    """Nested model for SearchcommunitiesResponseMeta"""

    next_token: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
