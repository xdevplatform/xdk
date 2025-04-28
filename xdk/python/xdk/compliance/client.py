"""
Compliance client for the X API.

This module provides a client for interacting with the Compliance endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import requests_oauthlib
from ..client import Client
from .models import (
    list_batch_compliance_jobs_response,
    create_batch_compliance_job_request,
    create_batch_compliance_job_response,
    get_tweets_label_stream_response,
    get_likes_compliance_stream_response,
    get_users_compliance_stream_response,
    get_tweets_compliance_stream_response,
    get_batch_compliance_job_response,
)


class ComplianceClient:
    """Client for Compliance operations"""


    def __init__(self, client: Client):
        self.client = client


    def list_batch_compliance_jobs(
        self,
        type: str,
        status: str = None,
        compliance_job_fields: List = None,
    ) -> list_batch_compliance_jobs_response:
        """
        List Compliance Jobs
        Returns recent Compliance Jobs for a given job type and optional job status
        Args:
            type: Type of Compliance Job to list.
        Args:
            status: Status of Compliance Job to list.
        Args:
            compliance_job_fields: A comma separated list of ComplianceJob fields to display.
        Returns:
            list_batch_compliance_jobs_response: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
        params = {}
        if type is not None:
            params["type"] = type
        if status is not None:
            params["status"] = status
        if compliance_job_fields is not None:
            params["compliance_job.fields"] = compliance_job_fields
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
        return list_batch_compliance_jobs_response.model_validate(response_data)


    def create_batch_compliance_job(
        self,
        body: create_batch_compliance_job_request,
    ) -> create_batch_compliance_job_response:
        """
        Create compliance job
        Creates a compliance for the given job type
            body: A request to create a new batch compliance job.
        Returns:
            create_batch_compliance_job_response: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
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
        return create_batch_compliance_job_response.model_validate(response_data)


    def get_tweets_label_stream(
        self,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
    ) -> get_tweets_label_stream_response:
        """
        Posts Label stream
        Streams 100% of labeling events applied to Posts
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.
        Returns:
            get_tweets_label_stream_response: Response data
        """
        url = self.client.base_url + "/2/tweets/label/stream"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
        params = {}
        if backfill_minutes is not None:
            params["backfill_minutes"] = backfill_minutes
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
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
        return get_tweets_label_stream_response.model_validate(response_data)


    def get_likes_compliance_stream(
        self,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
    ) -> get_likes_compliance_stream_response:
        """
        Likes Compliance stream
        Streams 100% of compliance data for Users
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided.
        Returns:
            get_likes_compliance_stream_response: Response data
        """
        url = self.client.base_url + "/2/likes/compliance/stream"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
        params = {}
        if backfill_minutes is not None:
            params["backfill_minutes"] = backfill_minutes
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
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
        return get_likes_compliance_stream_response.model_validate(response_data)


    def get_users_compliance_stream(
        self,
        partition: int,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
    ) -> get_users_compliance_stream_response:
        """
        Users Compliance stream
        Streams 100% of compliance data for Users
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        Args:
            partition: The partition number.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
        Returns:
            get_users_compliance_stream_response: Response data
        """
        url = self.client.base_url + "/2/users/compliance/stream"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
        params = {}
        if backfill_minutes is not None:
            params["backfill_minutes"] = backfill_minutes
        if partition is not None:
            params["partition"] = partition
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
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
        return get_users_compliance_stream_response.model_validate(response_data)


    def get_tweets_compliance_stream(
        self,
        partition: int,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
    ) -> get_tweets_compliance_stream_response:
        """
        Posts Compliance stream
        Streams 100% of compliance data for Posts
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        Args:
            partition: The partition number.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.
        Returns:
            get_tweets_compliance_stream_response: Response data
        """
        url = self.client.base_url + "/2/tweets/compliance/stream"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
        params = {}
        if backfill_minutes is not None:
            params["backfill_minutes"] = backfill_minutes
        if partition is not None:
            params["partition"] = partition
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
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
        return get_tweets_compliance_stream_response.model_validate(response_data)


    def get_batch_compliance_job(
        self,
        id: str,
        compliance_job_fields: List = None,
    ) -> get_batch_compliance_job_response:
        """
        Get Compliance Job
        Returns a single Compliance Job by ID
        Args:
            id: The ID of the Compliance Job to retrieve.
        Args:
            compliance_job_fields: A comma separated list of ComplianceJob fields to display.
        Returns:
            get_batch_compliance_job_response: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs/{id}"
        self.client.session.headers["Authorization"] = f"Bearer {self.client.token}"
        params = {}
        if compliance_job_fields is not None:
            params["compliance_job.fields"] = compliance_job_fields
        url = url.replace("{id}", str(id))
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
        return get_batch_compliance_job_response.model_validate(response_data)
