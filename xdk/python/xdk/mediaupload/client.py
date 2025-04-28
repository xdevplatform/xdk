"""
MediaUpload client for the X API.

This module provides a client for interacting with the MediaUpload endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import requests_oauthlib
from ..client import Client
from .models import (
    upload_media_status_response,
    upload_media_request,
    upload_media_response,
    create_subtitles_request,
    create_subtitles_response,
    delete_subtitles_request,
    delete_subtitles_response,
    metadata_create_request,
    metadata_create_response,
)


class MediaUploadClient:
    """Client for MediaUpload operations"""


    def __init__(self, client: Client):
        self.client = client


    def upload_media_status(
        self,
        media_id: str,
        command: str = None,
    ) -> upload_media_status_response:
        """
        Media Upload Status
        Get MediaUpload Status
        Args:
            media_id: Media id for the requested media upload status.
        Args:
            command: The command for the media upload request.
        Returns:
            upload_media_status_response: Response data
        """
        url = self.client.base_url + "/2/media/upload"
        params = {}
        if media_id is not None:
            params["media_id"] = media_id
        if command is not None:
            params["command"] = command
        headers = {}
        # Make the request
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
        return upload_media_status_response.model_validate(response_data)


    def upload_media(
        self,
        command: str,
        media_id: str = None,
        total_bytes: int = None,
        media_type: str = None,
        media_category: str = None,
        additional_owners: List = None,
        body: Optional[upload_media_request] = None,
    ) -> upload_media_response:
        """
        Media Upload
        MediaUpload
        Args:
            media_id: The media id of the targeted media to APPEND/FINALIZE.
        Args:
            total_bytes: Total number of bytes being uploaded.
        Args:
            media_type: The MIME type of the media being uploaded. For example, video/mp4.
        Args:
            media_category: A string enum value which identifies a media use-case. This identifier is used to enforce use-case specific constraints (e.g. file size, video duration) and enable advanced features.
        Args:
            additional_owners: A comma-separated list of user IDs to set as additional owners allowed to use the returned media_id in Tweets or Cards. Up to 100 additional owners may be specified.
        Args:
            command: The type of command to use.
            body: Request body
        Returns:
            upload_media_response: Response data
        """
        url = self.client.base_url + "/2/media/upload"
        params = {}
        if media_id is not None:
            params["media_id"] = media_id
        if total_bytes is not None:
            params["total_bytes"] = total_bytes
        if media_type is not None:
            params["media_type"] = media_type
        if media_category is not None:
            params["media_category"] = media_category
        if additional_owners is not None:
            params["additional_owners"] = additional_owners
        if command is not None:
            params["command"] = command
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
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
        return upload_media_response.model_validate(response_data)


    def create_subtitles(
        self,
        body: Optional[create_subtitles_request] = None,
    ) -> create_subtitles_response:
        """
        Subtitle Create
        SubtitleCreate
            body: Request body
        Returns:
            create_subtitles_response: Response data
        """
        url = self.client.base_url + "/2/media/subtitles"
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
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
        return create_subtitles_response.model_validate(response_data)


    def delete_subtitles(
        self,
        body: Optional[delete_subtitles_request] = None,
    ) -> delete_subtitles_response:
        """
        Subtitle Delete
        SubtitleDelete
            body: Request body
        Returns:
            delete_subtitles_response: Response data
        """
        url = self.client.base_url + "/2/media/subtitles"
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
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
        return delete_subtitles_response.model_validate(response_data)


    def metadata_create(
        self,
        body: Optional[metadata_create_request] = None,
    ) -> metadata_create_response:
        """
        Metadata Create
        MetadataCreate
            body: Request body
        Returns:
            metadata_create_response: Response data
        """
        url = self.client.base_url + "/2/media/metadata"
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
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
        return metadata_create_response.model_validate(response_data)
