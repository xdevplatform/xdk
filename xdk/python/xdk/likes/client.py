"""
Likes client for the X API.

This module provides a client for interacting with the Likes endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    StreamlikesfirehoseResponse,
    Streamlikessample10Response,
)


class LikesClient:
    """Client for Likes operations"""

    def __init__(self, client: Client):
        self.client = client

    def stream_likes_firehose(
        self,
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
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )

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

            params["like_with_tweet_author.fields"] = ",".join(
                str(item) for item in like_with_tweet_author_fields
            )

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

    def stream_likes_sample10(
        self,
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
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )

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

            params["like_with_tweet_author.fields"] = ",".join(
                str(item) for item in like_with_tweet_author_fields
            )

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
