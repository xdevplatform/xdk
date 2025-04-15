"""
Users client for the X API.

This module provides a client for interacting with the Users endpoints of the X API.
"""

from typing import Dict, List, Optional, Any, Union
import requests
import requests_oauthlib
from ..client import Client


class UsersClient:
    """Client for Users operations"""


    def __init__(self, client: Client):
        self.client = client


    def tweets_id_retweeting_users(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Returns User objects that have retweeted the provided Post ID
        Returns a list of Users that have retweeted the provided Post ID
        Args:
            id: A single Post ID.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/retweeted_by"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def search_user_by_query(self,
        query: str,
        max_results: int = None,
        next_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        User search
        Returns Users that match a search query.
        Args:
            query: TThe the query string by which to query for users.
        Args:
            max_results: The maximum number of results.
        Args:
            next_token: This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/search"
        params = {}
        if query is not None:
            params["query"] = query
        if max_results is not None:
            params["max_results"] = max_results
        if next_token is not None:
            params["next_token"] = next_token
        if user_fields is not None:
            params["user.fields"] = user_fields
        if expansions is not None:
            params["expansions"] = expansions
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
        # Return the response data
        return response.json()


    def find_my_user(self,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        User lookup me
        This endpoint returns information about the requesting User.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/me"
        params = {}
        if user_fields is not None:
            params["user.fields"] = user_fields
        if expansions is not None:
            params["expansions"] = expansions
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
        # Return the response data
        return response.json()


    def tweets_id_liking_users(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Returns User objects that have liked the provided Post ID
        Returns a list of Users that have liked the provided Post ID
        Args:
            id: A single Post ID.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/tweets/{id}/liking_users"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def users_id_d_m_block(self,
        id: str,
    ) -> Dict[str, Any]:
        """
        Causes DMs to/from the target User (in the path) to be blocked by the authenticated request user
        Causes DMs to/from the target User (in the path) to be blocked by the authenticated request user
        Args:
            id: The ID of the target User that the authenticated user requesting to block dms for.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/dm/block"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def find_users_by_username(self,
        usernames: List,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        User lookup by usernames
        This endpoint returns information about Users. Specify Users by their username.
        Args:
            usernames: A list of usernames, comma-separated.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/by"
        params = {}
        if usernames is not None:
            params["usernames"] = usernames
        if user_fields is not None:
            params["user.fields"] = user_fields
        if expansions is not None:
            params["expansions"] = expansions
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
        # Return the response data
        return response.json()


    def find_user_by_username(self,
        username: str,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        User lookup by username
        This endpoint returns information about a User. Specify User by username.
        Args:
            username: A username.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/by/username/{username}"
        params = {}
        if user_fields is not None:
            params["user.fields"] = user_fields
        if expansions is not None:
            params["expansions"] = expansions
        if tweet_fields is not None:
            params["tweet.fields"] = tweet_fields
        url = url.replace("{username}", str(username))
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


    def users_id_muting(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Returns User objects that are muted by the provided User ID
        Returns a list of Users that are muted by the provided User ID
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get the next 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/muting"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def users_id_mute(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Mute User by User ID.
        Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.
        Args:
            id: The ID of the authenticated source User that is requesting to mute the target User.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/muting"
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


    def find_users_by_id(self,
        ids: List,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        User lookup by IDs
        This endpoint returns information about Users. Specify Users by their ID.
        Args:
            ids: A list of User IDs, comma-separated. You can specify up to 100 IDs.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users"
        params = {}
        if ids is not None:
            params["ids"] = ids
        if user_fields is not None:
            params["user.fields"] = user_fields
        if expansions is not None:
            params["expansions"] = expansions
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
        # Return the response data
        return response.json()


    def users_id_blocking(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Returns User objects that are blocked by provided User ID
        Returns a list of Users that are blocked by the provided User ID
        Args:
            id: The ID of the authenticated source User for whom to return results.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/blocking"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def users_id_following(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Following by User ID
        Returns a list of Users that are being followed by the provided User ID
        Args:
            id: The ID of the User to lookup.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/following"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def users_id_follow(self,
        id: str,
        body: Dict[str, Any]
               = None,
    ) -> Dict[str, Any]:
        """
        Follow User
        Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request
        Args:
            id: The ID of the authenticated source User that is requesting to follow the target User.
            body: Request body
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/following"
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


    def list_of_repost_of_user(self,
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
        Returns repost of user
        This endpoint returns reposts of the requesting User.
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
        url = self.client.base_url + "/2/users/reposts_of_me"
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


    def users_id_d_m_un_block(self,
        id: str,
    ) -> Dict[str, Any]:
        """
        Causes DMs to/from the target User (in the path) to be unblocked by the authenticated request user
        Causes DMs to/from the target User (in the path) to be unblocked by the authenticated request user
        Args:
            id: The ID of the target User that the authenticated user requesting to unblock dms for.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/dm/unblock"
        params = {}
        url = url.replace("{id}", str(id))
        headers = {}
        # Make the request
        response = self.client.session.post(
            url,
            params=params,
            headers=headers,
        )
        # Check for errors
        response.raise_for_status()
        # Return the response data
        return response.json()


    def users_id_unmute(self,
        source_user_id: str,
        target_user_id: str,
    ) -> Dict[str, Any]:
        """
        Unmute User by User ID
        Causes the source User to unmute the target User. The source User must match the User context authorizing the request
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unmute the target User.
        Args:
            target_user_id: The ID of the User that the source User is requesting to unmute.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{source_user_id}/muting/{target_user_id}"
        params = {}
        url = url.replace("{source_user_id}", str(source_user_id))
        url = url.replace("{target_user_id}", str(target_user_id))
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


    def list_get_members(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Returns User objects that are members of a List by the provided List ID.
        Returns a list of Users that are members of a List by the provided List ID.
        Args:
            id: The ID of the List.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/members"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def list_get_followers(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Returns User objects that follow a List by the provided List ID
        Returns a list of Users that follow a List by the provided List ID
        Args:
            id: The ID of the List.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/lists/{id}/followers"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def users_id_followers(self,
        id: str,
        max_results: int = None,
        pagination_token: str = None,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        Followers by User ID
        Returns a list of Users who are followers of the specified User ID.
        Args:
            id: The ID of the User to lookup.
        Args:
            max_results: The maximum number of results.
        Args:
            pagination_token: This parameter is used to get a specified 'page' of results.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}/followers"
        params = {}
        if max_results is not None:
            params["max_results"] = max_results
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
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


    def users_id_unfollow(self,
        source_user_id: str,
        target_user_id: str,
    ) -> Dict[str, Any]:
        """
        Unfollow User
        Causes the source User to unfollow the target User. The source User must match the User context authorizing the request
        Args:
            source_user_id: The ID of the authenticated source User that is requesting to unfollow the target User.
        Args:
            target_user_id: The ID of the User that the source User is requesting to unfollow.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{source_user_id}/following/{target_user_id}"
        params = {}
        url = url.replace("{source_user_id}", str(source_user_id))
        url = url.replace("{target_user_id}", str(target_user_id))
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


    def find_user_by_id(self,
        id: str,
        user_fields: List = None,
        expansions: List = None,
        tweet_fields: List = None,
    ) -> Dict[str, Any]:
        """
        User lookup by ID
        This endpoint returns information about a User. Specify User by ID.
        Args:
            id: The ID of the User to lookup.
        Args:
            user_fields: A comma separated list of User fields to display.
        Args:
            expansions: A comma separated list of fields to expand.
        Args:
            tweet_fields: A comma separated list of Tweet fields to display.
        Returns:
            Dict[str, Any]: Response data
        """
        url = self.client.base_url + "/2/users/{id}"
        params = {}
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
