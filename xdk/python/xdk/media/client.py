"""
Auto-generated media client for the X API.

This module provides a client for interacting with the media endpoints of the X API.

All methods, parameters, and response models are generated from the OpenAPI specification.

Generated automatically - do not edit manually.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time


if TYPE_CHECKING:
    from ..client import Client
from .models import (
    GetByKeyResponse,
    CreateSubtitlesRequest,
    CreateSubtitlesResponse,
    DeleteSubtitlesRequest,
    DeleteSubtitlesResponse,
    CreateMetadataRequest,
    CreateMetadataResponse,
    GetAnalyticsResponse,
    AppendUploadRequest,
    AppendUploadResponse,
    InitializeUploadRequest,
    InitializeUploadResponse,
    FinalizeUploadResponse,
    GetByKeysResponse,
    GetUploadStatusResponse,
    UploadRequest,
    UploadResponse,
)


class MediaClient:
    """Client for media operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_by_key(self, media_key: Any) -> GetByKeyResponse:
        """
        Get Media by media key
        Retrieves details of a specific Media file by its media key.
        Args:
            media_key: A single Media Key.
            Returns:
            GetByKeyResponse: Response data
        """
        url = self.client.base_url + "/2/media/{media_key}"
        url = url.replace("{media_key}", str(media_key))
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
        headers = {}
        # Prepare request data
        json_data = None
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
        return GetByKeyResponse.model_validate(response_data)


    def create_subtitles(
        self, body: Optional[CreateSubtitlesRequest] = None
    ) -> CreateSubtitlesResponse:
        """
        Create Media subtitles
        Creates subtitles for a specific Media file.
        body: Request body
        Returns:
            CreateSubtitlesResponse: Response data
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
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateSubtitlesResponse.model_validate(response_data)


    def delete_subtitles(
        self, body: Optional[DeleteSubtitlesRequest] = None
    ) -> DeleteSubtitlesResponse:
        """
        Delete Media subtitles
        Deletes subtitles for a specific Media file.
        body: Request body
        Returns:
            DeleteSubtitlesResponse: Response data
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
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.delete(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return DeleteSubtitlesResponse.model_validate(response_data)


    def create_metadata(
        self, body: Optional[CreateMetadataRequest] = None
    ) -> CreateMetadataResponse:
        """
        Create Media metadata
        Creates metadata for a Media file.
        body: Request body
        Returns:
            CreateMetadataResponse: Response data
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
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return CreateMetadataResponse.model_validate(response_data)


    def get_analytics(
        self, media_keys: List, end_time: str, start_time: str, granularity: str
    ) -> GetAnalyticsResponse:
        """
        Get Media analytics
        Retrieves analytics data for media.
        Args:
            media_keys: A comma separated list of Media Keys. Up to 100 are allowed in a single request.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
            granularity: The granularity for the search counts results.
            Returns:
            GetAnalyticsResponse: Response data
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
        headers = {}
        # Prepare request data
        json_data = None
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
        return GetAnalyticsResponse.model_validate(response_data)


    def append_upload(
        self, id: Any, body: Optional[AppendUploadRequest] = None
    ) -> AppendUploadResponse:
        """
        Append Media upload
        Appends data to a Media upload request.
        Args:
            id: The media identifier for the media to perform the append operation.
            body: Request body
        Returns:
            AppendUploadResponse: Response data
        """
        url = self.client.base_url + "/2/media/upload/{id}/append"
        url = url.replace("{id}", str(id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return AppendUploadResponse.model_validate(response_data)


    def initialize_upload(
        self, body: Optional[InitializeUploadRequest] = None
    ) -> InitializeUploadResponse:
        """
        Initialize media upload
        Initializes a media upload.
        body: Request body
        Returns:
            InitializeUploadResponse: Response data
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
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return InitializeUploadResponse.model_validate(response_data)


    def finalize_upload(self, id: Any) -> FinalizeUploadResponse:
        """
        Finalize Media upload
        Finalizes a Media upload request.
        Args:
            id: The media id of the targeted media to finalize.
            Returns:
            FinalizeUploadResponse: Response data
        """
        url = self.client.base_url + "/2/media/upload/{id}/finalize"
        url = url.replace("{id}", str(id))
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        headers = {}
        # Prepare request data
        json_data = None
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
        return FinalizeUploadResponse.model_validate(response_data)


    def get_by_keys(self, media_keys: List) -> GetByKeysResponse:
        """
        Get Media by media keys
        Retrieves details of Media files by their media keys.
        Args:
            media_keys: A comma separated list of Media Keys. Up to 100 are allowed in a single request.
            Returns:
            GetByKeysResponse: Response data
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
        headers = {}
        # Prepare request data
        json_data = None
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
        return GetByKeysResponse.model_validate(response_data)


    def get_upload_status(
        self, media_id: Any, command: str = None
    ) -> GetUploadStatusResponse:
        """
        Get Media upload status
        Retrieves the status of a Media upload by its ID.
        Args:
            media_id: Media id for the requested media upload status.
            command: The command for the media upload request.
            Returns:
            GetUploadStatusResponse: Response data
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
        # Prepare request data
        json_data = None
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
        return GetUploadStatusResponse.model_validate(response_data)


    def upload(self, body: Optional[UploadRequest] = None) -> UploadResponse:
        """
        Upload media
        Uploads a media file for use in posts or other content.
        body: Request body
        Returns:
            UploadResponse: Response data
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
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
                json=json_data,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return UploadResponse.model_validate(response_data)
