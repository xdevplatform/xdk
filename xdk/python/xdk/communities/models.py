"""
Communities models for the X API.

This module provides models for the Communities endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for communityIdGet


class community_id_get_response(BaseModel):
    """Response model for communityIdGet"""

    data: Dict[str, Any] = Field(
        description="A X Community is a curated group of Posts.", default_factory=dict
    )

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for communitiesSearch


class communities_search_response(BaseModel):
    """Response model for communitiesSearch"""

    data: Optional[List] = None

    errors: Optional[List] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
