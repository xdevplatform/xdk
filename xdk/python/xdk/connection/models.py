"""
Connection models for the X API.

This module provides models for the Connection endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime


# Models for killAllAppConnections


class kill_all_app_connections_response(BaseModel):
    """Response model for killAllAppConnections"""

    data: Optional[Dict[str, Any]] = None

    errors: Optional[List] = None

    class Config:
        """Pydantic model configuration"""

        populate_by_name = True
