
"""
Auto-generated posts client for the X API.

This module provides a client for interacting with the posts endpoints of the X API.

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
    
    
    GetCountsAllResponse,
    
    
    
    SearchRecentResponse,
    
    
    
    GetByIdResponse,
    
    
    
    DeleteResponse,
    
    
    
    GetByIdsResponse,
    
    
    
    CreateRequest,
    
    CreateResponse,
    
    
    
    
    HideReplyRequest,
    
    HideReplyResponse,
    
    
    
    
    GetRepostsResponse,
    
    
    
    GetAnalyticsResponse,
    
    
    
    SearchAllResponse,
    
    
    
    GetRepostedByResponse,
    
    
    
    GetInsightsHistoricalResponse,
    
    
    
    GetQuotedResponse,
    
    
    
    GetLikingUsersResponse,
    
    
    
    GetInsights28hrResponse,
    
    
    
    GetCountsRecentResponse,
    
    
)

class PostsClient:
    """Client for posts operations"""
    
    def __init__(self, client: Client):
        self.client = client
    
    
    def get_counts_all(self, query: str, start_time: str = None, end_time: str = None, since_id: Any = None, until_id: Any = None, next_token: Any = None, pagination_token: Any = None, granularity: str = None, search_countfields: List = None) -> GetCountsAllResponse:
        """
        Get count of all Posts
        
        Retrieves the count of Posts matching a search query from the full archive.
        
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            granularity: The granularity for the search counts results.
            search_countfields: A comma separated list of SearchCount fields to display.
            Returns:
            GetCountsAllResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/counts/all"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
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
            
        if search_countfields is not None:
            params["search_count.fields"] = ",".join(str(item) for item in search_countfields)
            
        
        
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
        
        return GetCountsAllResponse.model_validate(response_data)
        
        

    
    def search_recent(self, query: str, start_time: str = None, end_time: str = None, since_id: Any = None, until_id: Any = None, max_results: int = None, next_token: Any = None, pagination_token: Any = None, sort_order: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> SearchRecentResponse:
        """
        Search recent Posts
        
        Retrieves Posts from the last 7 days matching a search query.
        
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
            max_results: The maximum number of search results to be returned by a request.
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            sort_order: This order in which to return results.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            SearchRecentResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/recent"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
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
        
        return SearchRecentResponse.model_validate(response_data)
        
        

    
    def get_by_id(self, id: Any, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> GetByIdResponse:
        """
        Get Post by ID
        
        Retrieves details of a specific Post by its ID.
        
        Args:
            id: A single Post ID.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            GetByIdResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}"
        url = url.replace("{id}", str(id))
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        params = {}
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
        
        return GetByIdResponse.model_validate(response_data)
        
        

    
    def delete(self, id: Any) -> DeleteResponse:
        """
        Delete Post
        
        Deletes a specific Post by its ID, if owned by the authenticated user.
        
        Args:
            id: The ID of the Post to be deleted.
            Returns:
            DeleteResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}"
        url = url.replace("{id}", str(id))
        

        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        params = {}
        
        
        headers = {}
        
        
        # Prepare request data
        json_data = None
        
        
        
        















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
        
        return DeleteResponse.model_validate(response_data)
        
        

    
    def get_by_ids(self, ids: List, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> GetByIdsResponse:
        """
        Get Posts by IDs
        
        Retrieves details of multiple Posts by their IDs.
        
        Args:
            ids: A comma separated list of Post IDs. Up to 100 are allowed in a single request.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            GetByIdsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        params = {}
        if ids is not None:
            params["ids"] = ",".join(str(item) for item in ids)
            
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
        
        return GetByIdsResponse.model_validate(response_data)
        
        

    
    def create(self, body: CreateRequest) -> Dict[str, Any]:
        """
        Create or Edit Post
        
        Creates a new Post for the authenticated user, or edits an existing Post when edit_options are provided.
        
        body: Request body
        Returns:
            CreateResponse: Response data
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
        
        
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = body.model_dump(exclude_none=True) if hasattr(body, 'model_dump') else body
        
        
        
        















        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
                
                json=json_data,
                
            )
        else:
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
        
        return CreateResponse.model_validate(response_data)
        
        

    
    def hide_reply(self, tweet_id: Any, body: Optional[HideReplyRequest] = None) -> HideReplyResponse:
        """
        Hide reply
        
        Hides or unhides a reply to a conversation owned by the authenticated user.
        
        Args:
            tweet_id: The ID of the reply that you want to hide or unhide.
            body: Request body
        Returns:
            HideReplyResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{tweet_id}/hidden"
        url = url.replace("{tweet_id}", str(tweet_id))
        

        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        
        
        params = {}
        
        
        headers = {}
        headers["Content-Type"] = "application/json"
        
        
        # Prepare request data
        json_data = None
        if body is not None:
            json_data = body.model_dump(exclude_none=True) if hasattr(body, 'model_dump') else body
        
        
        
        















        # Make the request
        
        
        if self.client.oauth2_session:
            response = self.client.oauth2_session.put(
                url,
                params=params,
                headers=headers,
                
                json=json_data,
                
            )
        else:
            response = self.client.session.put(
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
        
        return HideReplyResponse.model_validate(response_data)
        
        

    
    def get_reposts(self, id: Any, max_results: int = None, pagination_token: Any = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> GetRepostsResponse:
        """
        Get Reposts
        
        Retrieves a list of Posts that repost a specific Post by its ID.
        
        Args:
            id: A single Post ID.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            GetRepostsResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/retweets"
        url = url.replace("{id}", str(id))
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
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
        
        return GetRepostsResponse.model_validate(response_data)
        
        

    
    def get_analytics(self, ids: List, end_time: str, start_time: str, granularity: str, analyticsfields: List = None) -> GetAnalyticsResponse:
        """
        Get Post analytics
        
        Retrieves analytics data for specified Posts within a defined time range.
        
        Args:
            ids: A comma separated list of Post IDs. Up to 100 are allowed in a single request.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
            granularity: The granularity for the search counts results.
            analyticsfields: A comma separated list of Analytics fields to display.
            Returns:
            GetAnalyticsResponse: Response data
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
            
        if analyticsfields is not None:
            params["analytics.fields"] = ",".join(str(item) for item in analyticsfields)
            
        
        
        headers = {}
        
        
        # Prepare request data
        json_data = None
        
        
        
        















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
        
        return GetAnalyticsResponse.model_validate(response_data)
        
        

    
    def search_all(self, query: str, start_time: str = None, end_time: str = None, since_id: Any = None, until_id: Any = None, max_results: int = None, next_token: Any = None, pagination_token: Any = None, sort_order: str = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> SearchAllResponse:
        """
        Search all Posts
        
        Retrieves Posts from the full archive matching a search query.
        
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
            max_results: The maximum number of search results to be returned by a request.
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            sort_order: This order in which to return results.
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            SearchAllResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/search/all"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
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
        
        return SearchAllResponse.model_validate(response_data)
        
        

    
    def get_reposted_by(self, id: Any, max_results: int = None, pagination_token: Any = None, userfields: List = None, expansions: List = None, tweetfields: List = None) -> GetRepostedByResponse:
        """
        Get Reposted by
        
        Retrieves a list of Users who reposted a specific Post by its ID.
        
        Args:
            id: A single Post ID.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            userfields: A comma separated list of User fields to display.
            expansions: A comma separated list of fields to expand.
            tweetfields: A comma separated list of Tweet fields to display.
            Returns:
            GetRepostedByResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/retweeted_by"
        url = url.replace("{id}", str(id))
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
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
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        
        
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
        
        return GetRepostedByResponse.model_validate(response_data)
        
        

    
    def get_insights_historical(self, tweet_ids: List, end_time: str, start_time: str, granularity: str, requested_metrics: List, engagementfields: List = None) -> GetInsightsHistoricalResponse:
        """
        Get historical Post insights
        
        Retrieves historical engagement metrics for specified Posts within a defined time range.
        
        Args:
            tweet_ids: List of PostIds for historical metrics.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the end of the time range.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The UTC timestamp representing the start of the time range.
            granularity: granularity of metrics response.
            requested_metrics: request metrics for historical request.
            engagementfields: A comma separated list of Engagement fields to display.
            Returns:
            GetInsightsHistoricalResponse: Response data
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
            params["requested_metrics"] = ",".join(str(item) for item in requested_metrics)
            
        if engagementfields is not None:
            params["engagement.fields"] = ",".join(str(item) for item in engagementfields)
            
        
        
        headers = {}
        
        
        # Prepare request data
        json_data = None
        
        
        
        















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
        
        return GetInsightsHistoricalResponse.model_validate(response_data)
        
        

    
    def get_quoted(self, id: Any, max_results: int = None, pagination_token: Any = None, exclude: List = None, tweetfields: List = None, expansions: List = None, mediafields: List = None, pollfields: List = None, userfields: List = None, placefields: List = None) -> GetQuotedResponse:
        """
        Get Quoted Posts
        
        Retrieves a list of Posts that quote a specific Post by its ID.
        
        Args:
            id: A single Post ID.
            max_results: The maximum number of results to be returned.
            pagination_token: This parameter is used to get a specified 'page' of results.
            exclude: The set of entities to exclude (e.g. 'replies' or 'retweets').
            tweetfields: A comma separated list of Tweet fields to display.
            expansions: A comma separated list of fields to expand.
            mediafields: A comma separated list of Media fields to display.
            pollfields: A comma separated list of Poll fields to display.
            userfields: A comma separated list of User fields to display.
            placefields: A comma separated list of Place fields to display.
            Returns:
            GetQuotedResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/quote_tweets"
        url = url.replace("{id}", str(id))
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
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
        
        return GetQuotedResponse.model_validate(response_data)
        
        

    
    def get_liking_users(self, id: Any, max_results: int = None, pagination_token: Any = None, userfields: List = None, expansions: List = None, tweetfields: List = None) -> GetLikingUsersResponse:
        """
        Get Liking Users
        
        Retrieves a list of Users who liked a specific Post by its ID.
        
        Args:
            id: A single Post ID.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            userfields: A comma separated list of User fields to display.
            expansions: A comma separated list of fields to expand.
            tweetfields: A comma separated list of Tweet fields to display.
            Returns:
            GetLikingUsersResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/liking_users"
        url = url.replace("{id}", str(id))
        

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
            
        if userfields is not None:
            params["user.fields"] = ",".join(str(item) for item in userfields)
            
        if expansions is not None:
            params["expansions"] = ",".join(str(item) for item in expansions)
            
        if tweetfields is not None:
            params["tweet.fields"] = ",".join(str(item) for item in tweetfields)
            
        
        
        headers = {}
        
        
        # Prepare request data
        json_data = None
        
        
        
        















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
        
        return GetLikingUsersResponse.model_validate(response_data)
        
        

    
    def get_insights28hr(self, tweet_ids: List, granularity: str, requested_metrics: List, engagementfields: List = None) -> GetInsights28hrResponse:
        """
        Get 28-hour Post insights
        
        Retrieves engagement metrics for specified Posts over the last 28 hours.
        
        Args:
            tweet_ids: List of PostIds for 28hr metrics.
            granularity: granularity of metrics response.
            requested_metrics: request metrics for historical request.
            engagementfields: A comma separated list of Engagement fields to display.
            Returns:
            GetInsights28hrResponse: Response data
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
            params["requested_metrics"] = ",".join(str(item) for item in requested_metrics)
            
        if engagementfields is not None:
            params["engagement.fields"] = ",".join(str(item) for item in engagementfields)
            
        
        
        headers = {}
        
        
        # Prepare request data
        json_data = None
        
        
        
        















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
        
        return GetInsights28hrResponse.model_validate(response_data)
        
        

    
    def get_counts_recent(self, query: str, start_time: str = None, end_time: str = None, since_id: Any = None, until_id: Any = None, next_token: Any = None, pagination_token: Any = None, granularity: str = None, search_countfields: List = None) -> GetCountsRecentResponse:
        """
        Get count of recent Posts
        
        Retrieves the count of Posts from the last 7 days matching a search query.
        
        Args:
            query: One query/rule/filter for matching Posts. Refer to https://t.co/rulelength to identify the max query length.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Posts will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).
            end_time: YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Posts will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).
            since_id: Returns results with a Post ID greater than (that is, more recent than) the specified ID.
            until_id: Returns results with a Post ID less than (that is, older than) the specified ID.
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            pagination_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            granularity: The granularity for the search counts results.
            search_countfields: A comma separated list of SearchCount fields to display.
            Returns:
            GetCountsRecentResponse: Response data
        """
        url = self.client.base_url + "/2/tweets/counts/recent"
        

        if self.client.bearer_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.bearer_token}"
        elif self.client.access_token:
            self.client.session.headers["Authorization"] = f"Bearer {self.client.access_token}"
        
        
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
            
        if search_countfields is not None:
            params["search_count.fields"] = ",".join(str(item) for item in search_countfields)
            
        
        
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
        
        return GetCountsRecentResponse.model_validate(response_data)
        
        

    