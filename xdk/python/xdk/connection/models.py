"""
connection models for the X API.

This module provides models for the connection endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


# Models for delete_all_connections


class DeleteAllConnectionsResponse(BaseModel):
    """Response model for delete_all_connections"""

    data: Optional["DeleteAllConnectionsResponseData"] = None
    errors: Optional[List] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteAllConnectionsResponseData(BaseModel):
    """Nested model for DeleteAllConnectionsResponseData"""

    killed_connections: Optional[bool] = None

    model_config = ConfigDict(populate_by_name=True)
