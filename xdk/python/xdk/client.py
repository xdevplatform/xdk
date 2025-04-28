"""
Main client for the X API.

This module provides a client for interacting with the X API.
"""

import requests
import requests_oauthlib
from typing import Dict, List, Optional, Union, Any


from .tweets.client import TweetsClient

from .likes.client import LikesClient

from .mediaupload.client import MediaUploadClient

from .compliance.client import ComplianceClient

from .users.client import UsersClient

from .connection.client import ConnectionClient

from .general.client import GeneralClient

from .trends.client import TrendsClient

from .spaces.client import SpacesClient

from .bookmarks.client import BookmarksClient

from .lists.client import ListsClient

from .usage.client import UsageClient

from .direct_messages.client import Direct_MessagesClient

from .community_notes.client import Community_NotesClient

from .communities.client import CommunitiesClient


class Client:
    """Client for interacting with the X API."""


    def __init__(
        self,
        api_key: str,
        api_secret: str,
        access_token: str,
        access_token_secret: str,
        base_url: str = "https://api.twitter.com",
        bearer_token: str = None,
    ):
        """Initialize the X API client.
        Args:
            api_key: The API key for the X API.
            api_secret: The API secret for the X API.
            access_token: The access token for the X API.
            access_token_secret: The access token secret for the X API.
            base_url: The base URL for the X API.
            bearer_token: The bearer token for the X API.
        """
        self.session = requests.Session()
        self.base_url = base_url
        self.bearer_token = bearer_token
        # Set up authentication
        self.session.auth = requests_oauthlib.OAuth1(
            api_key, api_secret, access_token, access_token_secret
        )
        # Initialize clients for each tag
        self.tweets = TweetsClient(self)
        self.likes = LikesClient(self)
        self.mediaupload = MediaUploadClient(self)
        self.compliance = ComplianceClient(self)
        self.users = UsersClient(self)
        self.connection = ConnectionClient(self)
        self.general = GeneralClient(self)
        self.trends = TrendsClient(self)
        self.spaces = SpacesClient(self)
        self.bookmarks = BookmarksClient(self)
        self.lists = ListsClient(self)
        self.usage = UsageClient(self)
        self.direct_messages = Direct_MessagesClient(self)
        self.community_notes = Community_NotesClient(self)
        self.communities = CommunitiesClient(self)
