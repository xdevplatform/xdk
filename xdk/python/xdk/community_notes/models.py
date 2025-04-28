"""
Community_Notes models for the X API.

This module provides models for the Community_Notes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for findNoteByTweetId


class find_note_by_tweet_id_response(BaseModel):
    """Response model for findNoteByTweetId"""

    data: Dict[str, Any] = Field(
        description="A X Community Note is a note on a Post.", default_factory=dict
    )

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
