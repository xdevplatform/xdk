"""
Stream client for the X API.

This module provides a client for interacting with the Stream endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    
    
    StreampostsfirehosekoResponse,
    
    
    
    StreamlikesfirehoseResponse,
    
    
    
    StreampostsResponse,
    
    
    
    Streamlikessample10Response,
    
    
    
    StreampostsfirehosejaResponse,
    
    
    
    StreampostsfirehoseenResponse,
    
    
    
    GetrulecountsResponse,
    
    
    
    StreamlabelscomplianceResponse,
    
    
    
    StreampostsfirehoseResponse,
    
    
    
    StreampostssampleResponse,
    
    
    
    StreampostsfirehoseptResponse,
    
    
    
    StreampostscomplianceResponse,
    
    
    
    Streampostssample10Response,
    
    
    
    StreamlikescomplianceResponse,
    
    
    
    StreamuserscomplianceResponse,
    
    
    
    GetrulesResponse,
    
    
    
    UpdaterulesRequest,
    
    UpdaterulesResponse,
    
    
    
)

class StreamClient:
    """Client for Stream operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def stream_posts_firehose_ko(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostsfirehosekoResponse:
        """
        Stream Korean Posts
        
        
        Streams all public Korean-language Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostsfirehosekoResponse: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostsfirehosekoResponse.model_validate(response_data)
        
    
    def stream_likes_firehose(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        like_with_tweet_author_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> StreamlikesfirehoseResponse:
        """
        Stream all Likes
        
        
        Streams all public Likes in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            like_with_tweet_author_fields: A comma separated list of LikeWithTweetAuthor fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            StreamlikesfirehoseResponse: Response data
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
            
        
        
        
        
        
        if like_with_tweet_author_fields is not None:
            
            params["like_with_tweet_author.fields"] = ",".join(str(item) for item in like_with_tweet_author_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreamlikesfirehoseResponse.model_validate(response_data)
        
    
    def stream_posts(self, 
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostsResponse:
        """
        Stream filtered Posts
        
        
        Streams Posts in real-time matching the active rule set.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostsResponse: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostsResponse.model_validate(response_data)
        
    
    def stream_likes_sample10(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        like_with_tweet_author_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        
    ) -> Streamlikessample10Response:
        """
        Stream sampled Likes
        
        
        Streams a 10% sample of public Likes in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Likes will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            like_with_tweet_author_fields: A comma separated list of LikeWithTweetAuthor fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        
        Returns:
            Streamlikessample10Response: Response data
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
            
        
        
        
        
        
        if like_with_tweet_author_fields is not None:
            
            params["like_with_tweet_author.fields"] = ",".join(str(item) for item in like_with_tweet_author_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return Streamlikessample10Response.model_validate(response_data)
        
    
    def stream_posts_firehose_ja(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostsfirehosejaResponse:
        """
        Stream Japanese Posts
        
        
        Streams all public Japanese-language Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostsfirehosejaResponse: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostsfirehosejaResponse.model_validate(response_data)
        
    
    def stream_posts_firehose_en(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostsfirehoseenResponse:
        """
        Stream English Posts
        
        
        Streams all public English-language Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostsfirehoseenResponse: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostsfirehoseenResponse.model_validate(response_data)
        
    
    def get_rule_counts(self, 
        
        
        
        
        
        
        
        rules_count_fields: List = None,
        
        
        
        
    ) -> GetrulecountsResponse:
        """
        Get stream rule counts
        
        
        Retrieves the count of rules in the active rule set for the filtered stream.
        
        
        
        
        Args:
            rules_count_fields: A comma separated list of RulesCount fields to display.
        
        
        
        
        Returns:
            GetrulecountsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules/counts"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        if rules_count_fields is not None:
            
            params["rules_count.fields"] = ",".join(str(item) for item in rules_count_fields)
            
        
        
        
        
        
        
        
        
        
        
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
        
        return GetrulecountsResponse.model_validate(response_data)
        
    
    def stream_labels_compliance(self, 
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> StreamlabelscomplianceResponse:
        """
        Stream Post labels
        
        
        Streams all labeling events applied to Posts.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post labels will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Post labels will be provided.
        
        
        
        
        Returns:
            StreamlabelscomplianceResponse: Response data
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
        
        return StreamlabelscomplianceResponse.model_validate(response_data)
        
    
    def stream_posts_firehose(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostsfirehoseResponse:
        """
        Stream all Posts
        
        
        Streams all public Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostsfirehoseResponse: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostsfirehoseResponse.model_validate(response_data)
        
    
    def stream_posts_sample(self, 
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostssampleResponse:
        """
        Stream sampled Posts
        
        
        Streams a 1% sample of public Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostssampleResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/sample/stream"

        

        
        
        
        
        
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
        
        
        
        
        params = {}
        
        
        
        if backfill_minutes is not None:
            
            params["backfill_minutes"] = backfill_minutes
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostssampleResponse.model_validate(response_data)
        
    
    def stream_posts_firehose_pt(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> StreampostsfirehoseptResponse:
        """
        Stream Portuguese Posts
        
        
        Streams all public Portuguese-language Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            StreampostsfirehoseptResponse: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return StreampostsfirehoseptResponse.model_validate(response_data)
        
    
    def stream_posts_compliance(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> StreampostscomplianceResponse:
        """
        Stream Posts compliance data
        
        
        Streams all compliance data related to Posts.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Post Compliance events will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Post Compliance events will be provided.
        
        
        
        
        Returns:
            StreampostscomplianceResponse: Response data
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
        
        return StreampostscomplianceResponse.model_validate(response_data)
        
    
    def stream_posts_sample10(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        tweet_fields: List = None,
        
        
        
        expansions: List = None,
        
        
        
        media_fields: List = None,
        
        
        
        poll_fields: List = None,
        
        
        
        user_fields: List = None,
        
        
        
        place_fields: List = None,
        
        
        
        
    ) -> Streampostssample10Response:
        """
        Stream 10% sampled Posts
        
        
        Streams a 10% sample of public Posts in real-time.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided.
        
        
        
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        
        
        
        Args:
            expansions: A comma separated list of fields to expand.
        
        
        
        Args:
            media_fields: A comma separated list of Media fields to display.
        
        
        
        Args:
            poll_fields: A comma separated list of Poll fields to display.
        
        
        
        Args:
            user_fields: A comma separated list of User fields to display.
        
        
        
        Args:
            place_fields: A comma separated list of Place fields to display.
        
        
        
        
        Returns:
            Streampostssample10Response: Response data
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
            
        
        
        
        
        
        if tweet_fields is not None:
            
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
            
        
        
        
        
        
        if expansions is not None:
            
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        
        
        
        
        
        if media_fields is not None:
            
            params["media.fields"] = ",".join(str(item) for item in media_fields)
            
        
        
        
        
        
        if poll_fields is not None:
            
            params["poll.fields"] = ",".join(str(item) for item in poll_fields)
            
        
        
        
        
        
        if user_fields is not None:
            
            params["user.fields"] = ",".join(str(item) for item in user_fields)
            
        
        
        
        
        
        if place_fields is not None:
            
            params["place.fields"] = ",".join(str(item) for item in place_fields)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        return Streampostssample10Response.model_validate(response_data)
        
    
    def stream_likes_compliance(self, 
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> StreamlikescomplianceResponse:
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
            StreamlikescomplianceResponse: Response data
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
        
        return StreamlikescomplianceResponse.model_validate(response_data)
        
    
    def stream_users_compliance(self, 
        
        
        
        partition: int,
        
        
        
        
        
        
        
        backfill_minutes: int = None,
        
        
        
        start_time: str = None,
        
        
        
        end_time: str = None,
        
        
        
        
    ) -> StreamuserscomplianceResponse:
        """
        Stream Users compliance data
        
        
        Streams all compliance data related to Users.
        
        
        
        
        Args:
            backfill_minutes: The number of minutes of backfill requested.
        
        
        
        Args:
            partition: The partition number.
        
        
        
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.
        
        
        
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.
        
        
        
        
        Returns:
            StreamuserscomplianceResponse: Response data
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
        
        return StreamuserscomplianceResponse.model_validate(response_data)
        
    
    def get_rules(self, 
        
        
        
        
        
        
        
        ids: List = None,
        
        
        
        max_results: int = None,
        
        
        
        pagination_token: str = None,
        
        
        
        
    ) -> GetrulesResponse:
        """
        Get stream rules
        
        
        Retrieves the active rule set or a subset of rules for the filtered stream.
        
        
        
        
        Args:
            ids: A comma-separated list of Rule IDs.
        
        
        
        Args:
            max_results: The maximum number of results.
        
        
        
        Args:
            pagination_token: This value is populated by passing the 'next_token' returned in a request to paginate through results.
        
        
        
        
        Returns:
            GetrulesResponse: Response data
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
        
        return GetrulesResponse.model_validate(response_data)
        
    
    def update_rules(self, 
        
        
        
        
        body: UpdaterulesRequest,
        
        
        
        
        dry_run: bool = None,
        
        
        
        delete_all: bool = None,
        
        
        
        
    ) -> UpdaterulesResponse:
        """
        Update stream rules
        
        
        Adds or deletes rules from the active rule set for the filtered stream.
        
        
        
        
        Args:
            dry_run: Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
        
        
        
        Args:
            delete_all: Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.
        
        
        
        
        
        
        
            body: Request body
        
        
        
        
        Returns:
            UpdaterulesResponse: Response data
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
        
        return UpdaterulesResponse.model_validate(response_data)
        
    