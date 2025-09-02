"""
connections models for the X API.

This module provides models for the connections endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for delete_all


class DeleteAllResponse(BaseModel):
    """Response model for delete_all"""

    data: Optional["DeleteAllResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteAllResponseData(BaseModel):
    """Nested model for DeleteAllResponseData"""

    killed_connections: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
