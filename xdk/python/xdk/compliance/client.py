"""
Auto-generated compliance client for the X API.

This module provides a client for interacting with the compliance endpoints of the X API.

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
    GetJobsByIdResponse,
    GetJobsResponse,
    CreateJobsRequest,
    CreateJobsResponse,
)


class ComplianceClient:
    """Client for compliance operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_jobs_by_id(self, id: Any) -> GetJobsByIdResponse:
        """
        Get Compliance Job by ID
        Retrieves details of a specific Compliance Job by its ID.
        Args:
            id: The ID of the Compliance Job to retrieve.
            Returns:
            GetJobsByIdResponse: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs/{id}"
        url = url.replace("{id}", str(id))
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
        return GetJobsByIdResponse.model_validate(response_data)


    def get_jobs(self, type: str, status: str = None) -> GetJobsResponse:
        """
        Get Compliance Jobs
        Retrieves a list of Compliance Jobs filtered by job type and optional status.
        Args:
            type: Type of Compliance Job to list.
            status: Status of Compliance Job to list.
            Returns:
            GetJobsResponse: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if type is not None:
            params["type"] = type
        if status is not None:
            params["status"] = status
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
        return GetJobsResponse.model_validate(response_data)


    def create_jobs(self, body: CreateJobsRequest) -> CreateJobsResponse:
        """
        Create Compliance Job
        Creates a new Compliance Job for the specified job type.
        body: A request to create a new batch compliance job.
        Returns:
            CreateJobsResponse: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
        return CreateJobsResponse.model_validate(response_data)
