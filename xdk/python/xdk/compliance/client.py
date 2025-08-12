"""
compliance client for the X API.

This module provides a client for interacting with the compliance endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    GetJobsResponse,
    CreateJobsRequest,
    CreateJobsResponse,
    GetJobsByIdResponse,
)


class ComplianceClient:
    """Client for compliance operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_jobs(
        self,
        type: str,
        status: str = None,
        compliance_job_fields: List = None,
    ) -> GetJobsResponse:
        """
        Get Compliance Jobs
        Retrieves a list of Compliance Jobs filtered by job type and optional status.
        Args:
            type: Type of Compliance Job to list.
        Args:
            status: Status of Compliance Job to list.
        Args:
            compliance_job_fields: A comma separated list of ComplianceJob fields to display.
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
        if compliance_job_fields is not None:
            params["compliance_job.fields"] = ",".join(
                str(item) for item in compliance_job_fields
            )
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
        return GetJobsResponse.model_validate(response_data)


    def create_jobs(
        self,
        body: CreateJobsRequest,
    ) -> CreateJobsResponse:
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
        return CreateJobsResponse.model_validate(response_data)


    def get_jobs_by_id(
        self,
        id: str,
        compliance_job_fields: List = None,
    ) -> GetJobsByIdResponse:
        """
        Get Compliance Job by ID
        Retrieves details of a specific Compliance Job by its ID.
        Args:
            id: The ID of the Compliance Job to retrieve.
        Args:
            compliance_job_fields: A comma separated list of ComplianceJob fields to display.
        Returns:
            GetJobsByIdResponse: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs/{id}"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if compliance_job_fields is not None:
            params["compliance_job.fields"] = ",".join(
                str(item) for item in compliance_job_fields
            )
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
        return GetJobsByIdResponse.model_validate(response_data)
