"""
Tweets client for the X API.

This module provides a client for interacting with the Tweets endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union, cast
import requests
import time
from ..client import Client
from .models import (
    get_tweets_firehose_stream_response,
    space_buyers_response,
    get_tweets_firehose_stream_lang_en_response,
    find_tweet_by_id_response,
    delete_tweet_by_id_response,
    get_tweets_firehose_stream_lang_pt_response,
    users_id_retweets_request,
    users_id_retweets_response,
    lists_id_tweets_response,
    sample_stream_response,
    users_id_like_request,
    users_id_like_response,
    tweets_recent_search_response,
    twenty_eight_hours_engagement_api_response,
    get_tweets_firehose_stream_lang_ja_response,
    get_tweets_firehose_stream_lang_ko_response,
    get_tweets_sample10_stream_response,
    search_stream_response,
    users_id_mentions_response,
    users_id_unlike_response,
    users_id_unretweets_response,
    historical_engagement_api_response,
    users_id_liked_tweets_response,
    find_tweets_that_retweet_a_tweet_response,
    get_rules_response,
    add_or_delete_rules_request,
    add_or_delete_rules_response,
    users_id_tweets_response,
    find_tweets_by_id_response,
    create_tweet_request,
    create_tweet_response,
    tweets_fullarchive_search_response,
    users_id_timeline_response,
    space_tweets_response,
    tweet_counts_full_archive_search_response,
    find_tweets_that_quote_a_tweet_response,
    hide_reply_by_id_request,
    hide_reply_by_id_response,
    tweet_counts_recent_search_response,
)


class TweetsClient:
    """Client for Tweets operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_tweets_firehose_stream(
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
    ) -> get_tweets_firehose_stream_response:
        """
        Firehose stream
        Streams 100% of public Posts.
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
            get_tweets_firehose_stream_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_tweets_firehose_stream_response.model_validate(response_data)


    def space_buyers(
        self,
        id: str,
        pagination_token: str = None,
        max_results: int = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> space_buyers_response:
        """
        Retrieve the list of Users who purchased a ticket to the given space
        Retrieves the list of Users who purchased a ticket to the given space
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
            space_buyers_response: Response data
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
            params["user.fields"] = user_fields
        if expansions is not None:
            params["expansions"] = expansions
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
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
        return space_buyers_response.model_validate(response_data)


    def get_tweets_firehose_stream_lang_en(
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
    ) -> get_tweets_firehose_stream_lang_en_response:
        """
        English Language Firehose stream
        Streams 100% of English Language public Posts.
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
            get_tweets_firehose_stream_lang_en_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_tweets_firehose_stream_lang_en_response.model_validate(response_data)


    def find_tweet_by_id(
        self,
        id: str,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> find_tweet_by_id_response:
        """
        Post lookup by Post ID
        Returns a variety of information about the Post specified by the requested ID.
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
            find_tweet_by_id_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return find_tweet_by_id_response.model_validate(response_data)


    def delete_tweet_by_id(
        self,
        id: str,
    ) -> delete_tweet_by_id_response:
        """
        Post delete by Post ID
        Delete specified Post (in the path) by ID.
        Args:
            id: The ID of the Post to be deleted.
        Returns:
            delete_tweet_by_id_response: Response data
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
        return delete_tweet_by_id_response.model_validate(response_data)


    def get_tweets_firehose_stream_lang_pt(
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
    ) -> get_tweets_firehose_stream_lang_pt_response:
        """
        Portuguese Language Firehose stream
        Streams 100% of Portuguese Language public Posts.
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
            get_tweets_firehose_stream_lang_pt_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_tweets_firehose_stream_lang_pt_response.model_validate(response_data)


    def users_id_retweets(
        self,
        id: str,
        body: Optional[users_id_retweets_request] = None,
    ) -> users_id_retweets_response:
        """
        Causes the User (in the path) to repost the specified Post.
        Causes the User (in the path) to repost the specified Post. The User in the path must match the User context authorizing the request.
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
            body: Request body
        Returns:
            users_id_retweets_response: Response data
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
        return users_id_retweets_response.model_validate(response_data)


    def lists_id_tweets(
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
    ) -> lists_id_tweets_response:
        """
        List Posts timeline by List ID.
        Returns a list of Posts associated with the provided List ID.
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
            lists_id_tweets_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return lists_id_tweets_response.model_validate(response_data)


    def sample_stream(
        self,
        backfill_minutes: int = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> sample_stream_response:
        """
        Sample stream
        Streams a deterministic 1% of public Posts.
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
            sample_stream_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return sample_stream_response.model_validate(response_data)


    def users_id_like(
        self,
        id: str,
        body: Optional[users_id_like_request] = None,
    ) -> users_id_like_response:
        """
        Causes the User (in the path) to like the specified Post
        Causes the User (in the path) to like the specified Post. The User in the path must match the User context authorizing the request.
        Args:
            id: The ID of the authenticated source User that is requesting to like the Post.
            body: Request body
        Returns:
            users_id_like_response: Response data
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
        return users_id_like_response.model_validate(response_data)


    def tweets_recent_search(
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
    ) -> tweets_recent_search_response:
        """
        Recent search
        Returns Posts from the last 7 days that match a search query.
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
            tweets_recent_search_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return tweets_recent_search_response.model_validate(response_data)


    def twenty_eight_hours_engagement_api(
        self,
        tweet_ids: List,
        granularity: str,
        requested_metrics: List,
        engagement_fields: List = None,
    ) -> twenty_eight_hours_engagement_api_response:
        """
        Get Last 28hr Metrics for Posts
        Get 28hr Metrics for Posts.
        Args:
            tweet_ids: List of PostIds for 28hr metrics.
        Args:
            granularity: granularity of metrics response.
        Args:
            requested_metrics: request metrics for historical request.
        Args:
            engagement_fields: A comma separated list of Engagement fields to display.
        Returns:
            twenty_eight_hours_engagement_api_response: Response data
        """
        url = self.client.base_url + "/2/insights/28hr"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if tweet_ids is not None:
            params["tweet_ids"] = tweet_ids
        if granularity is not None:
            params["granularity"] = granularity
        if requested_metrics is not None:
            params["requested_metrics"] = requested_metrics
        if engagement_fields is not None:
            params["engagement.fields"] = engagement_fields
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
        return twenty_eight_hours_engagement_api_response.model_validate(response_data)


    def get_tweets_firehose_stream_lang_ja(
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
    ) -> get_tweets_firehose_stream_lang_ja_response:
        """
        Japanese Language Firehose stream
        Streams 100% of Japanese Language public Posts.
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
            get_tweets_firehose_stream_lang_ja_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_tweets_firehose_stream_lang_ja_response.model_validate(response_data)


    def get_tweets_firehose_stream_lang_ko(
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
    ) -> get_tweets_firehose_stream_lang_ko_response:
        """
        Korean Language Firehose stream
        Streams 100% of Korean Language public Posts.
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
            get_tweets_firehose_stream_lang_ko_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_tweets_firehose_stream_lang_ko_response.model_validate(response_data)


    def get_tweets_sample10_stream(
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
    ) -> get_tweets_sample10_stream_response:
        """
        Sample 10% stream
        Streams a deterministic 10% of public Posts.
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
            get_tweets_sample10_stream_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return get_tweets_sample10_stream_response.model_validate(response_data)


    def search_stream(
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
    ) -> search_stream_response:
        """
        Filtered stream
        Streams Posts matching the stream's active rule set.
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
            search_stream_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return search_stream_response.model_validate(response_data)


    def users_id_mentions(
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
    ) -> users_id_mentions_response:
        """
        User mention timeline by User ID
        Returns Post objects that mention username associated to the provided User ID
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
            users_id_mentions_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return users_id_mentions_response.model_validate(response_data)


    def users_id_unlike(
        self,
        id: str,
        tweet_id: str,
    ) -> users_id_unlike_response:
        """
        Causes the User (in the path) to unlike the specified Post
        Causes the User (in the path) to unlike the specified Post. The User must match the User context authorizing the request
        Args:
            id: The ID of the authenticated source User that is requesting to unlike the Post.
        Args:
            tweet_id: The ID of the Post that the User is requesting to unlike.
        Returns:
            users_id_unlike_response: Response data
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
        return users_id_unlike_response.model_validate(response_data)


    def users_id_unretweets(
        self,
        id: str,
        source_tweet_id: str,
    ) -> users_id_unretweets_response:
        """
        Causes the User (in the path) to unretweet the specified Post
        Causes the User (in the path) to unretweet the specified Post. The User must match the User context authorizing the request
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
        Args:
            source_tweet_id: The ID of the Post that the User is requesting to unretweet.
        Returns:
            users_id_unretweets_response: Response data
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
        return users_id_unretweets_response.model_validate(response_data)


    def historical_engagement_api(
        self,
        tweet_ids: List,
        end_time: str,
        start_time: str,
        granularity: str,
        requested_metrics: List,
        engagement_fields: List = None,
    ) -> historical_engagement_api_response:
        """
        Get Historical Metrics for Posts
        Get Historical Metrics for Posts.
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
            historical_engagement_api_response: Response data
        """
        url = self.client.base_url + "/2/insights/historical"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if tweet_ids is not None:
            params["tweet_ids"] = tweet_ids
        if end_time is not None:
            params["end_time"] = end_time
        if start_time is not None:
            params["start_time"] = start_time
        if granularity is not None:
            params["granularity"] = granularity
        if requested_metrics is not None:
            params["requested_metrics"] = requested_metrics
        if engagement_fields is not None:
            params["engagement.fields"] = engagement_fields
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
        return historical_engagement_api_response.model_validate(response_data)


    def users_id_liked_tweets(
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
    ) -> users_id_liked_tweets_response:
        """
        Returns Post objects liked by the provided User ID
        Returns a list of Posts liked by the provided User ID
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
            users_id_liked_tweets_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return users_id_liked_tweets_response.model_validate(response_data)


    def find_tweets_that_retweet_a_tweet(
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
    ) -> find_tweets_that_retweet_a_tweet_response:
        """
        Retrieve Posts that repost a Post.
        Returns a variety of information about each Post that has retweeted the Post specified by the requested ID.
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
            find_tweets_that_retweet_a_tweet_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return find_tweets_that_retweet_a_tweet_response.model_validate(response_data)


    def get_rules(
        self,
        ids: List = None,
        max_results: int = None,
        pagination_token: str = None,
    ) -> get_rules_response:
        """
        Rules lookup
        Returns rules from a User's active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.
        Args:
            ids: A comma-separated list of Rule IDs.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This value is populated by passing the 'next_token' returned in a request to paginate through results.
        Returns:
            get_rules_response: Response data
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
            params["ids"] = ids
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
        return get_rules_response.model_validate(response_data)


    def add_or_delete_rules(
        self,
        body: add_or_delete_rules_request,
        dry_run: bool = None,
        delete_all: bool = None,
    ) -> add_or_delete_rules_response:
        """
        Add/Delete rules
        Add or delete rules from a User's active rule set. Users can provide unique, optionally tagged rules to add. Users can delete their entire rule set or a subset specified by rule ids or values.
        Args:
            dry_run: Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
        Args:
            delete_all: Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.
            body: Request body
        Returns:
            add_or_delete_rules_response: Response data
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
        return add_or_delete_rules_response.model_validate(response_data)


    def users_id_tweets(
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
    ) -> users_id_tweets_response:
        """
        User Posts timeline by User ID
        Returns a list of Posts authored by the provided User ID
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
            users_id_tweets_response: Response data
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
            params["exclude"] = exclude
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return users_id_tweets_response.model_validate(response_data)


    def find_tweets_by_id(
        self,
        ids: List,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> find_tweets_by_id_response:
        """
        Post lookup by Post IDs
        Returns a variety of information about the Post specified by the requested ID.
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
            find_tweets_by_id_response: Response data
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
            params["ids"] = ids
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return find_tweets_by_id_response.model_validate(response_data)


    def create_tweet(
        self,
        body: create_tweet_request,
    ) -> Dict[str, Any]:
        """
        Creation of a Post
        Causes the User to create a Post under the authorized account.
            body: Request body
        Returns:
            create_tweet_response: Response data
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
        return create_tweet_response.model_validate(response_data)


    def tweets_fullarchive_search(
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
    ) -> tweets_fullarchive_search_response:
        """
        Full-archive search
        Returns Posts that match a search query.
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
            tweets_fullarchive_search_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return tweets_fullarchive_search_response.model_validate(response_data)


    def users_id_timeline(
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
    ) -> users_id_timeline_response:
        """
        User home timeline by User ID
        Returns Post objects that appears in the provided User ID's home timeline
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
            users_id_timeline_response: Response data
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
            params["exclude"] = exclude
        if start_time is not None:
            params["start_time"] = start_time
        if end_time is not None:
            params["end_time"] = end_time
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return users_id_timeline_response.model_validate(response_data)


    def space_tweets(
        self,
        id: str,
        max_results: int = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> space_tweets_response:
        """
        Retrieve Posts from a Space.
        Retrieves Posts shared in the specified Space.
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
            space_tweets_response: Response data
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
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return space_tweets_response.model_validate(response_data)


    def tweet_counts_full_archive_search(
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
    ) -> tweet_counts_full_archive_search_response:
        """
        Full archive search counts
        Returns Post Counts that match a search query.
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
            tweet_counts_full_archive_search_response: Response data
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
            params["search_count.fields"] = search_count_fields
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
        return tweet_counts_full_archive_search_response.model_validate(response_data)


    def find_tweets_that_quote_a_tweet(
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
    ) -> find_tweets_that_quote_a_tweet_response:
        """
        Retrieve Posts that quote a Post.
        Returns a variety of information about each Post that quotes the Post specified by the requested ID.
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
            find_tweets_that_quote_a_tweet_response: Response data
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
            params["exclude"] = exclude
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        if expansions is not None:
            params["expansions"] = expansions
        if media_fields is not None:
            params["media.fields"] = media_fields
        if poll_fields is not None:
            params["poll.fields"] = poll_fields
        if user_fields is not None:
            params["user.fields"] = user_fields
        if place_fields is not None:
            params["place.fields"] = place_fields
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
        return find_tweets_that_quote_a_tweet_response.model_validate(response_data)


    def hide_reply_by_id(
        self,
        tweet_id: str,
        body: Optional[hide_reply_by_id_request] = None,
    ) -> hide_reply_by_id_response:
        """
        Hide replies
        Hides or unhides a reply to an owned conversation.
        Args:
            tweet_id: The ID of the reply that you want to hide or unhide.
            body: Request body
        Returns:
            hide_reply_by_id_response: Response data
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
        return hide_reply_by_id_response.model_validate(response_data)


    def tweet_counts_recent_search(
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
    ) -> tweet_counts_recent_search_response:
        """
        Recent search counts
        Returns Post Counts from the last 7 days that match a search query.
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
            tweet_counts_recent_search_response: Response data
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
            params["search_count.fields"] = search_count_fields
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
        return tweet_counts_recent_search_response.model_validate(response_data)
