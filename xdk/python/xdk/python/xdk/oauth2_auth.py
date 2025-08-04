"""
OAuth2 PKCE authentication for the X API.

This module provides OAuth2 PKCE authentication functionality for the X API client.
"""

import secrets
import base64
import hashlib
import time
import urllib.parse
from typing import Dict, Optional, Any, Tuple
from requests_oauthlib import OAuth2Session


class OAuth2PKCEAuth:
    """OAuth2 PKCE authentication for the X API."""


    def __init__(
        self,
        base_url: str = "https://api.twitter.com",
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = None,
        token: Dict[str, Any] = None,
        scope: str = None,
    ):
        """Initialize the OAuth2 PKCE authentication.
        Args:
            base_url: The base URL for the X API.
            client_id: The client ID for the X API.
            client_secret: The client secret for the X API.
            redirect_uri: The redirect URI for OAuth2 authorization.
            token: An existing OAuth2 token dictionary (if available).
            scope: Space-separated list of scopes for OAuth2 authorization.
        """
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token = token
        self.scope = scope
        self.oauth2_session = None
        self.code_verifier = None
        self.code_challenge = None
        # Set up OAuth2 session if we have a token
        if token and client_id:
            self._setup_oauth_session()


    def _setup_oauth_session(self):
        """Set up the OAuth2 session with existing token."""
        self.oauth2_session = OAuth2Session(
            client_id=self.client_id,
            token=self.token,
            redirect_uri=self.redirect_uri,
            scope=self.scope,
        )


    def _generate_code_verifier(self, length: int = 128) -> str:
        """Generate a code verifier for PKCE.
        Args:
            length: The length of the code verifier.
        Returns:
            str: The generated code verifier.
        """
        code_verifier = secrets.token_urlsafe(96)[:length]
        return code_verifier


    def _generate_code_challenge(self, code_verifier: str) -> str:
        """Generate a code challenge from the code verifier.
        Args:
            code_verifier: The code verifier to generate a challenge from.
        Returns:
            str: The generated code challenge.
        """
        code_challenge = hashlib.sha256(code_verifier.encode()).digest()
        code_challenge = base64.urlsafe_b64encode(code_challenge).decode().rstrip("=")
        return code_challenge


    def get_authorization_url(self) -> Tuple[str, str]:
        """Get the authorization URL for the OAuth2 PKCE flow.
        Returns:
            tuple: (authorization_url, state)
        """
        self.code_verifier = self._generate_code_verifier()
        self.code_challenge = self._generate_code_challenge(self.code_verifier)
        self.oauth2_session = OAuth2Session(
            client_id=self.client_id, redirect_uri=self.redirect_uri, scope=self.scope
        )
        auth_url, state = self.oauth2_session.authorization_url(
            f"{self.base_url}/oauth2/authorize",
            code_challenge=self.code_challenge,
            code_challenge_method="S256",
        )
        return auth_url, state


    def fetch_token(self, authorization_response: str) -> Dict[str, Any]:
        """Fetch token using authorization response and code verifier.
        Args:
            authorization_response: The full callback URL received after authorization
        Returns:
            Dict[str, Any]: The token dictionary
        """
        if not self.oauth2_session:
            raise ValueError(
                "OAuth2 session not initialized. Call get_authorization_url first."
            )
        self.token = self.oauth2_session.fetch_token(
            f"{self.base_url}/oauth2/token",
            authorization_response=authorization_response,
            code_verifier=self.code_verifier,
            client_id=self.client_id,
            include_client_id=True,
        )
        return self.token


    def refresh_token(self) -> Dict[str, Any]:
        """Refresh the access token.
        Returns:
            Dict[str, Any]: The refreshed token dictionary
        """
        if not self.oauth2_session or not self.token:
            raise ValueError("No token to refresh")
        refresh_url = f"{self.base_url}/oauth2/token"
        self.token = self.oauth2_session.refresh_token(
            refresh_url, client_id=self.client_id, client_secret=self.client_secret
        )
        return self.token

    @property


    def access_token(self) -> Optional[str]:
        """Get the current access token.
        Returns:
            Optional[str]: The current access token, or None if no token exists.
        """
        if self.token:
            return self.token.get("access_token")
        return None


    def is_token_expired(self) -> bool:
        """Check if the token is expired.
        Returns:
            bool: True if the token is expired, False otherwise.
        """
        if not self.token or "expires_at" not in self.token:
            return True
        # Add a 10-second buffer to avoid edge cases
        return time.time() > (self.token["expires_at"] - 10)
