"""
Media client for the X API.

This module provides a client for interacting with the Media endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    CreateMediaMetadataRequest,
    CreateMediaMetadataResponse,
    CreateMediaSubtitlesRequest,
    CreateMediaSubtitlesResponse,
    DeleteMediaSubtitlesRequest,
    DeleteMediaSubtitlesResponse,
    GetMediaUploadStatusResponse,
    MediaUploadRequest,
    MediaUploadResponse,
    InitializeMediaUploadRequest,
    InitializeMediaUploadResponse,
    GetMediaAnalyticsResponse,
    GetMediaByMediaKeysResponse,
    GetMediaByMediaKeyResponse,
    FinalizeMediaUploadResponse,
    AppendMediaUploadRequest,
    AppendMediaUploadResponse,
)


class MediaClient:
    """Client for Media operations"""


    def __init__(self, client: Client):
        self.client = client


    def create_media_metadata(
        self,
        body: Optional[CreateMediaMetadataRequest] = None,
    ) -> CreateMediaMetadataResponse:
        """
        Create Media metadata
        Creates metadata for a Media file.
            body: Request body
        Returns:
            CreateMediaMetadataResponse: Response data
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
        return CreateMediaMetadataResponse.model_validate(response_data)


    def create_media_subtitles(
        self,
        body: Optional[CreateMediaSubtitlesRequest] = None,
    ) -> CreateMediaSubtitlesResponse:
        """
        Create Media subtitles
        Creates subtitles for a specific Media file.
            body: Request body
        Returns:
            CreateMediaSubtitlesResponse: Response data
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
        return CreateMediaSubtitlesResponse.model_validate(response_data)


    def delete_media_subtitles(
        self,
        body: Optional[DeleteMediaSubtitlesRequest] = None,
    ) -> DeleteMediaSubtitlesResponse:
        """
        Delete Media subtitles
        Deletes subtitles for a specific Media file.
            body: Request body
        Returns:
            DeleteMediaSubtitlesResponse: Response data
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
        return DeleteMediaSubtitlesResponse.model_validate(response_data)


    def get_media_upload_status(
        self,
        media_id: str,
        command: str = None,
    ) -> GetMediaUploadStatusResponse:
        """
        Get Media upload status
        Retrieves the status of a Media upload by its ID.
        Args:
            media_id: Media id for the requested media upload status.
        Args:
            command: The command for the media upload request.
        Returns:
            GetMediaUploadStatusResponse: Response data
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
        return GetMediaUploadStatusResponse.model_validate(response_data)


    def media_upload(
        self,
        body: Optional[MediaUploadRequest] = None,
    ) -> MediaUploadResponse:
        """
        Upload media
        Uploads a media file for use in posts or other content.
            body: Request body
        Returns:
            MediaUploadResponse: Response data
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
        return MediaUploadResponse.model_validate(response_data)


    def initialize_media_upload(
        self,
        body: Optional[InitializeMediaUploadRequest] = None,
    ) -> InitializeMediaUploadResponse:
        """
        Initialize media upload
        Initializes a media upload.
            body: Request body
        Returns:
            InitializeMediaUploadResponse: Response data
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
        return InitializeMediaUploadResponse.model_validate(response_data)


    def get_media_analytics(
        self,
        media_keys: List,
        end_time: str,
        start_time: str,
        granularity: str,
        media_analytics_fields: List = None,
    ) -> GetMediaAnalyticsResponse:
        """
        Get Media analytics
        Retrieves analytics data for media.
        Args:
            media_keys: A comma separated list of Media Keys. Up to 100 are allowed in a single request.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
        Args:
            granularity: The granularity for the search counts results.
        Args:
            media_analytics_fields: A comma separated list of MediaAnalytics fields to display.
        Returns:
            GetMediaAnalyticsResponse: Response data
        """
        url = self.client.base_url + "/2/media/analytics"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if media_keys is not None:
            params["media_keys"] = ",".join(str(item) for item in media_keys)
        if end_time is not None:
            params["end_time"] = end_time
        if start_time is not None:
            params["start_time"] = start_time
        if granularity is not None:
            params["granularity"] = granularity
        if media_analytics_fields is not None:
            params["media_analytics.fields"] = ",".join(
                str(item) for item in media_analytics_fields
            )
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
        return GetMediaAnalyticsResponse.model_validate(response_data)


    def get_media_by_media_keys(
        self,
        media_keys: List,
        media_fields: List = None,
    ) -> GetMediaByMediaKeysResponse:
        """
        Get Media by media keys
        Retrieves details of Media files by their media keys.
        Args:
            media_keys: A comma separated list of Media Keys. Up to 100 are allowed in a single request.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Returns:
            GetMediaByMediaKeysResponse: Response data
        """
        url = self.client.base_url + "/2/media"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if media_keys is not None:
            params["media_keys"] = ",".join(str(item) for item in media_keys)
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
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
        return GetMediaByMediaKeysResponse.model_validate(response_data)


    def get_media_by_media_key(
        self,
        media_key: str,
        media_fields: List = None,
    ) -> GetMediaByMediaKeyResponse:
        """
        Get Media by media key
        Retrieves details of a specific Media file by its media key.
        Args:
            media_key: A single Media Key.
        Args:
            media_fields: A comma separated list of Media fields to display.
        Returns:
            GetMediaByMediaKeyResponse: Response data
        """
        url = self.client.base_url + "/2/media/{media_key}"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if media_fields is not None:
            params["media.fields"] = ",".join(str(item) for item in media_fields)
        url = url.replace("{media_key}", str(media_key))
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
        return GetMediaByMediaKeyResponse.model_validate(response_data)


    def finalize_media_upload(
        self,
        id: str,
    ) -> FinalizeMediaUploadResponse:
        """
        Finalize Media upload
        Finalizes a Media upload request.
        Args:
            id: The media id of the targeted media to finalize.
        Returns:
            FinalizeMediaUploadResponse: Response data
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
        return FinalizeMediaUploadResponse.model_validate(response_data)


    def append_media_upload(
        self,
        id: str,
        body: Optional[AppendMediaUploadRequest] = None,
    ) -> AppendMediaUploadResponse:
        """
        Append Media upload
        Appends data to a Media upload request.
        Args:
            id: The media identifier for the media to perform the append operation.
            body: Request body
        Returns:
            AppendMediaUploadResponse: Response data
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
        return AppendMediaUploadResponse.model_validate(response_data)
