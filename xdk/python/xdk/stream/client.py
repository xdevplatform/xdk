
"""
Auto-generated stream client for the X API.

This module provides a client for interacting with the stream endpoints of the X API.
Real-time streaming operations return generators that yield data as it arrives.
All methods, parameters, and response models are generated from the OpenAPI specification.

Generated automatically - do not edit manually.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING, Iterator, Generator
import requests
import time
import json

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    
    
    PostsSample10Response,
    
    
    
    PostsFirehoseResponse,
    
    
    
    PostsFirehoseJaResponse,
    
    
    
    PostsFirehosePtResponse,
    
    
    
    PostsComplianceResponse,
    
    
    
    GetRulesResponse,
    
    
    
    UpdateRulesRequest,
    
    UpdateRulesResponse,
    
    
    
    
    LikesFirehoseResponse,
    
    
    
    PostsFirehoseKoResponse,
    
    
    
    GetRuleCountsResponse,
    
    
    
    LabelsComplianceResponse,
    
    
    
    PostsFirehoseEnResponse,
    
    
    
    LikesSample10Response,
    
    
    
    UsersComplianceResponse,
    
    
    
    LikesComplianceResponse,
    
    
    
    PostsResponse,
    
    
    
    PostsSampleResponse,
    
    
)

class StreamClient:
    """Streaming Client for stream operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def posts_sample10(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsSample10Response, None, None]:
        """
        Stream 10% sampled Posts (Streaming)
        
        Streams a 10% sample of public Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsSample10Response: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/sample10/stream"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsSample10Response.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsSample10Response.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_firehose(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsFirehoseResponse, None, None]:
        """
        Stream all Posts (Streaming)
        
        Streams all public Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsFirehoseResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/firehose/stream"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsFirehoseResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsFirehoseResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_firehose_ja(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsFirehoseJaResponse, None, None]:
        """
        Stream Japanese Posts (Streaming)
        
        Streams all public Japanese-language Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsFirehoseJaResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/ja"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsFirehoseJaResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsFirehoseJaResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_firehose_pt(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsFirehosePtResponse, None, None]:
        """
        Stream Portuguese Posts (Streaming)
        
        Streams all public Portuguese-language Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsFirehosePtResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/pt"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsFirehosePtResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsFirehosePtResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_compliance(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsComplianceResponse, None, None]:
        """
        Stream Posts compliance data (Streaming)
        
        Streams all compliance data related to Posts.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsComplianceResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
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
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsComplianceResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsComplianceResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def get_rules(self, ids: List = None, max_results: int = None, pagination_token: str = None) -> GetRulesResponse:
        """
        Get stream rules
        
        Retrieves the active rule set or a subset of rules for the filtered stream.
        
        Args:
            ids: A comma-separated list of Rule IDs.
            max_results: The maximum number of results.
            pagination_token: This value is populated by passing the 'next_token' returned in a request to paginate through results.
            Returns:
            GetRulesResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        params = {}
        if ids is not None:
            params["ids"] = ",".join(str(item) for item in ids)
            
        if max_results is not None:
            params["max_results"] = max_results
            
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
            
        
        
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
        
        return GetRulesResponse.model_validate(response_data)
        
        

    
    def update_rules(self, body: UpdateRulesRequest, dry_run: bool = None, delete_all: bool = None) -> UpdateRulesResponse:
        """
        Update stream rules
        
        Adds or deletes rules from the active rule set for the filtered stream.
        
        Args:
            dry_run: Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
            delete_all: Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.
            body: Request body
        Returns:
            UpdateRulesResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        params = {}
        if dry_run is not None:
            params["dry_run"] = dry_run
            
        if delete_all is not None:
            params["delete_all"] = delete_all
            
        
        
        headers = {}
        headers["Content-Type"] = "application/json"
        
        
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = body.model_dump(exclude_none=True) if hasattr(body, 'model_dump') else body
        
        
        
        










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
        
        return UpdateRulesResponse.model_validate(response_data)
        
        

    
    def likes_firehose(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, like_with_tweet_authorfields: List = None, expansions: List = None, userfields: List = None, tweetfields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[LikesFirehoseResponse, None, None]:
        """
        Stream all Likes (Streaming)
        
        Streams all public Likes in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            like_with_tweet_authorfields: A comma separated list of LikeWithTweetAuthor fields to display.
            expansions: A comma separated list of fields to expand.
            userfields: A comma separated list of User fields to display.
            tweetfields: A comma separated list of Tweet fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            LikesFirehoseResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/likes/firehose/stream"
        

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
            
        if like_with_tweet_authorfields is not None:
            params["like_with_tweet_author.fields"] = ",".join(str(item) for item in like_with_tweet_authorfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield LikesFirehoseResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield LikesFirehoseResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_firehose_ko(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsFirehoseKoResponse, None, None]:
        """
        Stream Korean Posts (Streaming)
        
        Streams all public Korean-language Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsFirehoseKoResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/ko"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsFirehoseKoResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsFirehoseKoResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def get_rule_counts(self, rules_countfields: List = None) -> GetRuleCountsResponse:
        """
        Get stream rule counts
        
        Retrieves the count of rules in the active rule set for the filtered stream.
        
        Args:
            rules_countfields: A comma separated list of RulesCount fields to display.
            Returns:
            GetRuleCountsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules/counts"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        params = {}
        if rules_countfields is not None:
            params["rules_count.fields"] = ",".join(str(item) for item in rules_countfields)
            
        
        
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
        
        return GetRuleCountsResponse.model_validate(response_data)
        
        

    
    def labels_compliance(self, backfill_minutes: int = None, start_time: str = None, end_time: str = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[LabelsComplianceResponse, None, None]:
        """
        Stream Post labels (Streaming)
        
        Streams all labeling events applied to Posts.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            LabelsComplianceResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
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
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield LabelsComplianceResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield LabelsComplianceResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_firehose_en(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsFirehoseEnResponse, None, None]:
        """
        Stream English Posts (Streaming)
        
        Streams all public English-language Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsFirehoseEnResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/en"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsFirehoseEnResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsFirehoseEnResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def likes_sample10(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, like_with_tweet_authorfields: List = None, expansions: List = None, userfields: List = None, tweetfields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[LikesSample10Response, None, None]:
        """
        Stream sampled Likes (Streaming)
        
        Streams a 10% sample of public Likes in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            like_with_tweet_authorfields: A comma separated list of LikeWithTweetAuthor fields to display.
            expansions: A comma separated list of fields to expand.
            userfields: A comma separated list of User fields to display.
            tweetfields: A comma separated list of Tweet fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            LikesSample10Response: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/likes/sample10/stream"
        

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
            
        if like_with_tweet_authorfields is not None:
            params["like_with_tweet_author.fields"] = ",".join(str(item) for item in like_with_tweet_authorfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield LikesSample10Response.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield LikesSample10Response.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def users_compliance(self, partition: int, backfill_minutes: int = None, start_time: str = None, end_time: str = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[UsersComplianceResponse, None, None]:
        """
        Stream Users compliance data (Streaming)
        
        Streams all compliance data related to Users.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            partition: The partition number.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            UsersComplianceResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
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
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield UsersComplianceResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield UsersComplianceResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def likes_compliance(self, backfill_minutes: int = None, start_time: str = None, end_time: str = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[LikesComplianceResponse, None, None]:
        """
        Stream Likes compliance data (Streaming)
        
        Streams all compliance data related to Likes for Users.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Likes Compliance events will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Likes Compliance events will be provided.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            LikesComplianceResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
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
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield LikesComplianceResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield LikesComplianceResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts(self, backfill_minutes: int = None, start_time: str = None, end_time: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsResponse, None, None]:
        """
        Stream filtered Posts (Streaming)
        
        Streams Posts in real-time matching the active rule set.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/search/stream"
        

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
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    
    def posts_sample(self, backfill_minutes: int = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None, timeout: Optional[float] = None, chunk_size: int = 1024) -> Generator[PostsSampleResponse, None, None]:
        """
        Stream sampled Posts (Streaming)
        
        Streams a 1% sample of public Posts in real-time.
        
        This is a streaming endpoint that yields data in real-time as it becomes available.
        Each yielded item represents a single data point from the stream.
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            timeout: Request timeout in seconds (default: None for no timeout)
            chunk_size: Size of chunks to read from the stream (default: 1024 bytes)
        
        Yields:
            PostsSampleResponse: Individual streaming data items
        
        Raises:
            requests.exceptions.RequestException: If the streaming connection fails
            json.JSONDecodeError: If the streamed data is not valid JSON
        """
        url = self.client.base_url + "/2/tweets/sample/stream"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        params = {}
        if backfill_minutes is not None:
            params["backfill_minutes"] = backfill_minutes
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if mediafields is not None:
            params["media.fields"] = ",".join(str(item) for item in mediafields)
            
        if pollfields is not None:
            params["poll.fields"] = ",".join(str(item) for item in pollfields)
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if placefields is not None:
            params["place.fields"] = ",".join(str(item) for item in placefields)
            
        
        
        headers = {
            "Accept": "application/json",
        }
        
        
        # Prepare request data
        json_data = None
        
        
        
        try:
            # Make streaming request
            with self.client.session.get(
                url,
                params=params,
                headers=headers,
                
                stream=True,
                timeout=timeout,
            ) as response:
                # Check for HTTP errors
                response.raise_for_status()
                
                # Buffer for incomplete lines
                buffer = ""
                
                # Stream data chunk by chunk
                for chunk in response.iter_content(chunk_size=chunk_size, decode_unicode=True):
                    if chunk:
                        # Ensure chunk is always a string, not bytes
                        if isinstance(chunk, bytes):
                            chunk = chunk.decode('utf-8')
                        buffer += chunk
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line:
                                try:
                                    # Parse JSON line
                                    data = json.loads(line)
                                    
                                    # Convert to response model if available
                                    
                                    yield PostsSampleResponse.model_validate(data)
                                    
                                    
                                except json.JSONDecodeError:
                                    # Skip invalid JSON lines
                                    continue
                                except Exception:
                                    # Skip lines that cause processing errors
                                    continue
                
                # Process any remaining data in buffer
                if buffer.strip():
                    try:
                        data = json.loads(buffer.strip())
                        
                        yield PostsSampleResponse.model_validate(data)
                        
                    except json.JSONDecodeError:
                        # Skip invalid JSON in final buffer
                        pass
        except requests.exceptions.RequestException:
            raise
        except Exception:
            raise
        

    