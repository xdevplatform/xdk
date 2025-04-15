"""
Tweets client for the X API.

This module provides a client for interacting with the Tweets endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class TweetsClient:
    """Client for Tweets operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_rules(self,
        ids: List = None,
        max_results: int = None,
        pagination_token: str = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules"
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
        # Return the response data
        return response.json()


    def add_or_delete_rules(self,
        body: Any,
        dry_run: bool = None,
        delete_all: bool = None,
    ) -> Dict[str, Any]:
        """
        Add/Delete rules
        Add or delete rules from a User's active rule set. Users can provide unique, optionally tagged rules to add. Users can delete their entire rule set or a subset specified by rule ids or values.
        Args:
            dry_run: Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.
        Args:
            delete_all: Delete All can be used to delete all of the rules associated this client app, it should be specified with no other parameters. Once deleted, rules cannot be recovered.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream/rules"
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
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def users_id_retweets(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Causes the User (in the path) to repost the specified Post.
        Causes the User (in the path) to repost the specified Post. The User in the path must match the User context authorizing the request.
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/retweets"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def get_tweets_firehose_stream_lang_en(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/en"
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
        # Return the response data
        return response.json()


    def users_id_timeline(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/timelines/reverse_chronological"
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
        # Return the response data
        return response.json()


    def space_buyers(self,
        id: str,
        pagination_token: str = None,
        max_results: int = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/buyers"
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
        response = self.client.session.get(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def find_tweets_that_quote_a_tweet(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/quote_tweets"
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
        # Return the response data
        return response.json()


    def tweet_counts_recent_search(self,
        query: str,
        start_time: str = None,
        end_time: str = None,
        since_id: str = None,
        until_id: str = None,
        next_token: str = None,
        pagination_token: str = None,
        granularity: str = None,
        search_count_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/counts/recent"
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
        # Return the response data
        return response.json()


    def get_tweets_firehose_stream_lang_ko(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/ko"
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
        # Return the response data
        return response.json()


    def historical_engagement_api(self,
        tweet_ids: List,
        end_time: str,
        start_time: str,
        granularity: str,
        requested_metrics: List,
        engagement_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/insights/historical"
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
        response = self.client.session.get(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def find_tweet_by_id(self,
        id: str,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}"
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
        # Return the response data
        return response.json()


    def delete_tweet_by_id(self,
        id: str,
    ) -> Dict[str, Any]:
        """
        Post delete by Post ID
        Delete specified Post (in the path) by ID.
        Args:
            id: The ID of the Post to be deleted.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def users_id_liked_tweets(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/liked_tweets"
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
        # Return the response data
        return response.json()


    def get_tweets_sample10_stream(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/sample10/stream"
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
        # Return the response data
        return response.json()


    def tweets_fullarchive_search(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/search/all"
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
        # Return the response data
        return response.json()


    def users_id_like(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Causes the User (in the path) to like the specified Post
        Causes the User (in the path) to like the specified Post. The User in the path must match the User context authorizing the request.
        Args:
            id: The ID of the authenticated source User that is requesting to like the Post.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/likes"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def space_tweets(self,
        id: str,
        max_results: int = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/spaces/{id}/tweets"
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
        # Return the response data
        return response.json()


    def users_id_unretweets(self,
        id: str,
        source_tweet_id: str,
    ) -> Dict[str, Any]:
        """
        Causes the User (in the path) to unretweet the specified Post
        Causes the User (in the path) to unretweet the specified Post. The User must match the User context authorizing the request
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
        Args:
            source_tweet_id: The ID of the Post that the User is requesting to unretweet.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/retweets/{source_tweet_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{source_tweet_id}", str(source_tweet_id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def search_stream(self,
        backfill_minutes: int = None,
        start_time: str = None,
        end_time: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/search/stream"
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
        # Return the response data
        return response.json()


    def users_id_mentions(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/mentions"
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
        # Return the response data
        return response.json()


    def find_tweets_that_retweet_a_tweet(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/retweets"
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
        # Return the response data
        return response.json()


    def users_id_tweets(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/tweets"
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
        # Return the response data
        return response.json()


    def tweets_recent_search(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/search/recent"
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
        # Return the response data
        return response.json()


    def sample_stream(self,
        backfill_minutes: int = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/sample/stream"
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
        # Return the response data
        return response.json()


    def users_id_unlike(self,
        id: str,
        tweet_id: str,
    ) -> Dict[str, Any]:
        """
        Causes the User (in the path) to unlike the specified Post
        Causes the User (in the path) to unlike the specified Post. The User must match the User context authorizing the request
        Args:
            id: The ID of the authenticated source User that is requesting to unlike the Post.
        Args:
            tweet_id: The ID of the Post that the User is requesting to unlike.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/likes/{tweet_id}"
        params = {}
        url = url.replace("{id}", str(id))
        url = url.replace("{tweet_id}", str(tweet_id))
        headers = {}
        # Make the request
        response = self.client.session.delete(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def twenty_eight_hours_engagement_api(self,
        tweet_ids: List,
        granularity: str,
        requested_metrics: List,
        engagement_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/insights/28hr"
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
        response = self.client.session.get(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def get_tweets_firehose_stream(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/firehose/stream"
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
        # Return the response data
        return response.json()


    def get_tweets_firehose_stream_lang_ja(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/ja"
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
        # Return the response data
        return response.json()


    def lists_id_tweets(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/tweets"
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
        # Return the response data
        return response.json()


    def tweet_counts_full_archive_search(self,
        query: str,
        start_time: str = None,
        end_time: str = None,
        since_id: str = None,
        until_id: str = None,
        next_token: str = None,
        pagination_token: str = None,
        granularity: str = None,
        search_count_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/counts/all"
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
        # Return the response data
        return response.json()


    def get_tweets_firehose_stream_lang_pt(self,
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
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/firehose/stream/lang/pt"
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
        # Return the response data
        return response.json()


    def find_tweets_by_id(self,
        ids: List,
        tweet_fields: List = None,
        expansions: List = None,
        media_fields: List = None,
        poll_fields: List = None,
        user_fields: List = None,
        place_fields: List = None,
    ) -> Dict[str, Any]:
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
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets"
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
        # Return the response data
        return response.json()


    def create_tweet(self,
        body: Dict[str, Any]
              ,
    ) -> Dict[str, Any]:
        """
        Creation of a Post
        Causes the User to create a Post under the authorized account.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets"
        params = {}
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def hide_reply_by_id(self,
        tweet_id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Hide replies
        Hides or unhides a reply to an owned conversation.
        Args:
            tweet_id: The ID of the reply that you want to hide or unhide.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{tweet_id}/hidden"
        params = {}
        url = url.replace("{tweet_id}", str(tweet_id))
        headers = {}
        headers["Content-Type"] = "application/json"
        # Make the request
        response = self.client.session.put(
            url,
            params=params,
            headers=headers,
            json=body,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()
