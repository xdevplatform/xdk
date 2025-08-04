"""
Tweets client for the X API.

This module provides a client for interacting with the Tweets endpoints of the X API.
"""

from __future__ import annotations
from typing import Dict, List, Optional, Any, Union, cast, TYPE_CHECKING
import requests
import time

if TYPE_CHECKING:
    from ..client import Client
from .models import (
    Streampostssample10Response,
    GetspacespostsResponse,
    GetlistspostsResponse,
    GetpostscountsrecentResponse,
    SearchpostsrecentResponse,
    GetpostscountsallResponse,
    StreampostsfirehoseResponse,
    GetrulecountsResponse,
    StreampostsfirehoseenResponse,
    LikepostRequest,
    LikepostResponse,
    GetpostsanalyticsResponse,
    StreampostsfirehosekoResponse,
    StreampostsResponse,
    GetpostsquotedpostsResponse,
    GetusersmentionsResponse,
    UnlikepostResponse,
    GetpostsbyidResponse,
    DeletepostsResponse,
    SearchpostsallResponse,
    HidepostsreplyRequest,
    HidepostsreplyResponse,
    StreampostssampleResponse,
    GetuserstimelineResponse,
    GetuserspostsResponse,
    GetspacesbuyersResponse,
    RepostpostRequest,
    RepostpostResponse,
    Getinsights28hrResponse,
    GetpostsbyidsResponse,
    CreatepostsRequest,
    CreatepostsResponse,
    GetuserslikedpostsResponse,
    GetinsightshistoricalResponse,
    StreampostsfirehosejaResponse,
    StreampostsfirehoseptResponse,
    UnrepostpostResponse,
    GetpostsrepostsResponse,
    GetrulesResponse,
    UpdaterulesRequest,
    UpdaterulesResponse,
)


class TweetsClient:
    """Client for Tweets operations"""


    def __init__(self, client: Client):
        self.client = client


    def stream_posts_sample10(
        self,
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


    def get_spaces_posts(
        self,
        id: str,
        max_results: int = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetspacespostsResponse:
        """
        Get Space Posts
        Retrieves a list of Posts shared in a specific Space by its ID.
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            max_results: The number of Posts to fetch from the provided space. If not provided, the value will default to the maximum of 100.
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
            GetspacespostsResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/tweets"
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
        if max_results is not None:
            params["max_results"] = max_results
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
        return GetspacespostsResponse.model_validate(response_data)


    def get_lists_posts(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetlistspostsResponse:
        """
        Get List Posts
        Retrieves a list of Posts associated with a specific List by its ID.
        Args:
            id: The ID of the List.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
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
            GetlistspostsResponse: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/tweets"
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
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        return GetlistspostsResponse.model_validate(response_data)


    def get_posts_counts_recent(
        self,
        query: str,
        start_time: str = None,
        end_time: str = None,
        since_id: str = None,
        until_id: str = None,
        next_token: str = None,
        pagination_token: str = None,
        granularity: str = None,
        search_count_fields: List = None,
    ) -> GetpostscountsrecentResponse:
        """
        Get count of recent Posts
        Retrieves the count of Posts from the last 7 days matching a search query.
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        Args:
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
        Args:
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            granularity: The granularity for the search counts results.
        Args:
            search_count_fields: A comma separated list of SearchCount fields to display.
        Returns:
            GetpostscountsrecentResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/counts/recent"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if query is not None:
            params["query"] = query
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if next_token is not None:
            params["next_token"] = next_token
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if granularity is not None:
            params["granularity"] = granularity
        if search_count_fields is not None:
            params["search_count.fields"] = ",".join(
                str(item) for item in search_count_fields
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
        return GetpostscountsrecentResponse.model_validate(response_data)


    def search_posts_recent(
        self,
        query: str,
        start_time: str = None,
        end_time: str = None,
        since_id: str = None,
        until_id: str = None,
        max_results: int = None,
        next_token: str = None,
        pagination_token: str = None,
        sort_order: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> SearchpostsrecentResponse:
        """
        Search recent Posts
        Retrieves Posts from the last 7 days matching a search query.
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        Args:
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
        Args:
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
        Args:
            max_results: The maximum number of search results to be returned by a request.
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            sort_order: This order in which to return results.
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
            SearchpostsrecentResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/recent"
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
        if query is not None:
            params["query"] = query
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if max_results is not None:
            params["max_results"] = max_results
        if next_token is not None:
            params["next_token"] = next_token
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if sort_order is not None:
            params["sort_order"] = sort_order
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
        return SearchpostsrecentResponse.model_validate(response_data)


    def get_posts_counts_all(
        self,
        query: str,
        start_time: str = None,
        end_time: str = None,
        since_id: str = None,
        until_id: str = None,
        next_token: str = None,
        pagination_token: str = None,
        granularity: str = None,
        search_count_fields: List = None,
    ) -> GetpostscountsallResponse:
        """
        Get count of all Posts
        Retrieves the count of Posts matching a search query from the full archive.
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        Args:
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
        Args:
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            granularity: The granularity for the search counts results.
        Args:
            search_count_fields: A comma separated list of SearchCount fields to display.
        Returns:
            GetpostscountsallResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/counts/all"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if query is not None:
            params["query"] = query
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if next_token is not None:
            params["next_token"] = next_token
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if granularity is not None:
            params["granularity"] = granularity
        if search_count_fields is not None:
            params["search_count.fields"] = ",".join(
                str(item) for item in search_count_fields
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
        return GetpostscountsallResponse.model_validate(response_data)


    def stream_posts_firehose(
        self,
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


    def get_rule_counts(
        self,
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
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if rules_count_fields is not None:
            params["rules_count.fields"] = ",".join(
                str(item) for item in rules_count_fields
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
        return GetrulecountsResponse.model_validate(response_data)


    def stream_posts_firehose_en(
        self,
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


    def like_post(
        self,
        id: str,
        body: Optional[LikepostRequest] = None,
    ) -> LikepostResponse:
        """
        Like Post
        Causes the authenticated user to Like a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to like the Post.
            body: Request body
        Returns:
            LikepostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/likes"
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
        return LikepostResponse.model_validate(response_data)


    def get_posts_analytics(
        self,
        ids: List,
        end_time: str,
        start_time: str,
        granularity: str,
        analytics_fields: List = None,
    ) -> GetpostsanalyticsResponse:
        """
        Get Post analytics
        Retrieves analytics data for specified Posts within a defined time range.
        Args:
            ids: A comma separated list of Post IDs. Up to 100 are allowed in a single request.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
        Args:
            granularity: The granularity for the search counts results.
        Args:
            analytics_fields: A comma separated list of Analytics fields to display.
        Returns:
            GetpostsanalyticsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/analytics"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if ids is not None:
            params["ids"] = ",".join(str(item) for item in ids)
        if end_time is not None:
            params["end_time"] = end_time
        if start_time is not None:
            params["start_time"] = start_time
        if granularity is not None:
            params["granularity"] = granularity
        if analytics_fields is not None:
            params["analytics.fields"] = ",".join(
                str(item) for item in analytics_fields
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
        return GetpostsanalyticsResponse.model_validate(response_data)


    def stream_posts_firehose_ko(
        self,
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


    def stream_posts(
        self,
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


    def get_posts_quoted_posts(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        exclude: List = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetpostsquotedpostsResponse:
        """
        Get Quoted Posts
        Retrieves a list of Posts that quote a specific Post by its ID.
        Args:
            id: A single Post ID.
        Args:
            max_results: The maximum number of results to be returned.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            exclude: The set of entities to exclude (e.g. 'replies' or 'retweets').
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
            GetpostsquotedpostsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/quote_tweets"
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
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if exclude is not None:
            params["exclude"] = ",".join(str(item) for item in exclude)
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
        return GetpostsquotedpostsResponse.model_validate(response_data)


    def get_users_mentions(
        self,
        id: str,
        since_id: str = None,
        until_id: str = None,
        max_results: int = None,
        pagination_token: str = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetusersmentionsResponse:
        """
        Get mentions
        Retrieves a list of Posts that mention a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
        Args:
            since_id: The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
        Args:
            until_id: The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
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
            GetusersmentionsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/mentions"
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
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        return GetusersmentionsResponse.model_validate(response_data)


    def unlike_post(
        self,
        id: str,
        tweet_id: str,
    ) -> UnlikepostResponse:
        """
        Unlike Post
        Causes the authenticated user to Unlike a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to unlike the Post.
        Args:
            tweet_id: The ID of the Post that the User is requesting to unlike.
        Returns:
            UnlikepostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/likes/{tweet_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{tweet_id}", str(tweet_id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.delete(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return UnlikepostResponse.model_validate(response_data)


    def get_posts_by_id(
        self,
        id: str,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetpostsbyidResponse:
        """
        Get Post by ID
        Retrieves details of a specific Post by its ID.
        Args:
            id: A single Post ID.
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
            GetpostsbyidResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}"
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
        return GetpostsbyidResponse.model_validate(response_data)


    def delete_posts(
        self,
        id: str,
    ) -> DeletepostsResponse:
        """
        Delete Post
        Deletes a specific Post by its ID, if owned by the authenticated user.
        Args:
            id: The ID of the Post to be deleted.
        Returns:
            DeletepostsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}"
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
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.delete(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return DeletepostsResponse.model_validate(response_data)


    def search_posts_all(
        self,
        query: str,
        start_time: str = None,
        end_time: str = None,
        since_id: str = None,
        until_id: str = None,
        max_results: int = None,
        next_token: str = None,
        pagination_token: str = None,
        sort_order: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> SearchpostsallResponse:
        """
        Search all Posts
        Retrieves Posts from the full archive matching a search query.
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
        Args:
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
        Args:
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
        Args:
            max_results: The maximum number of search results to be returned by a request.
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            sort_order: This order in which to return results.
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
            SearchpostsallResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/all"
        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
        params = {}
        if query is not None:
            params["query"] = query
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if max_results is not None:
            params["max_results"] = max_results
        if next_token is not None:
            params["next_token"] = next_token
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if sort_order is not None:
            params["sort_order"] = sort_order
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
        return SearchpostsallResponse.model_validate(response_data)


    def hide_posts_reply(
        self,
        tweet_id: str,
        body: Optional[HidepostsreplyRequest] = None,
    ) -> HidepostsreplyResponse:
        """
        Hide reply
        Hides or unhides a reply to a conversation owned by the authenticated user.
        Args:
            tweet_id: The ID of the reply that you want to hide or unhide.
            body: Request body
        Returns:
            HidepostsreplyResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{tweet_id}/hidden"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{tweet_id}", str(tweet_id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.put(
                url,
                params=params,
                headers=headers,
                json=body.model_dump(exclude_none=True) if body else None,
            )
        else:
            response = self.client.session.put(
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
        return HidepostsreplyResponse.model_validate(response_data)


    def stream_posts_sample(
        self,
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


    def get_users_timeline(
        self,
        id: str,
        since_id: str = None,
        until_id: str = None,
        max_results: int = None,
        pagination_token: str = None,
        exclude: List = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetuserstimelineResponse:
        """
        Get Timeline
        Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
        Args:
            id: The ID of the authenticated source User to list Reverse Chronological Timeline Posts of.
        Args:
            since_id: The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
        Args:
            until_id: The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Args:
            exclude: The set of entities to exclude (e.g. 'replies' or 'retweets').
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
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
            GetuserstimelineResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/timelines/reverse_chronological"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if exclude is not None:
            params["exclude"] = ",".join(str(item) for item in exclude)
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
        url = url.replace("{id}", str(id))
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
        return GetuserstimelineResponse.model_validate(response_data)


    def get_users_posts(
        self,
        id: str,
        since_id: str = None,
        until_id: str = None,
        max_results: int = None,
        pagination_token: str = None,
        exclude: List = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetuserspostsResponse:
        """
        Get Posts
        Retrieves a list of posts authored by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
        Args:
            since_id: The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
        Args:
            until_id: The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Args:
            exclude: The set of entities to exclude (e.g. 'replies' or 'retweets').
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
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
            GetuserspostsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/tweets"
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
        if since_id is not None:
            params["since_id"] = since_id
        if until_id is not None:
            params["until_id"] = until_id
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if exclude is not None:
            params["exclude"] = ",".join(str(item) for item in exclude)
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
        return GetuserspostsResponse.model_validate(response_data)


    def get_spaces_buyers(
        self,
        id: str,
        pagination_token: str = None,
        max_results: int = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> GetspacesbuyersResponse:
        """
        Get Space ticket buyers
        Retrieves a list of Users who purchased tickets to a specific Space by its ID.
        Args:
            id: The ID of the Space to be retrieved.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            max_results: The maximum number of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            GetspacesbuyersResponse: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/buyers"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        if max_results is not None:
            params["max_results"] = max_results
        if user_fields is not None:
            params["user.fields"] = ",".join(str(item) for item in user_fields)
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
        if tweet_fields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweet_fields)
        url = url.replace("{id}", str(id))
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
        return GetspacesbuyersResponse.model_validate(response_data)


    def repost_post(
        self,
        id: str,
        body: Optional[RepostpostRequest] = None,
    ) -> RepostpostResponse:
        """
        Repost Post
        Causes the authenticated user to repost a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
            body: Request body
        Returns:
            RepostpostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/retweets"
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
        return RepostpostResponse.model_validate(response_data)


    def get_insights28_hr(
        self,
        tweet_ids: List,
        granularity: str,
        requested_metrics: List,
        engagement_fields: List = None,
    ) -> Getinsights28hrResponse:
        """
        Get 28-hour Post insights
        Retrieves engagement metrics for specified Posts over the last 28 hours.
        Args:
            tweet_ids: List of PostIds for 28hr metrics.
        Args:
            granularity: granularity of metrics response.
        Args:
            requested_metrics: request metrics for historical request.
        Args:
            engagement_fields: A comma separated list of Engagement fields to display.
        Returns:
            Getinsights28hrResponse: Response data
        """
        url = self.client.base_url + "/2/insights/28hr"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if tweet_ids is not None:
            params["tweet_ids"] = ",".join(str(item) for item in tweet_ids)
        if granularity is not None:
            params["granularity"] = granularity
        if requested_metrics is not None:
            params["requested_metrics"] = ",".join(
                str(item) for item in requested_metrics
            )
        if engagement_fields is not None:
            params["engagement.fields"] = ",".join(
                str(item) for item in engagement_fields
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
        return Getinsights28hrResponse.model_validate(response_data)


    def get_posts_by_ids(
        self,
        ids: List,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetpostsbyidsResponse:
        """
        Get Posts by IDs
        Retrieves details of multiple Posts by their IDs.
        Args:
            ids: A comma separated list of Post IDs. Up to 100 are allowed in a single request.
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
            GetpostsbyidsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets"
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
        if ids is not None:
            params["ids"] = ",".join(str(item) for item in ids)
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
        return GetpostsbyidsResponse.model_validate(response_data)


    def create_posts(
        self,
        body: CreatepostsRequest,
    ) -> Dict[str, Any]:
        """
        Create Post
        Creates a new Post for the authenticated user.
            body: Request body
        Returns:
            CreatepostsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets"
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
        return CreatepostsResponse.model_validate(response_data)


    def get_users_liked_posts(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetuserslikedpostsResponse:
        """
        Get liked Posts
        Retrieves a list of Posts liked by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
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
            GetuserslikedpostsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/liked_tweets"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        url = url.replace("{id}", str(id))
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
        return GetuserslikedpostsResponse.model_validate(response_data)


    def get_insights_historical(
        self,
        tweet_ids: List,
        end_time: str,
        start_time: str,
        granularity: str,
        requested_metrics: List,
        engagement_fields: List = None,
    ) -> GetinsightshistoricalResponse:
        """
        Get historical Post insights
        Retrieves historical engagement metrics for specified Posts within a defined time range.
        Args:
            tweet_ids: List of PostIds for historical metrics.
        Args:
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
        Args:
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
        Args:
            granularity: granularity of metrics response.
        Args:
            requested_metrics: request metrics for historical request.
        Args:
            engagement_fields: A comma separated list of Engagement fields to display.
        Returns:
            GetinsightshistoricalResponse: Response data
        """
        url = self.client.base_url + "/2/insights/historical"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if tweet_ids is not None:
            params["tweet_ids"] = ",".join(str(item) for item in tweet_ids)
        if end_time is not None:
            params["end_time"] = end_time
        if start_time is not None:
            params["start_time"] = start_time
        if granularity is not None:
            params["granularity"] = granularity
        if requested_metrics is not None:
            params["requested_metrics"] = ",".join(
                str(item) for item in requested_metrics
            )
        if engagement_fields is not None:
            params["engagement.fields"] = ",".join(
                str(item) for item in engagement_fields
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
        return GetinsightshistoricalResponse.model_validate(response_data)


    def stream_posts_firehose_ja(
        self,
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


    def stream_posts_firehose_pt(
        self,
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


    def unrepost_post(
        self,
        id: str,
        source_tweet_id: str,
    ) -> UnrepostpostResponse:
        """
        Unrepost Post
        Causes the authenticated user to unrepost a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
        Args:
            source_tweet_id: The ID of the Post that the User is requesting to unretweet.
        Returns:
            UnrepostpostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/retweets/{source_tweet_id}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{source_tweet_id}", str(source_tweet_id))
        headers = {}
        # Make the request
        if self.client.oauth2_session:
            response = self.client.oauth2_session.delete(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.delete(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return UnrepostpostResponse.model_validate(response_data)


    def get_posts_reposts(
        self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> GetpostsrepostsResponse:
        """
        Get Reposts
        Retrieves a list of Posts that repost a specific Post by its ID.
        Args:
            id: A single Post ID.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
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
            GetpostsrepostsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/retweets"
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
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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
        return GetpostsrepostsResponse.model_validate(response_data)


    def get_rules(
        self,
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
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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


    def update_rules(
        self,
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
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.bearer_token}"
            )
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = (
                f"Bearer {self.client.access_token}"
            )
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
