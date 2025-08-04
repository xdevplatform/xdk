"""
Main client for the X API.

This module provides a client for interacting with the X API.
"""

import requests
from typing import Dict, List, Optional, Union, Any, Callable

from .oauth2_auth import OAuth2PKCEAuth
from .paginator import Cursor, cursor, PaginationError

from .connection.client import ConnectionClient

from .spaces.client import SpacesClient

from .stream.client import StreamClient

from .community_notes.client import CommunityNotesClient

from .direct_messages.client import DirectMessagesClient

from .compliance.client import ComplianceClient

from .webhooks.client import WebhooksClient

from .tweets.client import TweetsClient

from .media.client import MediaClient

from .likes.client import LikesClient

from .aaasubscriptions.client import AAASubscriptionsClient

from .account_activity.client import AccountActivityClient

from .usage.client import UsageClient

from .users.client import UsersClient

from .communities.client import CommunitiesClient

from .bookmarks.client import BookmarksClient

from .lists.client import ListsClient

from .general.client import GeneralClient

from .trends.client import TrendsClient


class Client:
    """Client for interacting with the X API."""


    def __init__(
        self,
        base_url: str = "https://api.twitter.com",
        bearer_token: str = None,
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = None,
        token: Dict[str, Any] = None,
        scope: str = None,
    ):
        """Initialize the X API client.
        Args:
            base_url: The base URL for the X API.
            bearer_token: The bearer token for the X API.
            client_id: The client ID for the X API.
            client_secret: The client secret for the X API.
            redirect_uri: The redirect URI for OAuth2 authorization.
            token: An existing OAuth2 token dictionary (if available).
            scope: Space-separated list of scopes for OAuth2 authorization.
        """
        self.session = requests.Session()
        self.base_url = base_url
        self.bearer_token = bearer_token
        # Set up OAuth2 PKCE authentication if credentials are provided
        self.oauth2_auth = None
        if client_id or token:
            self.oauth2_auth = OAuth2PKCEAuth(
                base_url=base_url,
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                token=token,
                scope=scope,
            )
        # Initialize clients for each tag
        self.connection = ConnectionClient(self)
        self.spaces = SpacesClient(self)
        self.stream = StreamClient(self)
        self.community_notes = CommunityNotesClient(self)
        self.direct_messages = DirectMessagesClient(self)
        self.compliance = ComplianceClient(self)
        self.webhooks = WebhooksClient(self)
        self.tweets = TweetsClient(self)
        self.media = MediaClient(self)
        self.likes = LikesClient(self)
        self.aaasubscriptions = AAASubscriptionsClient(self)
        self.account_activity = AccountActivityClient(self)
        self.usage = UsageClient(self)
        self.users = UsersClient(self)
        self.communities = CommunitiesClient(self)
        self.bookmarks = BookmarksClient(self)
        self.lists = ListsClient(self)
        self.general = GeneralClient(self)
        self.trends = TrendsClient(self)

    @property


    def oauth2_session(self):
        """Get the OAuth2 session if available."""
        if self.oauth2_auth:
            return self.oauth2_auth.oauth2_session
        return None

    @property


    def token(self):
        """Get the current OAuth2 token if available."""
        if self.oauth2_auth:
            return self.oauth2_auth.token
        return None

    @property


    def access_token(self):
        """Get the current access token if available."""
        if self.oauth2_auth:
            return self.oauth2_auth.access_token
        return None


    def get_authorization_url(self):
        """Get the authorization URL for the OAuth2 PKCE flow."""
        if not self.oauth2_auth:
            raise ValueError("OAuth2 credentials not configured")
        return self.oauth2_auth.get_authorization_url()


    def fetch_token(self, authorization_response):
        """Fetch token using authorization response."""
        if not self.oauth2_auth:
            raise ValueError("OAuth2 credentials not configured")
        return self.oauth2_auth.fetch_token(authorization_response)


    def refresh_token(self):
        """Refresh the OAuth2 token."""
        if not self.oauth2_auth:
            raise ValueError("OAuth2 credentials not configured")
        return self.oauth2_auth.refresh_token()


    def is_token_expired(self):
        """Check if the OAuth2 token is expired."""
        if not self.oauth2_auth:
            return True
        return self.oauth2_auth.is_token_expired()
