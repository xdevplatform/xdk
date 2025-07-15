"""
GrokConversation models for the X API.

This module provides models for the GrokConversation endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, Literal
from pydantic import BaseModel, Field
from datetime import datetime



# Models for GetGrokConversationEventsAPI








class 2_get_grok_conversation_events_response(BaseModel):
    """Response model for GetGrokConversationEventsAPI"""
    
    
    data: Optional[List] = None
    
    errors: Optional[List] = None
    
    

    class Config:
        """Pydantic model configuration"""
        populate_by_name = True




 