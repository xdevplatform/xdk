"""
MediaUpload client for the X API.

This module provides a client for interacting with the MediaUpload endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_media_subtitles_request, 2_media_subtitles_response, 2_media_subtitles_request, 2_media_subtitles_response, 2_media_upload_response, 2_media_upload_request, 2_media_upload_response, 2_media_metadata_request, 2_media_metadata_response, 2_media_upload_id_append_request, 2_media_upload_id_append_response, 2_media_upload_id_finalize_response, 2_media_upload_initialize_request, 2_media_upload_initialize_response

class MediaUploadClient:
    """Client for MediaUpload operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def create_media_subtitles(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_media_subtitles_request] = None,
        
    ) -> 2_media_subtitles_response:
        """
        Create Media subtitles
        
        
        Creates subtitles for a specific Media file.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_media_subtitles_response: Response data
        """
        url = self.client.base_url + "/2/media/subtitles"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_subtitles_response.model_validate(response_data)
        
    
    def delete_media_subtitles(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_media_subtitles_request] = None,
        
    ) -> 2_media_subtitles_response:
        """
        Delete Media subtitles
        
        
        Deletes subtitles for a specific Media file.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_media_subtitles_response: Response data
        """
        url = self.client.base_url + "/2/media/subtitles"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.delete(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_subtitles_response.model_validate(response_data)
        
    
    def get_media_upload_status(self, 
        
        
        
        media_id: str,
        
        
        
        
        
        
        
        command: str = None,
        
        
        
        
    ) -> 2_media_upload_response:
        """
        Get Media upload status
        
        
        Retrieves the status of a Media upload by its ID.
        
        
        
        
        Args:
            media_id: Media id for the requested media upload status.
        
        
        
        Args:
            command: The command for the media upload request.
        
        
        
        
        Returns:
            2_media_upload_response: Response data
        """
        url = self.client.base_url + "/2/media/upload"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        if media_id is not None:
            
            params["media_id"] = media_id
            
        
        
        
        
        
        if command is not None:
            
            params["command"] = command
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        headers = {}
        
        
        
        
        
        
        
        
        
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.get(
                url,
                params=params,
                headers=headers,
                
            )
        else:
            response = self.client.session.get(
                url,
                params=params,
                headers=headers,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_upload_response.model_validate(response_data)
        
    
    def media_upload(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_media_upload_request] = None,
        
    ) -> 2_media_upload_response:
        """
        Upload media
        
        
        Uploads a media file for use in posts or other content.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_media_upload_response: Response data
        """
        url = self.client.base_url + "/2/media/upload"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_upload_response.model_validate(response_data)
        
    
    def create_media_metadata(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_media_metadata_request] = None,
        
    ) -> 2_media_metadata_response:
        """
        Create Media metadata
        
        
        Creates metadata for a Media file.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_media_metadata_response: Response data
        """
        url = self.client.base_url + "/2/media/metadata"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_metadata_response.model_validate(response_data)
        
    
    def append_media_upload(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
        body: Optional[2_media_upload_id_append_request] = None,
        
    ) -> 2_media_upload_id_append_response:
        """
        Append Media upload
        
        
        Appends data to a Media upload request.
        
        
        
        
        Args:
            id: The media identifier for the media to perform the append operation.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_media_upload_id_append_response: Response data
        """
        url = self.client.base_url + "/2/media/upload/{id}/append"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{id}", str(id))
        
        
        
        
        headers = {}
        
        
        
        
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_upload_id_append_response.model_validate(response_data)
        
    
    def finalize_media_upload(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        
    ) -> 2_media_upload_id_finalize_response:
        """
        Finalize Media upload
        
        
        Finalizes a Media upload request.
        
        
        
        
        Args:
            id: The media id of the targeted media to finalize.
        
        
        
        
        Returns:
            2_media_upload_id_finalize_response: Response data
        """
        url = self.client.base_url + "/2/media/upload/{id}/finalize"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        
        
        url = url.replace("{id}", str(id))
        
        
        
        
        headers = {}
        
        
        
        
        
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_upload_id_finalize_response.model_validate(response_data)
        
    
    def initialize_media_upload(self, 
        
        
        
        
        
        
        
        
        body: Optional[2_media_upload_initialize_request] = None,
        
    ) -> 2_media_upload_initialize_response:
        """
        Initialize media upload
        
        
        Initializes a media upload.
        
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            2_media_upload_initialize_response: Response data
        """
        url = self.client.base_url + "/2/media/upload/initialize"

        

        
        
        
        
        
        
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        
        
        
        
        
        
        
        
        params = {}
        
        
        
        
        headers = {}
        
        
        
        headers["Content-Type"] = "application/json"
        
        
        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                
                json=body.model_dump(exclude_none=True) if body else None,
                
            )
        
        
        
        # Check for errors
        response.raise_for_status()
        
        # Parse the response data
        response_data = response.json()
        
        # Convert to Pydantic model if applicable
        
        return 2_media_upload_initialize_response.model_validate(response_data)
        
    