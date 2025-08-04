"""
Connection models for the X API.

This module provides models for the Connection endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for deleteAllConnections


class DeleteallconnectionsResponse(BaseModel):
    """Response model for deleteAllConnections"""

    data: Optional["DeleteallconnectionsResponseData"] = None
    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True


class DeleteallconnectionsResponseData(BaseModel):
    """Nested model for DeleteallconnectionsResponseData"""

    killed_connections: Optional[bool] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
