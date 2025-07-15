"""
Compliance client for the X API.

This module provides a client for interacting with the Compliance endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from .models import 2_users_compliance_stream_response, 2_tweets_compliance_stream_response, 2_tweets_label_stream_response, 2_compliance_jobs_id_response, 2_likes_compliance_stream_response, 2_compliance_jobs_response, 2_compliance_jobs_request, 2_compliance_jobs_response

class ComplianceClient:
    """Client for Compliance operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def 2_users_compliance_stream(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> 2_users_compliance_stream_response:
        """
        Stream Users compliance data
        
        
        Streams all compliance data related to Users in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
        
        
        
        
        Returns:
            2_users_compliance_stream_response: Response data
        """
        url = self.client.base_url + "/2/users/compliance/stream"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
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
        
        return 2_users_compliance_stream_response.model_validate(response_data)
        
    
    def 2_tweets_compliance_stream(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> 2_tweets_compliance_stream_response:
        """
        Stream Posts compliance data
        
        
        Streams all compliance data related to Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.
        
        
        
        
        Returns:
            2_tweets_compliance_stream_response: Response data
        """
        url = self.client.base_url + "/2/tweets/compliance/stream"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
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
        
        return 2_tweets_compliance_stream_response.model_validate(response_data)
        
    
    def 2_tweets_label_stream(self, 
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> 2_tweets_label_stream_response:
        """
        Stream Post labels
        
        
        Streams all labeling events applied to Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.
        
        
        
        
        Returns:
            2_tweets_label_stream_response: Response data
        """
        url = self.client.base_url + "/2/tweets/label/stream"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
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
        
        return 2_tweets_label_stream_response.model_validate(response_data)
        
    
    def 2_compliance_jobs_id(self, 
        
        
        
        id: str,
        
        
        
        
        
        
        
        compliance_job_fields: List = None,
        
        
        
        
    ) -> 2_compliance_jobs_id_response:
        """
        Get Compliance Job by ID
        
        
        Retrieves details of a specific Compliance Job by its ID.
        
        
        
        
        Args:
            id: The ID of the Compliance Job to retrieve.
        
        
        
        Args:
            compliance_job_fields: A comma separated list of ComplianceJob fields to display.
        
        
        
        
        Returns:
            2_compliance_jobs_id_response: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs/{id}"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        
        
        
        
        if compliance_job_fields is not None:
            
            params["compliance_job.fields"] = ",".join(str(item) for item in compliance_job_fields)
            
        
        
        
        
        
        
        
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
        
        return 2_compliance_jobs_id_response.model_validate(response_data)
        
    
    def 2_likes_compliance_stream(self, 
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> 2_likes_compliance_stream_response:
        """
        Stream Likes compliance data
        
        
        Streams all compliance data related to Likes for Users.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided.
        
        
        
        
        Returns:
            2_likes_compliance_stream_response: Response data
        """
        url = self.client.base_url + "/2/likes/compliance/stream"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
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
        
        return 2_likes_compliance_stream_response.model_validate(response_data)
        
    
    def 2_compliance_jobs(self, 
        
        
        
        type: str,
        
        
        
        
        
        
        
        status: str = None,
        
        
        
        compliance_job_fields: List = None,
        
        
        
        
    ) -> 2_compliance_jobs_response:
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
            2_compliance_jobs_response: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        if type is not None:
            
            params["type"] = type
            
        
        
        
        
        
        if status is not None:
            
            params["status"] = status
            
        
        
        
        
        
        if compliance_job_fields is not None:
            
            params["compliance_job.fields"] = ",".join(str(item) for item in compliance_job_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return 2_compliance_jobs_response.model_validate(response_data)
        
    
    def 2_compliance_jobs(self, 
        
        
        
        
        body: 2_compliance_jobs_request,
        
        
        
        
        
    ) -> 2_compliance_jobs_response:
        """
        Create Compliance Job
        
        
        Creates a new Compliance Job for the specified job type.
        
        
        
        
        
        
        
        
            body: A request to create a new batch compliance job.
        
        
        
        
        Returns:
            2_compliance_jobs_response: Response data
        """
        url = self.client.base_url + "/2/compliance/jobs"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
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
        
        return 2_compliance_jobs_response.model_validate(response_data)
        
    