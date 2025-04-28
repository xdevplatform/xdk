"""
Likes client for the X API.

This module provides a client for interacting with the Likes endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import requests_oauthlib
from ..client import Client
from .models import likes_sample10_stream_response, likes_firehose_stream_response


class LikesClient:
    """Client for Likes operations"""


    def __init__(self, client: Client):
        self.client = client


    def likes_sample10_stream(
        self,
        partition: int,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
        like_with_tweet_author_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> likes_sample10_stream_response:
        """
        Likes Sample 10 stream
        Streams 10% of public Likes.
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
            likes_sample10_stream_response: Response data
        """
        url = self.client.base_url + "/2/likes/sample10/stream"
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
        if like_with_tweet_author_fields is not None:
            params["like_with_tweet_author.fields"] = like_with_tweet_author_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
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
        return likes_sample10_stream_response.model_validate(response_data)


    def likes_firehose_stream(
        self,
        partition: int,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
        like_with_tweet_author_fields: List = None,
        expansions: List = None,
        user_fields: List = None,
        tweet_fields: List = None,
    ) -> likes_firehose_stream_response:
        """
        Likes Firehose stream
        Streams 100% of public Likes.
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
            likes_firehose_stream_response: Response data
        """
        url = self.client.base_url + "/2/likes/firehose/stream"
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
        if like_with_tweet_author_fields is not None:
            params["like_with_tweet_author.fields"] = like_with_tweet_author_fields
        if expansions is not None:
            params["expansions"] = expansions
        if user_fields is not None:
            params["user.fields"] = user_fields
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
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
        return likes_firehose_stream_response.model_validate(response_data)
