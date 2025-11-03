"""
Auto-generated spaces models for the X API.

This module provides Pydantic models for request and response data structures
for the spaces endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for get_buyers


class GetBuyersResponse(BaseModel):
    """Response model for get_buyers"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_by_creator_ids


class GetByCreatorIdsResponse(BaseModel):
    """Response model for get_by_creator_ids"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_posts


class GetPostsResponse(BaseModel):
    """Response model for get_posts"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_by_id


class GetByIdResponse(BaseModel):
    """Response model for get_by_id"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for get_by_ids


class GetByIdsResponse(BaseModel):
    """Response model for get_by_ids"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# Models for search


class SearchResponse(BaseModel):
    """Response model for search"""

    model_config = ConfigDict(populate_by_name=True, extra="allow")
