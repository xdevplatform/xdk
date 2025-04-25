"""
Connection client for the X API.

This module provides a client for interacting with the Connection endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, TypedDict
import requests
import requests_oauthlib
from ..client import Client



# Type definitions for killAllAppConnections




class kill_all_app_connections_response(TypedDict, total=False):
    """Response type for killAllAppConnections"""
    




class ConnectionClient:
    """Client for Connection operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def kill_all_app_connections(self, 
        
        
        
        
        
        
        
        
    ) -> kill_all_app_connections_response:
        """
        Force kills all streaming connections of the authenticated application.
        
        
        Force kills all streaming connections of the authenticated application.
        
        
        
        
        
        Returns:
            kill_all_app_connections_response: Response data
        """
        url = self.client.base_url + "/2/connections/all"
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
            
        )
        
        # Check for errors
        response.raise_for_status()
        
        # Return the response data
        return response.json()
     