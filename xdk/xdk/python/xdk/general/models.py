"""
General models for the X API.

This module provides models for the General endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime









# Models for getOpenApiSpec








class GetopenapispecResponse(BaseModel):
    """Response model for getOpenApiSpec"""
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True



















  