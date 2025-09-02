"""
Auto-generated users client for the X API.

This module provides a client for interacting with the users endpoints of the X API.

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
    GetListMembershipsResponse,
    SearchResponse,
    LikePostRequest,
    LikePostResponse,
    GetBlockingResponse,
    UnrepostPostResponse,
    GetLikedPostsResponse,
    GetByIdsResponse,
    GetByIdResponse,
    GetByUsernameResponse,
    GetBookmarksResponse,
    CreateBookmarkRequest,
    CreateBookmarkResponse,
    GetMutingResponse,
    MuteUserRequest,
    MuteUserResponse,
    GetBookmarkFoldersResponse,
    UnfollowListResponse,
    UnfollowUserResponse,
    UnlikePostResponse,
    GetFollowingResponse,
    FollowUserRequest,
    FollowUserResponse,
    RepostPostRequest,
    RepostPostResponse,
    GetTimelineResponse,
    UnmuteUserResponse,
    DeleteBookmarkResponse,
    GetByUsernamesResponse,
    GetRepostsOfMeResponse,
    GetMentionsResponse,
    GetOwnedListsResponse,
    GetPostsResponse,
    GetMeResponse,
    GetBookmarksByFolderIdResponse,
    UnblockDmsResponse,
    GetFollowedListsResponse,
    FollowListRequest,
    FollowListResponse,
    GetFollowersResponse,
    GetPinnedListsResponse,
    PinListRequest,
    PinListResponse,
    BlockDmsResponse,
    UnpinListResponse,
)


class UsersClient:
    """Client for users operations"""


    def __init__(self, client: Client):
        self.client = client


    def get_list_memberships(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetListMembershipsResponse:
        """
        Get List memberships
        Retrieves a list of Lists that a specific User is a member of by their ID.
        Args:
            id: The ID of the User to lookup.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetListMembershipsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/list_memberships"
        url = url.replace("{id}", str(id))
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
        return GetListMembershipsResponse.model_validate(response_data)


    def search(
        self, query: Any, max_results: int = None, next_token: Any = None
    ) -> SearchResponse:
        """
        Search Users
        Retrieves a list of Users matching a search query.
        Args:
            query: TThe the query string by which to query for users.
            max_results: The maximum number of results.
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
            Returns:
            SearchResponse: Response data
        """
        url = self.client.base_url + "/2/users/search"
        # Ensure we have a valid access token
        if self.client.oauth2_auth and self.client.token:
            # Check if token needs refresh
            if self.client.is_token_expired():
                self.client.refresh_token()
        params = {}
        if query is not None:
            params["query"] = query
        if max_results is not None:
            params["max_results"] = max_results
        if next_token is not None:
            params["next_token"] = next_token
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
        return SearchResponse.model_validate(response_data)


    def like_post(
        self, id: Any, body: Optional[LikePostRequest] = None
    ) -> LikePostResponse:
        """
        Like Post
        Causes the authenticated user to Like a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to like the Post.
            body: Request body
        Returns:
            LikePostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/likes"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return LikePostResponse.model_validate(response_data)


    def get_blocking(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetBlockingResponse:
        """
        Get blocking
        Retrieves a list of Users blocked by the specified User ID.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetBlockingResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/blocking"
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
        return GetBlockingResponse.model_validate(response_data)


    def unrepost_post(self, id: Any, source_tweet_id: Any) -> UnrepostPostResponse:
        """
        Unrepost Post
        Causes the authenticated user to unrepost a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
            source_tweet_id: The ID of the Post that the User is requesting to unretweet.
            Returns:
            UnrepostPostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/retweets/{source_tweet_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{source_tweet_id}", str(source_tweet_id))
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
        return UnrepostPostResponse.model_validate(response_data)


    def get_liked_posts(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetLikedPostsResponse:
        """
        Get liked Posts
        Retrieves a list of Posts liked by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            Returns:
            GetLikedPostsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/liked_tweets"
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
        return GetLikedPostsResponse.model_validate(response_data)


    def get_by_ids(self, ids: List) -> GetByIdsResponse:
        """
        Get Users by IDs
        Retrieves details of multiple Users by their IDs.
        Args:
            ids: A list of User IDs, comma-separated. You can specify up to 100 IDs.
            Returns:
            GetByIdsResponse: Response data
        """
        url = self.client.base_url + "/2/users"
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


    def get_by_id(self, id: Any) -> GetByIdResponse:
        """
        Get User by ID
        Retrieves details of a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            Returns:
            GetByIdResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}"
        url = url.replace("{id}", str(id))
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


    def get_by_username(self, username: str) -> GetByUsernameResponse:
        """
        Get User by username
        Retrieves details of a specific User by their username.
        Args:
            username: A username.
            Returns:
            GetByUsernameResponse: Response data
        """
        url = self.client.base_url + "/2/users/by/username/{username}"
        url = url.replace("{username}", str(username))
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
        return GetByUsernameResponse.model_validate(response_data)


    def get_bookmarks(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetBookmarksResponse:
        """
        Get Bookmarks
        Retrieves a list of Posts bookmarked by the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            Returns:
            GetBookmarksResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks"
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
        return GetBookmarksResponse.model_validate(response_data)


    def create_bookmark(
        self, id: Any, body: CreateBookmarkRequest
    ) -> CreateBookmarkResponse:
        """
        Create Bookmark
        Adds a post to the authenticated user’s bookmarks.
        Args:
            id: The ID of the authenticated source User for whom to add bookmarks.
            body: Request body
        Returns:
            CreateBookmarkResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return CreateBookmarkResponse.model_validate(response_data)


    def get_muting(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetMutingResponse:
        """
        Get muting
        Retrieves a list of Users muted by the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            Returns:
            GetMutingResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/muting"
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
        return GetMutingResponse.model_validate(response_data)


    def mute_user(
        self, id: Any, body: Optional[MuteUserRequest] = None
    ) -> MuteUserResponse:
        """
        Mute User
        Causes the authenticated user to mute a specific User by their ID.
        Args:
            id: The ID of the authenticated source User that is requesting to mute the target User.
            body: Request body
        Returns:
            MuteUserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/muting"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return MuteUserResponse.model_validate(response_data)


    def get_bookmark_folders(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetBookmarkFoldersResponse:
        """
        Get Bookmark folders
        Retrieves a list of Bookmark folders created by the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            Returns:
            GetBookmarkFoldersResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/folders"
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
        return GetBookmarkFoldersResponse.model_validate(response_data)


    def unfollow_list(self, id: Any, list_id: Any) -> UnfollowListResponse:
        """
        Unfollow List
        Causes the authenticated user to unfollow a specific List by its ID.
        Args:
            id: The ID of the authenticated source User that will unfollow the List.
            list_id: The ID of the List to unfollow.
            Returns:
            UnfollowListResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists/{list_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{list_id}", str(list_id))
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
        return UnfollowListResponse.model_validate(response_data)


    def unfollow_user(
        self, source_user_id: Any, target_user_id: Any
    ) -> UnfollowUserResponse:
        """
        Unfollow User
        Causes the authenticated user to unfollow a specific user by their ID.
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unfollow the target User.
            target_user_id: The ID of the User that the source User is requesting to unfollow.
            Returns:
            UnfollowUserResponse: Response data
        """
        url = (
            self.client.base_url
            + "/2/users/{source_user_id}/following/{target_user_id}"
        )
        url = url.replace("{source_user_id}", str(source_user_id))
        url = url.replace("{target_user_id}", str(target_user_id))
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
        return UnfollowUserResponse.model_validate(response_data)


    def unlike_post(self, id: Any, tweet_id: Any) -> UnlikePostResponse:
        """
        Unlike Post
        Causes the authenticated user to Unlike a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to unlike the Post.
            tweet_id: The ID of the Post that the User is requesting to unlike.
            Returns:
            UnlikePostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/likes/{tweet_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{tweet_id}", str(tweet_id))
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
        return UnlikePostResponse.model_validate(response_data)


    def get_following(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetFollowingResponse:
        """
        Get following
        Retrieves a list of Users followed by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetFollowingResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/following"
        url = url.replace("{id}", str(id))
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
        return GetFollowingResponse.model_validate(response_data)


    def follow_user(
        self, id: Any, body: Optional[FollowUserRequest] = None
    ) -> FollowUserResponse:
        """
        Follow User
        Causes the authenticated user to follow a specific user by their ID.
        Args:
            id: The ID of the authenticated source User that is requesting to follow the target User.
            body: Request body
        Returns:
            FollowUserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/following"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return FollowUserResponse.model_validate(response_data)


    def repost_post(
        self, id: Any, body: Optional[RepostPostRequest] = None
    ) -> RepostPostResponse:
        """
        Repost Post
        Causes the authenticated user to repost a specific Post by its ID.
        Args:
            id: The ID of the authenticated source User that is requesting to repost the Post.
            body: Request body
        Returns:
            RepostPostResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/retweets"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return RepostPostResponse.model_validate(response_data)


    def get_timeline(
        self,
        id: Any,
        since_id: Any = None,
        until_id: Any = None,
        max_results: int = None,
        pagination_token: Any = None,
        exclude: List = None,
        start_time: str = None,
        end_time: str = None,
    ) -> GetTimelineResponse:
        """
        Get Timeline
        Retrieves a reverse chronological list of Posts in the authenticated User’s Timeline.
        Args:
            id: The ID of the authenticated source User to list Reverse Chronological Timeline Posts of.
            since_id: The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
            until_id: The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            exclude: The set of entities to exclude (e.g. 'replies' or 'retweets').
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
            Returns:
            GetTimelineResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/timelines/reverse_chronological"
        url = url.replace("{id}", str(id))
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
        return GetTimelineResponse.model_validate(response_data)


    def unmute_user(
        self, source_user_id: Any, target_user_id: Any
    ) -> UnmuteUserResponse:
        """
        Unmute User
        Causes the authenticated user to unmute a specific user by their ID.
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unmute the target User.
            target_user_id: The ID of the User that the source User is requesting to unmute.
            Returns:
            UnmuteUserResponse: Response data
        """
        url = self.client.base_url + "/2/users/{source_user_id}/muting/{target_user_id}"
        url = url.replace("{source_user_id}", str(source_user_id))
        url = url.replace("{target_user_id}", str(target_user_id))
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
        return UnmuteUserResponse.model_validate(response_data)


    def delete_bookmark(self, id: Any, tweet_id: Any) -> DeleteBookmarkResponse:
        """
        Delete Bookmark
        Removes a Post from the authenticated user’s Bookmarks by its ID.
        Args:
            id: The ID of the authenticated source User whose bookmark is to be removed.
            tweet_id: The ID of the Post that the source User is removing from bookmarks.
            Returns:
            DeleteBookmarkResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/{tweet_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{tweet_id}", str(tweet_id))
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
        return DeleteBookmarkResponse.model_validate(response_data)


    def get_by_usernames(self, usernames: List) -> GetByUsernamesResponse:
        """
        Get Users by usernames
        Retrieves details of multiple Users by their usernames.
        Args:
            usernames: A list of usernames, comma-separated.
            Returns:
            GetByUsernamesResponse: Response data
        """
        url = self.client.base_url + "/2/users/by"
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
        if usernames is not None:
            params["usernames"] = ",".join(str(item) for item in usernames)
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
        return GetByUsernamesResponse.model_validate(response_data)


    def get_reposts_of_me(
        self, max_results: int = None, pagination_token: Any = None
    ) -> GetRepostsOfMeResponse:
        """
        Get Reposts of me
        Retrieves a list of Posts that repost content from the authenticated user.
        Args:
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            Returns:
            GetRepostsOfMeResponse: Response data
        """
        url = self.client.base_url + "/2/users/reposts_of_me"
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
        return GetRepostsOfMeResponse.model_validate(response_data)


    def get_mentions(
        self,
        id: Any,
        since_id: Any = None,
        until_id: Any = None,
        max_results: int = None,
        pagination_token: Any = None,
        start_time: str = None,
        end_time: str = None,
    ) -> GetMentionsResponse:
        """
        Get mentions
        Retrieves a list of Posts that mention a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            since_id: The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
            until_id: The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
            Returns:
            GetMentionsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/mentions"
        url = url.replace("{id}", str(id))
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
        return GetMentionsResponse.model_validate(response_data)


    def get_owned_lists(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetOwnedListsResponse:
        """
        Get owned Lists
        Retrieves a list of Lists owned by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetOwnedListsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/owned_lists"
        url = url.replace("{id}", str(id))
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
        return GetOwnedListsResponse.model_validate(response_data)


    def get_posts(
        self,
        id: Any,
        since_id: Any = None,
        until_id: Any = None,
        max_results: int = None,
        pagination_token: Any = None,
        exclude: List = None,
        start_time: str = None,
        end_time: str = None,
    ) -> GetPostsResponse:
        """
        Get Posts
        Retrieves a list of posts authored by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            since_id: The minimum Post ID to be included in the result set. This parameter takes precedence over start_time if both are specified.
            until_id: The maximum Post ID to be included in the result set. This parameter takes precedence over end_time if both are specified.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get the next 'page' of results.
            exclude: The set of entities to exclude (e.g. 'replies' or 'retweets').
            start_time: YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Posts will be provided. The since_id parameter takes precedence if it is also specified.
            end_time: YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Posts will be provided. The until_id parameter takes precedence if it is also specified.
            Returns:
            GetPostsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/tweets"
        url = url.replace("{id}", str(id))
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
        return GetPostsResponse.model_validate(response_data)


    def get_me(
        self,
    ) -> GetMeResponse:
        """
        Get my User
        Retrieves details of the authenticated user.
        Returns:
            GetMeResponse: Response data
        """
        url = self.client.base_url + "/2/users/me"
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
        return GetMeResponse.model_validate(response_data)


    def get_bookmarks_by_folder_id(
        self, id: Any, folder_id: Any
    ) -> GetBookmarksByFolderIdResponse:
        """
        Get Bookmarks by folder ID
        Retrieves Posts in a specific Bookmark folder by its ID for the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            folder_id: The ID of the Bookmark Folder that the authenticated User is trying to fetch Posts for.
            Returns:
            GetBookmarksByFolderIdResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/bookmarks/folders/{folder_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{folder_id}", str(folder_id))
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
        return GetBookmarksByFolderIdResponse.model_validate(response_data)


    def unblock_dms(self, id: Any) -> UnblockDmsResponse:
        """
        Unblock DMs
        Unblocks direct messages to or from a specific User by their ID for the authenticated user.
        Args:
            id: The ID of the target User that the authenticated user requesting to unblock dms for.
            Returns:
            UnblockDmsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/dm/unblock"
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
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return UnblockDmsResponse.model_validate(response_data)


    def get_followed_lists(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetFollowedListsResponse:
        """
        Get followed Lists
        Retrieves a list of Lists followed by a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetFollowedListsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"
        url = url.replace("{id}", str(id))
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
        return GetFollowedListsResponse.model_validate(response_data)


    def follow_list(
        self, id: Any, body: Optional[FollowListRequest] = None
    ) -> FollowListResponse:
        """
        Follow List
        Causes the authenticated user to follow a specific List by its ID.
        Args:
            id: The ID of the authenticated source User that will follow the List.
            body: Request body
        Returns:
            FollowListResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followed_lists"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return FollowListResponse.model_validate(response_data)


    def get_followers(
        self, id: Any, max_results: int = None, pagination_token: Any = None
    ) -> GetFollowersResponse:
        """
        Get followers
        Retrieves a list of Users who follow a specific User by their ID.
        Args:
            id: The ID of the User to lookup.
            max_results: The maximum number of results.
            pagination_token: This parameter is used to get a specified 'page' of results.
            Returns:
            GetFollowersResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followers"
        url = url.replace("{id}", str(id))
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
        return GetFollowersResponse.model_validate(response_data)


    def get_pinned_lists(self, id: Any) -> GetPinnedListsResponse:
        """
        Get pinned Lists
        Retrieves a list of Lists pinned by the authenticated user.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            Returns:
            GetPinnedListsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists"
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
        return GetPinnedListsResponse.model_validate(response_data)


    def pin_list(self, id: Any, body: PinListRequest) -> PinListResponse:
        """
        Pin List
        Causes the authenticated user to pin a specific List by its ID.
        Args:
            id: The ID of the authenticated source User that will pin the List.
            body: Request body
        Returns:
            PinListResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists"
        url = url.replace("{id}", str(id))
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
            json_data = (
                body.model_dump(exclude_none=True)
                if hasattr(body, "model_dump")
                else body
            )
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
        return PinListResponse.model_validate(response_data)


    def block_dms(self, id: Any) -> BlockDmsResponse:
        """
        Block DMs
        Blocks direct messages to or from a specific User by their ID for the authenticated user.
        Args:
            id: The ID of the target User that the authenticated user requesting to block dms for.
            Returns:
            BlockDmsResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/dm/block"
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
            response = self.client.oauth2_session.post(
                url,
                params=params,
                headers=headers,
            )
        else:
            response = self.client.session.post(
                url,
                params=params,
                headers=headers,
            )
        # Check for errors
        response.raise_for_status()
        # Parse the response data
        response_data = response.json()
        # Convert to Pydantic model if applicable
        return BlockDmsResponse.model_validate(response_data)


    def unpin_list(self, id: Any, list_id: Any) -> UnpinListResponse:
        """
        Unpin List
        Causes the authenticated user to unpin a specific List by its ID.
        Args:
            id: The ID of the authenticated source User for whom to return results.
            list_id: The ID of the List to unpin.
            Returns:
            UnpinListResponse: Response data
        """
        url = self.client.base_url + "/2/users/{id}/pinned_lists/{list_id}"
        url = url.replace("{id}", str(id))
        url = url.replace("{list_id}", str(list_id))
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
        return UnpinListResponse.model_validate(response_data)
