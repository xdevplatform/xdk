"""
Spaces models for the X API.

This module provides models for the Spaces endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for searchSpaces


class search_spaces_response(BaseModel):
    """Response model for searchSpaces"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for findSpacesByCreatorIds


class find_spaces_by_creator_ids_response(BaseModel):
    """Response model for findSpacesByCreatorIds"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for spaceBuyers


class space_buyers_response(BaseModel):
    """Response model for spaceBuyers"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for findSpaceById


class find_space_by_id_response(BaseModel):
    """Response model for findSpaceById"""

    data: Dict[str, Any] = Field(default_factory=dict)

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for spaceTweets


class space_tweets_response(BaseModel):
    """Response model for spaceTweets"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    meta: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for findSpacesByIds


class find_spaces_by_ids_response(BaseModel):
    """Response model for findSpacesByIds"""

    data: Optional[List] = None

    errors: Optional[List] = None

    includes: Optional[Dict[str, Any]] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
