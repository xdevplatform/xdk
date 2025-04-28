"""
Main client for the X API.

This module provides a client for interacting with the X API.
"""

import requests
import requests_oauthlib
from typing import Dict, List, Optional, Union, Any


from .users.client import UsersClient

from .direct_messages.client import Direct_MessagesClient

from .communities.client import CommunitiesClient

from .general.client import GeneralClient

from .compliance.client import ComplianceClient

from .mediaupload.client import MediaUploadClient

from .lists.client import ListsClient

from .trends.client import TrendsClient

from .spaces.client import SpacesClient

from .bookmarks.client import BookmarksClient

from .tweets.client import TweetsClient

from .community_notes.client import Community_NotesClient

from .usage.client import UsageClient

from .likes.client import LikesClient

from .connection.client import ConnectionClient


class Client:
    """Client for interacting with the X API."""


    def __init__(
        self,
        api_key: str,
        api_secret: str,
        access_token: str,
        access_token_secret: str,
        base_url: str = "https://api.twitter.com",
    ):
        """Initialize the X API client.
        Args:
            api_key: The API key for the X API.
            api_secret: The API secret for the X API.
            access_token: The access token for the X API.
            access_token_secret: The access token secret for the X API.
            base_url: The base URL for the X API.
        """
        self.session = requests.Session()
        self.base_url = base_url
        # Set up authentication
        self.session.auth = requests_oauthlib.OAuth1(
            api_key, api_secret, access_token, access_token_secret
        )
        # Initialize clients for each tag
        self.users = UsersClient(self)
        self.direct_messages = Direct_MessagesClient(self)
        self.communities = CommunitiesClient(self)
        self.general = GeneralClient(self)
        self.compliance = ComplianceClient(self)
        self.mediaupload = MediaUploadClient(self)
        self.lists = ListsClient(self)
        self.trends = TrendsClient(self)
        self.spaces = SpacesClient(self)
        self.bookmarks = BookmarksClient(self)
        self.tweets = TweetsClient(self)
        self.community_notes = Community_NotesClient(self)
        self.usage = UsageClient(self)
        self.likes = LikesClient(self)
        self.connection = ConnectionClient(self)
