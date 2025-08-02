"""
Likes models for the X API.

This module provides models for the Likes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for streamLikesFirehose


class StreamLikesFirehoseResponse(BaseModel):
    """Response model for streamLikesFirehose"""

    data: Optional["StreamLikesFirehoseResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamLikesFirehoseResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesFirehoseResponseData(BaseModel):
    """Nested model for StreamLikesFirehoseResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesFirehoseResponseIncludes(BaseModel):
    """Nested model for StreamLikesFirehoseResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


# Models for streamLikesSample10


class StreamLikesSample10Response(BaseModel):
    """Response model for streamLikesSample10"""

    data: Optional["StreamLikesSample10ResponseData"] = None
    errors: Optional[List] = None
    includes: Optional["StreamLikesSample10ResponseIncludes"] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesSample10ResponseData(BaseModel):
    """Nested model for StreamLikesSample10ResponseData"""

    created_at: Optional[str] = None
    id: Optional[str] = None
    liked_tweet_id: Optional[str] = None
    timestamp_ms: Optional[int] = None
    tweet_author_id: Optional[str] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class StreamLikesSample10ResponseIncludes(BaseModel):
    """Nested model for StreamLikesSample10ResponseIncludes"""

    media: Optional[List] = None
    places: Optional[List] = None
    polls: Optional[List] = None
    topics: Optional[List] = None
    tweets: Optional[List] = None
    users: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
