"""
Usage models for the X API.

This module provides models for the Usage endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for getUsageTweets


class get_usage_tweets_response(BaseModel):
    """Response model for getUsageTweets"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
