"""
Auto-generated connections models for the X API.

This module provides Pydantic models for request and response data structures
for the connections endpoints of the X API. All models are generated
from the OpenAPI specification and provide type safety and validation.

Generated automatically - do not edit manually.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime









# Models for delete_all








class DeleteAllResponse(BaseModel):
    """Response model for delete_all"""
    
    data: Optional["DeleteAllResponseData"] =None
    errors: Optional[List] =None
    

    model_config = ConfigDict(populate_by_name=True)


















class DeleteAllResponseData(BaseModel):
    """Nested model for DeleteAllResponseData"""
    killed_connections:Optional[bool] =None

    model_config = ConfigDict(populate_by_name=True)












  